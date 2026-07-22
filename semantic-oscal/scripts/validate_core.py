#!/usr/bin/env python3
"""OSCAL Semantic Core - gate-item-2 executable validator.

Runs, in order:
1. CONFORMANCE CORPUS: JCS vectors (canonical form + empty-omission rule),
   modality-lattice vectors, parameter vectors, tailoring vectors
   (same-target conflict, tier-scoped Deviation duties), attestation
   bi-modal vectors.
2. BUNDLE VALIDATION over every converted_examples bundle + the skill's
   example bundle: type inference (an object must match EXACTLY ONE of the
   nine kernel shapes - shape-disjointness is a conformance property),
   closed-shape schema validation, code systems, by-statement facet keys
   vs. host statement ids (D10 rev), {param:} token binding (the 216
   rule), optional-empty-container rule (D3.3), manifest completeness +
   both digests re-verified per object.

Exit 0 = all green. Usage: uv run --with jsonschema validate_core.py [bundle-dir ...]
"""
import json, hashlib, os, re, sys, copy, collections
import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SKILL = os.path.join(ROOT, "semantic-oscal")
SCHEMA = json.load(open(os.path.join(SKILL, "schemas", "oscal-semantic-core-1.0.0.schema.json"), encoding="utf-8"))
CONF = os.path.join(SKILL, "conformance")

TYPES = ["requirement", "requirementSet", "tailoring", "mapping", "component",
         "implementation", "assessment", "finding", "attestation"]
REGISTRY = jsonschema.validators.Draft202012Validator
VALIDATORS = {t: REGISTRY({"$ref": f"#/$defs/{t}", "$defs": SCHEMA["$defs"]}) for t in TYPES}
VALIDATORS["contentManifest"] = REGISTRY({"$ref": "#/$defs/contentManifest", "$defs": SCHEMA["$defs"]})

# normative stdlib facet descriptors (gate 2); payload validation per backlog #17
STDLIB = {}
for _fn in sorted(os.listdir(os.path.join(SKILL, "schemas", "stdlib"))):
    if _fn.endswith(".json"):
        _d = json.load(open(os.path.join(SKILL, "schemas", "stdlib", _fn), encoding="utf-8"))
        STDLIB[_d["id"]] = REGISTRY(_d["schema"])

# reference taxonomy (backlog #16): closure-required refs MUST land in-bundle;
# landmark refs (Mapping endpoints, party/authority URIs, evidence, external
# schema/reference URLs, attestation subjects — self-verifying via digest)
# resolve outside the bundle by design.
def closure_errors(objs):
    """objs: id -> (type, obj). Returns list of error strings."""
    errs = []
    def need(oid, ref, what):
        if ref not in objs:
            errs.append(f"{oid}: closure-required {what} does not resolve in-bundle: {ref}")
    for oid, (t, o) in objs.items():
        for ca in o.get("canonical-alias", []) or []:   # backlog #14: same-content is checkable
            tgt = objs.get(ca.get("of"))
            if tgt and content_digest(o) != content_digest(tgt[1]):
                errs.append(f"{oid}: canonical-alias claims SAME content as {ca.get('of')} "
                            f"but content digests differ — a meaning change must use `replaces` (backlog #14)")
        if t == "requirementSet":
            for m in o.get("members", []): need(oid, m["ref"], "member ref")
        elif t == "tailoring":
            for s in o.get("selects", []):
                if "set-ref" in s: need(oid, s["set-ref"], "selects set-ref")
            for e in o.get("excludes", []): need(oid, e["ref"], "excludes ref")
            for op in o.get("operations", []):
                need(oid, op["requirement-ref"], "operation requirement-ref")
                tgt = objs.get(op["requirement-ref"])
                if tgt and op.get("statement-id") and tgt[0] == "requirement":
                    if op["statement-id"] not in {s["id"] for s in tgt[1]["statements"]}:
                        errs.append(f"{oid}: operation statement-id '{op['statement-id']}' names no statement of {op['requirement-ref']}")
        elif t == "implementation":
            need(oid, o["component-ref"], "component-ref")
            need(oid, o["requirement-ref"], "requirement-ref")
            for sb in o.get("satisfied-by", []):
                inh = sb.get("inherited-from")
                if inh:
                    comp = objs.get(inh["component-ref"])
                    if not comp:
                        errs.append(f"{oid}: inherited-from component does not resolve in-bundle: {inh['component-ref']}")
                    elif inh["basis-ref"] not in {a["id"] for a in comp[1].get("authorizations", [])}:
                        errs.append(f"{oid}: basis-ref '{inh['basis-ref']}' names no authorization of {inh['component-ref']} (D5 edge-local rule)")
        elif t == "finding":
            need(oid, o["assessment-ref"], "assessment-ref")
            need(oid, o["requirement-ref"], "requirement-ref")
        elif t == "mapping":
            for side in ("source", "target"):   # endpoints are landmark; scopes bind IF the endpoint is present
                ep = objs.get(o.get(f"{side}-ref"))
                if ep and ep[0] == "requirement":
                    sids = {s["id"] for s in ep[1]["statements"]}
                    for sc in o.get(f"{side}-scope", []):
                        sid = sc.split(":", 1)[1]
                        if sid not in sids:
                            errs.append(f"{oid}: {side}-scope '{sc}' names no statement of the in-bundle endpoint")
    return errs

def facet_errors(objs_or_obj, pinned, path="?"):
    """Validate facet payloads (backlog #17): stdlib facets against the
    normative descriptors, others against the bundle-pinned schemas;
    private: is ignored by definition; anything else is unregistered."""
    errs = []
    items = objs_or_obj if isinstance(objs_or_obj, list) else [(path, objs_or_obj)]
    for pth, obj in items:
        for key, payload in (obj.get("facets") or {}).items():
            base = key.rsplit("@", 1)[0]
            if key.startswith("private:") or base.startswith("private:"):
                continue   # modifies-semantics [] by definition (D10)
            v = STDLIB.get(base) or pinned.get(base)
            if v is None:
                errs.append(f"{pth}: unregistered facet '{key}' — not stdlib, not pinned in the manifest, not private: (dangerous-by-default, D10)")
                continue
            err = next(iter(v.iter_errors(payload)), None)
            if err:
                errs.append(f"{pth}: facet '{key}' payload violates its schema: {err.message[:110]} @ {'/'.join(map(str, err.absolute_path))}")
    return errs

# tier anchor (backlog #19, layered - D13 rev 2): id-prefix derivation gives
# authority-CLAIMED; an in-bundle Attestation whose signer shares the selected
# content's origin and whose subjects include the Tailoring (digest-verified)
# upgrades to authority-PROVEN; anything else is consumer. Deviation duties
# bind at consumer tier only; claimed/proven are reported distinctly.
STDLIB_DECL = {}
for _fn in sorted(os.listdir(os.path.join(SKILL, "schemas", "stdlib"))):
    if _fn.endswith(".json"):
        _d = json.load(open(os.path.join(SKILL, "schemas", "stdlib", _fn), encoding="utf-8"))
        STDLIB_DECL[_d["id"]] = _d.get("modifies-semantics", [])

def uri_origin(u):
    p = str(u).split("/")
    return "/".join(p[:3]) if str(u).startswith("http") and len(p) >= 3 else str(u)

def derive_tier(tobj, objs, sdig_fn):
    origins = set()
    for s in tobj.get("selects", []):
        origins.add(uri_origin(s["set-ref"]) if "set-ref" in s else "<predicate>")
    content_origin = next(iter(origins)) if len(origins) == 1 and "<predicate>" not in origins else None
    claimed = content_origin is not None and uri_origin(tobj["id"]) == content_origin
    if content_origin:
        for (t, o) in objs.values():
            if t != "attestation" or uri_origin(o.get("signer", "")) != content_origin:
                continue
            for subj in o.get("subject-semantic-digests", []):
                if isinstance(subj, dict) and subj.get("id") == tobj["id"] \
                   and subj.get("semantic-digest") == sdig_fn(tobj):
                    return "authority-proven"
    return "authority-claimed" if claimed else "consumer"

def tailoring_duty_errors(objs, pinned_decl=None, sdig_fn=None):
    """Op-law enforcement with the derived tier (D13 + #19)."""
    errs = []
    pd = pinned_decl or {}
    for oid, (t, tobj) in objs.items():
        if t != "tailoring": continue
        tier = derive_tier(tobj, objs, sdig_fn or sdig)
        for op in tobj.get("operations", []):
            has_dev = "deviation" in op or "deviation-ref" in op
            duty = None
            if op["op"] == "set-modality":
                tgt = objs.get(op["requirement-ref"])
                if tgt and tgt[0] == "requirement":
                    stmt = next((s for s in tgt[1]["statements"] if s["id"] == op.get("statement-id")), None)
                    if stmt:
                        v = modality_verdict_py(stmt["modality"], op["modality"])
                        if v != "monotone": duty = f"non-monotone set-modality ({v})"
            elif op["op"] == "replace-prose" and op.get("intent") == "substantive":
                duty = "substantive replace-prose"
            elif op["op"] in ("attach-facet", "detach-facet"):
                base = str(op.get("facet", "")).rsplit("@", 1)[0]
                decl = STDLIB_DECL.get(base, pd.get(base))
                if decl: duty = f"{op['op']} of a semantics-bearing facet {decl}"
            elif op["op"] == "set-parameter":
                tgt = objs.get(op["requirement-ref"])
                stmt = next((s for s in tgt[1]["statements"] if s["id"] == op.get("statement-id")), None) \
                    if tgt and tgt[0] == "requirement" else None
                pdecl = next((p for p in stmt.get("parameters", []) if p["name"] == op.get("parameter")), None) \
                    if stmt else None
                if pdecl:
                    verdict = param_check(pdecl, op.get("value"))
                    if verdict == "invalid":   # type/cardinality/choice/range failure — malformed at ANY tier, not Deviation-escapable (D13)
                        errs.append(f"{oid}: set-parameter '{op.get('parameter')}' value fails the declared type/bounds "
                                    f"(D13; not Deviation-escapable)")
                    elif verdict == "deviation-required":
                        duty = "out-of-bounds / against-tightening set-parameter"
            elif op["op"] == "remove-relation":
                rel = op.get("relation")
                if isinstance(rel, dict) and rel.get("type") == "required":
                    duty = "remove-relation of a `required` edge"
            if duty and not has_dev and tier == "consumer":
                errs.append(f"{oid}: {duty} without a Deviation at consumer tier "
                            f"(derived tier: {tier}; B.1.6/D13 rev 2)")
    return errs

OBL_ORD = {"unspecified": 0, "may": 1, "should": 2, "must": 3}
PRO_ORD = {"unspecified": 0, "should-not": 1, "must-not": 2}
def modality_verdict_py(frm, to):
    if frm == to or frm == "unspecified": return "monotone"
    if to == "unspecified": return "easing"
    if frm == "may" and to == "may-only": return "monotone"
    if frm == "may-only" and to == "may": return "easing"
    if "may-only" in (frm, to): return "axis-change"
    if frm in OBL_ORD and to in OBL_ORD: return "monotone" if OBL_ORD[to] >= OBL_ORD[frm] else "easing"
    if frm in PRO_ORD and to in PRO_ORD: return "monotone" if PRO_ORD[to] >= PRO_ORD[frm] else "easing"
    return "axis-change"

# per-type optional array/object fields (D3.3: optional empties MUST be absent;
# required fields stay even when empty)
OPTIONAL_CONTAINERS = {"aliases", "canonical-alias", "replaces", "relations", "facets",
                       "annotations", "parameters", "deviations", "excludes",
                       "source-scope", "target-scope", "evidence-refs", "statement-refs",
                       "capabilities", "authorizations", "actions", "choices"}
REQUIRED_CONTAINERS = {"statements", "members", "selects", "operations", "subject-refs",
                       "satisfied-by", "subject-semantic-digests", "objects", "facet-schemas"}

fails = []
counts = collections.Counter()
def ok(section): counts[section] += 1
def fail(section, msg):
    counts[section + ":FAIL"] += 1
    fails.append(f"[{section}] {msg}")

# ---------------- canonical form ----------------
def _canon(o):
    # RFC 8785 member ordering: UTF-16 code units, not code points (P9b-3).
    if isinstance(o, dict):
        return {k: _canon(o[k]) for k in sorted(o.keys(), key=lambda s: s.encode("utf-16-be"))}
    if isinstance(o, list):
        return [_canon(x) for x in o]
    return o
def canonical(obj):
    o = copy.deepcopy(obj)
    if isinstance(o, dict): o.pop("annotations", None)
    return json.dumps(_canon(o), separators=(",", ":"), ensure_ascii=False)
def sdig(obj):
    return "sha256:" + hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()

def content_digest(obj):
    # sameness modulo identity (backlog #14): strip the fields a rebrand may
    # legitimately change, then digest what remains. canonical-alias asserts
    # SAME content at a new home; if these differ, it should be `replaces`.
    x = copy.deepcopy(obj)
    for k in ("id", "version", "label", "canonical-alias", "replaces"):
        x.pop(k, None)
    return sdig(x)

def optional_empty_violations(obj, path="$"):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in OPTIONAL_CONTAINERS and isinstance(v, (list, dict)) and len(v) == 0:
                out.append(f"{path}.{k}")
            out += optional_empty_violations(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out += optional_empty_violations(v, f"{path}[{i}]")
    return out

# ---------------- modality lattice ----------------
OBL = {"unspecified": 0, "may": 1, "should": 2, "must": 3}
PRO = {"unspecified": 0, "should-not": 1, "must-not": 2}
def modality_verdict(frm, to):
    if frm == to: return "monotone"
    if frm == "unspecified": return "monotone"
    if to == "unspecified": return "easing"
    if frm == "may" and to == "may-only": return "monotone"
    if frm == "may-only" and to == "may": return "easing"
    if "may-only" in (frm, to): return "axis-change"
    fo, to_o = frm in OBL, to in OBL
    fp, tp = frm in PRO, to in PRO
    if fo and to_o: return "monotone" if OBL[to] >= OBL[frm] else "easing"
    if fp and tp: return "monotone" if PRO[to] >= PRO[frm] else "easing"
    return "axis-change"

# ---------------- parameter law ----------------
def param_check(decl, value):
    t = decl.get("type")
    if t == "calendar-period" and "calendar-ref" not in decl: return "invalid"
    if value is None: return "invalid"
    if t == "choice":
        allowed = [c["value"] for c in decl.get("choices", [])]
        return "valid" if value in allowed else "deviation-required"
    if t == "integer":
        if not isinstance(value, int) or isinstance(value, bool): return "invalid"
        if "min" in decl and value < decl["min"]: return "deviation-required"
        if "max" in decl and value > decl["max"]: return "deviation-required"
        return "valid"
    if t == "decimal":
        # canonical decimal STRING (D3.4): no leading zeros; scale is lexically
        # significant (trailing zeros distinguish "1.5" from "1.50" by design).
        if not isinstance(value, str) or not re.match(r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?$", value): return "invalid"
        v = float(value)
        if "min" in decl and v < decl["min"]: return "deviation-required"
        if "max" in decl and v > decl["max"]: return "deviation-required"
        return "valid"
    if t in ("elapsed-duration", "calendar-period"):
        ELAPSED = {"seconds", "minutes", "hours"}; CAL = {"days", "bizdays", "weeks", "months", "years"}
        if not isinstance(value, dict) or "num" not in value or "unit" not in value: return "invalid"
        cls = ELAPSED if t == "elapsed-duration" else CAL
        if value["unit"] not in cls: return "invalid"   # unit-class boundary is semantic
        if decl.get("tightening") == "lower":
            base = decl.get("num")
            if base is not None and value["unit"] == decl.get("unit") and value["num"] > base:
                return "deviation-required"
        return "valid"
    return "valid"

# ---------------- 1) conformance corpus ----------------
def run_jcs():
    v = json.load(open(os.path.join(CONF, "jcs-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        name = case["name"]
        if "canonical" in case and case.get("canonical") is not None:
            got = canonical(case["input"])
            if got == case["canonical"]: ok("jcs")
            else: fail("jcs", f"{name}: got {got!r}")
        elif "authoring-input" in case:
            viol = optional_empty_violations(case["authoring-input"])
            verdict = "invalid" if viol else "valid"
            if verdict == case["expected"]: ok("jcs")
            else: fail("jcs", f"{name}: expected {case['expected']}, got {verdict} ({viol})")

def run_modality():
    v = json.load(open(os.path.join(CONF, "modality-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        got = modality_verdict(case["from"], case["to"])
        if got == case["verdict"]: ok("modality")
        else: fail("modality", f"{case['from']} -> {case['to']}: expected {case['verdict']}, got {got}")

def run_parameters():
    v = json.load(open(os.path.join(CONF, "parameter-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        got = param_check(case["parameter"], case["value"])
        if got == case["verdict"]: ok("parameter")
        else: fail("parameter", f"{case['name']}: expected {case['verdict']}, got {got}")

def run_tailoring():
    v = json.load(open(os.path.join(CONF, "tailoring-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        ops = case.get("operations", [])
        verdict = "valid"
        seen = set()
        for op in ops:
            key = (op.get("requirement-ref"), op.get("statement-id"),
                   op.get("parameter"), op.get("field"), op.get("facet"), op.get("op"))
            tkey = key[:5]
            if tkey in seen: verdict = "error"
            seen.add(tkey)
        if verdict != "error":
            for op in ops:
                needs_dev = False
                if op["op"] == "set-modality" and "base-modality" in case:
                    needs_dev = modality_verdict(case["base-modality"], op["modality"]) != "monotone"
                if op["op"] == "replace-prose" and op.get("intent") == "substantive":
                    needs_dev = True
                if op["op"] == "set-parameter" and "parameter-decl" in case:   # backlog #25
                    pv = param_check(case["parameter-decl"], op.get("value"))
                    if pv == "invalid": verdict = "error"                       # malformed at any tier
                    elif pv == "deviation-required": needs_dev = True
                if op["op"] == "remove-relation" and isinstance(op.get("relation"), dict) \
                        and op["relation"].get("type") == "required":           # backlog #25 (B.3)
                    needs_dev = True
                if needs_dev and case.get("tier") == "consumer" and "deviation" not in op and "deviation-ref" not in op:
                    verdict = "error"
        if verdict == case["verdict"]: ok("tailoring")
        else: fail("tailoring", f"{case['name']}: expected {case['verdict']}, got {verdict}")

def run_attestation():
    v = json.load(open(os.path.join(CONF, "attestation-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        sc = case["scenario"]
        signed = sc["subject"]
        signed_sem = sdig(signed)
        signed_pkg = "sha256:" + hashlib.sha256(json.dumps(signed, indent=1, ensure_ascii=False).encode()).hexdigest()
        delivered = copy.deepcopy(sc.get("delivered-subject", signed))
        mut = sc["delivered-mutation"]
        if mut == "reindent":
            delivered_bytes = json.dumps(delivered, indent=4, ensure_ascii=False).encode()
        elif mut == "annotation-added":
            delivered["annotations"] = {"web_name": "chrome"}
            delivered_bytes = json.dumps(delivered, indent=1, ensure_ascii=False).encode()
        else:
            delivered_bytes = json.dumps(delivered, indent=1, ensure_ascii=False).encode()
        del_pkg = "sha256:" + hashlib.sha256(delivered_bytes).hexdigest()
        del_sem = sdig(json.loads(delivered_bytes.decode()))
        if del_sem != signed_sem: got = "tamper"
        elif del_pkg == signed_pkg: got = "full-match"
        else: got = "semantic-match"
        if got == case["expected"]: ok("attestation")
        else: fail("attestation", f"{case['name']}: expected {case['expected']}, got {got}")

def run_facets():
    v = json.load(open(os.path.join(CONF, "facet-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        pinned = {k: REGISTRY(s) for k, s in (case.get("pinned") or {}).items()}
        errs = facet_errors(case["object"], pinned, case["name"])
        got = "invalid" if errs else "valid"
        if got == case["expected"]: ok("facet")
        else: fail("facet", f"{case['name']}: expected {case['expected']}, got {got} ({errs[:1]})")

def run_references():
    v = json.load(open(os.path.join(CONF, "reference-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        objs = {}
        for o in case["objects"]:
            t = inferType_single(o)
            if t: objs[o["id"]] = (t, o)
        errs = closure_errors(objs)
        if len(errs) == case["expected-errors"]: ok("reference")
        else: fail("reference", f"{case['name']}: expected {case['expected-errors']} errors, got {len(errs)} ({errs[:2]})")

def inferType_single(o):
    m = [t for t in TYPES if VALIDATORS[t].is_valid(o)]
    return m[0] if len(m) == 1 else None

DEV_NEXT = {"investigating": {"pending", "withdrawn"}, "pending": {"approved", "withdrawn"},
            "approved": set(), "withdrawn": set()}
FIND_NEXT = {"open": {"in-remediation", "closed"}, "in-remediation": {"closed"}, "closed": set()}
def run_tiers():
    v = json.load(open(os.path.join(CONF, "tier-vectors.json"), encoding="utf-8"))
    for case in v["vectors"]:
        # substitute live-computed digests BEFORE type inference — the
        # COMPUTE placeholder would otherwise fail the digest pattern
        by_id = {o["id"]: o for o in case["objects"]}
        for o in case["objects"]:
            for subj in o.get("subject-semantic-digests", []) or []:
                if isinstance(subj, dict) and subj.get("semantic-digest") == "COMPUTE":
                    tgt = by_id.get(subj["id"])
                    if tgt: subj["semantic-digest"] = sdig(tgt)
        objs = {}
        for o in case["objects"]:
            t = inferType_single(o)
            if t: objs[o["id"]] = (t, o)
        tobj = next(o for (t, o) in objs.values() if t == "tailoring")
        tier = derive_tier(tobj, objs, sdig)
        errs = tailoring_duty_errors(objs)
        got = "invalid" if errs else "valid"
        okv = tier == case["expected-tier"] and got == case["expected"]
        if okv: ok("tier")
        else: fail("tier", f"{case['name']}: expected {case['expected-tier']}/{case['expected']}, got {tier}/{got} ({errs[:1]})")

def run_lifecycle():
    v = json.load(open(os.path.join(CONF, "lifecycle-vectors.json"), encoding="utf-8"))
    for case in v["deviation-transitions"]:
        got = case["to"] in DEV_NEXT[case["from"]]
        if got == case["valid"]: ok("lifecycle")
        else: fail("lifecycle", f"deviation {case['from']}->{case['to']}: expected valid={case['valid']}")
    for case in v["finding-transitions"]:
        got = case["to"] in FIND_NEXT[case["from"]]
        if got == case["valid"]: ok("lifecycle")
        else: fail("lifecycle", f"finding {case['from']}->{case['to']}: expected valid={case['valid']}")
    for case in v["identity-events"]:
        allowed = case["record"] == "canonical-alias"
        want = case["substitution"] == "allowed"
        if allowed == want: ok("lifecycle")
        else: fail("lifecycle", f"identity {case['record']}: substitution rule mismatch")
    def compose(a, b):
        if "supplements" in (a, b): return None
        if a == b == "equal": return "equal"
        if a == "equal": return b
        if b == "equal" and a != "equal": return a if a == "supports" else "supports"
        return "supports"
    for case in v["relationship-composition"]:
        got = compose(case["a"], case["b"])
        # floor semantics: composed claim must never be STRONGER than expected
        okv = got == case["composed"] or (case["composed"] == "supports" and got in ("supports", "intersects"))
        if okv: ok("lifecycle")
        else: fail("lifecycle", f"compose({case['a']},{case['b']}): expected {case['composed']}, got {got}")
    # shape disjointness: nine canonical minimal objects -> exactly one match each; garbage -> zero
    P = "https://ex.org"
    MINIMAL = {
        "requirement": {"id": P+"/r", "version": "1", "lifecycle": "active",
            "statements": [{"id": "s1", "modality": "must", "obligated-parties": [P+"/p"], "prose": {"en": "X."}}]},
        "requirementSet": {"id": P+"/s", "version": "1", "lifecycle": "active", "members": [{"ref": P+"/r", "sequence": 10}]},
        "tailoring": {"id": P+"/t", "version": "1", "lifecycle": "active", "selects": [{"set-ref": P+"/s"}]},
        "mapping": {"id": P+"/m", "version": "1", "lifecycle": "active", "source-ref": P+"/r", "target-ref": P+"/r2",
            "relationship": "supports", "direction": "source-to-target", "confidence": "draft",
            "provenance": {"author-ref": P+"/p", "date": "2026-07-21"}},
        "component": {"id": P+"/c", "version": "1", "lifecycle": "active", "kind": "service"},
        "implementation": {"id": P+"/i", "version": "1", "lifecycle": "active", "component-ref": P+"/c",
            "requirement-ref": P+"/r", "responsibility": "provider",
            "satisfied-by": [{"capability-ref": "cap"}], "status": "implemented"},
        "assessment": {"id": P+"/a", "version": "1", "lifecycle": "active", "subject-refs": [P+"/r"],
            "method": {"kind": "review"}, "performer-ref": P+"/p", "time": "2026-07-21", "result": "satisfied"},
        "finding": {"id": P+"/f", "version": "1", "lifecycle": "active", "assessment-ref": P+"/a",
            "requirement-ref": P+"/r", "state": "open"},
        "attestation": {"id": P+"/at", "version": "1", "lifecycle": "active",
            "subject-semantic-digests": ["sha256:" + "0"*64], "content-manifest-digest": "sha256:" + "0"*64,
            "signer": P+"/p", "timestamp": "2026-07-21"},
    }
    for want, o in MINIMAL.items():
        m = [t for t in TYPES if VALIDATORS[t].is_valid(o)]
        if m == [want]: ok("lifecycle")
        else: fail("lifecycle", f"disjointness: minimal {want} matches {m}")
    if [t for t in TYPES if VALIDATORS[t].is_valid({"id": P+"/x", "version": "1", "lifecycle": "active"})]:
        fail("lifecycle", "disjointness: field-free object matches a type")
    else: ok("lifecycle")

# ---------------- 2) bundle validation ----------------
PARAM_TOKEN = re.compile(r"\{param:([^}]+)\}")

def infer_type(obj):
    matches = [t for t in TYPES if VALIDATORS[t].is_valid(obj)]
    return matches

def validate_object(section, path, obj):
    matches = infer_type(obj)
    if len(matches) != 1:
        best = ""
        if not matches:
            errs = sorted(VALIDATORS["requirement"].iter_errors(obj), key=lambda e: -len(e.absolute_path))
            guess = {t: len(list(VALIDATORS[t].iter_errors(obj))) for t in TYPES}
            t0 = min(guess, key=guess.get)
            e0 = next(iter(VALIDATORS[t0].iter_errors(obj)), None)
            best = f" (closest {t0}: {e0.message[:110] if e0 else '?'} @ {'/'.join(map(str, e0.absolute_path)) if e0 else ''})"
        fail(section, f"{path}: matches {matches or 'NO type'}{best}")
        return None
    ok(section)
    t = matches[0]
    viol = optional_empty_violations(obj)
    if viol: fail(section, f"{path}: optional empty containers present: {viol}")
    if t == "requirement":
        sids = {s["id"] for s in obj["statements"]}
        if len(sids) != len(obj["statements"]):
            fail(section, f"{path}: duplicate statement ids (unique-within, B.1.3) — identity addressing becomes ambiguous")
        for s in obj["statements"]:
            declared = {p["name"] for p in s.get("parameters", [])}
            for lang, txt in s["prose"].items():
                for tok in PARAM_TOKEN.findall(txt if isinstance(txt, str) else " ".join(txt)):
                    if tok not in declared:
                        fail(section, f"{path}: unbound {{param:{tok}}} in statement {s['id']} (the 216 rule)")
        for fid, payload in (obj.get("facets") or {}).items():
            if isinstance(payload, dict) and "by-statement" in payload and isinstance(payload["by-statement"], dict):
                for sid in payload["by-statement"]:
                    if sid not in sids:
                        fail(section, f"{path}: facet {fid} by-statement key '{sid}' names no statement (D10 rev)")
    return t

def validate_bundle(bdir):
    section = os.path.relpath(bdir, ROOT).replace("\\", "/")
    mpath = os.path.join(bdir, "content-manifest.json")
    if not os.path.exists(mpath):
        fail(section, "no content-manifest.json"); return
    manifest = json.load(open(mpath, encoding="utf-8"))
    if not VALIDATORS["contentManifest"].is_valid(manifest):
        e = next(VALIDATORS["contentManifest"].iter_errors(manifest))
        fail(section, f"manifest schema: {e.message[:120]} @ {'/'.join(map(str, e.absolute_path))}")
    else:
        ok(section)
    listed = {e["path"]: e for e in manifest.get("objects", [])}
    typec = collections.Counter()
    seen_ids = {}
    bundle_objs = {}
    for rel, entry in listed.items():
        fp = os.path.join(bdir, rel)
        if not os.path.exists(fp):
            fail(section, f"{rel}: listed but missing"); continue
        raw = open(fp, "rb").read()
        if "sha256:" + hashlib.sha256(raw).hexdigest() != entry["package-digest"]:
            fail(section, f"{rel}: package-digest mismatch")
        obj = json.loads(raw.decode("utf-8"))
        if sdig(obj) != entry["semantic-digest"]:
            fail(section, f"{rel}: semantic-digest mismatch")
        t = validate_object(section, rel, obj)
        if t: typec[t] += 1
        if obj.get("id") != entry["id"]:
            fail(section, f"{rel}: manifest id != object id")
        if obj.get("id") in seen_ids:
            fail(section, f"{rel}: object id already used by {seen_ids[obj['id']]} (unique-within — the twin-catalog corpse)")
        seen_ids[obj.get("id")] = rel
        if t: bundle_objs[obj["id"]] = (t, obj)
    # pinned facet schemas: files must exist, digests must verify, and they
    # form the registry for non-stdlib facet payload validation (#17)
    pinned = {}
    for fe in manifest.get("facet-schemas", []):
        fp = os.path.join(bdir, fe["path"])
        if not os.path.exists(fp):
            fail(section, f"{fe['path']}: pinned facet schema listed but missing"); continue
        raw = open(fp, "rb").read()
        if "sha256:" + hashlib.sha256(raw).hexdigest() != fe["digest"]:
            fail(section, f"{fe['path']}: pinned facet schema digest mismatch")
        try:
            sd = json.loads(raw.decode("utf-8"))
            pinned[sd["id"]] = REGISTRY(sd.get("schema", {"type": "object"}))
        except Exception as e:
            fail(section, f"{fe['path']}: pinned facet schema unreadable: {e}")
    # reference taxonomy (#16) + facet payloads (#17) + tier duties (#19)
    for e in closure_errors(bundle_objs):
        fail(section, e)
    for e in tailoring_duty_errors(bundle_objs):
        fail(section, e)
    for e in facet_errors([(oid, o) for oid, (t, o) in bundle_objs.items()], pinned):
        fail(section, e)
    # #24: report the derived Tailoring tier DISTINCTLY (spec:399) — a prefix
    # claim is an honest-publisher signal, not proof; signature verification of
    # the proven tier is gate-4 (DSSE engine).
    for tid, (tt, tobj2) in sorted(bundle_objs.items()):
        if tt == "tailoring":
            tr = derive_tier(tobj2, bundle_objs, sdig)
            note = {"authority-claimed": " [prefix claim - UNPROVEN]",
                    "authority-proven": " [attestation digest-matched; signature check is gate-4]"}.get(tr, "")
            print(f"    tier: {tid} = {tr}{note}")
    on_disk = set()
    for base, _, files in os.walk(bdir):
        for fn in files:
            rel = os.path.relpath(os.path.join(base, fn), bdir).replace("\\", "/")
            if rel.startswith("objects/") and rel.endswith(".json"): on_disk.add(rel)
    for rel in sorted(on_disk - set(listed)):
        fail(section, f"{rel}: on disk but not in manifest")
    return typec

def validate_examples():
    exdir = os.path.join(SKILL, "examples")
    section = "skill-examples"
    typec = collections.Counter()
    for fn in sorted(os.listdir(exdir)):
        if not fn.endswith(".json") or "manifest" in fn or "stub" in fn or fn.startswith(("gspp-taxonomy",)):
            continue
        obj = json.load(open(os.path.join(exdir, fn), encoding="utf-8"))
        t = validate_object(section, fn, obj)
        if t: typec[t] += 1
    return typec

# ---------------- run ----------------
print("== conformance corpus ==")
run_jcs(); run_modality(); run_parameters(); run_tailoring(); run_attestation(); run_facets(); run_references(); run_lifecycle(); run_tiers()
for k in ("jcs", "modality", "parameter", "tailoring", "attestation", "facet", "reference", "lifecycle", "tier"):
    print(f"  {k}: {counts[k]} pass, {counts[k + ':FAIL']} fail")

print("== bundles ==")
targets = sys.argv[1:]
if not targets:
    ce = os.path.join(ROOT, "converted_examples")
    targets = []
    for corpus in sorted(os.listdir(ce)):
        cdir = os.path.join(ce, corpus)
        if not os.path.isdir(cdir): continue
        for d in sorted(os.listdir(cdir)):
            if d.endswith("-bundle") and os.path.isdir(os.path.join(cdir, d)):
                targets.append(os.path.join(cdir, d))
total_types = collections.Counter()
for b in targets:
    tc = validate_bundle(b) or collections.Counter()
    total_types += tc
    sec = os.path.relpath(b, ROOT).replace("\\", "/")
    print(f"  {sec}: {counts[sec]} pass, {counts[sec + ':FAIL']} fail  {dict(tc)}")
tc = validate_examples()
total_types += tc
print(f"  skill-examples: {counts['skill-examples']} pass, {counts['skill-examples:FAIL']} fail  {dict(tc)}")
print("== type coverage ==", dict(total_types))

if fails:
    print(f"\n{len(fails)} FAILURES:")
    for f in fails[:60]: print("  -", f)
    sys.exit(1)
print("\nALL GREEN")
