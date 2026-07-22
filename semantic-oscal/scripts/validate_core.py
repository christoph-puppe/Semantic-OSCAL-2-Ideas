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
def canonical(obj):
    o = copy.deepcopy(obj)
    if isinstance(o, dict): o.pop("annotations", None)
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
def sdig(obj):
    return "sha256:" + hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()

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
        if not isinstance(value, str) or not re.match(r"^-?[0-9]+(\.[0-9]+)?$", value): return "invalid"
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
run_jcs(); run_modality(); run_parameters(); run_tailoring(); run_attestation()
for k in ("jcs", "modality", "parameter", "tailoring", "attestation"):
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
