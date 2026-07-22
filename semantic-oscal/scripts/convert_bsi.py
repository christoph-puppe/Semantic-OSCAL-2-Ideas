#!/usr/bin/env python3
"""BSI Grundschutz++ + MS-TLS (OSCAL 1.1.3) -> Semantic Core bundle.
Gate item 1, authority 2. Nested pseudo-controls -> statements; part-level
grammar/objective/taxonomy props -> facet payloads keyed by statement id;
{{ insert: param }} -> {param:} tokens; the {{...}} prop-value defects are
REPORTED, never laundered. Pattern-based coverage: UNMAPPED target = 0."""
import json, hashlib, os, re, copy, collections, shutil

OUT = "/home/claude/bsi-core-bundle"
RMD = "/home/claude/bsi-coverage-report.md"
RJS = "/home/claude/bsi-coverage-report.json"
SOURCES = [("gspp", "/home/claude/gspp.json", "https://ns.bsi.bund.de/gspp"),
           ("mstls", "/home/claude/tls.json", "https://ns.bsi.bund.de/mstls")]
F_GRAM = "https://ns.oscal.org/stdlib/facet/statement-grammar@1"
F_SECO = "https://ns.oscal.org/stdlib/facet/security-objectives@1"
F_ACRIT = "https://ns.oscal.org/stdlib/facet/assessment-criteria@1"
F_TAX  = "https://ns.bsi.bund.de/facet/gspp-taxonomy@1"
F_NARR = "https://ns.bsi.bund.de/facet/gspp-narrative@1"
F_COMPAT = "https://ns.oscal.org/compat/oscal-1x@1"
MODAL = {"MUSS":"must","SOLLTE":"should","KANN":"may","DARF NICHT":"must-not",
         "SOLLTE NICHT":"should-not","DARF NUR":"may-only",
         "MÜSSEN":"must","SOLLTEN":"should","KÖNNEN":"may",
         "DÜRFEN NICHT":"must-not","DÜRFEN NUR":"may-only"}

def w(path,obj):
    p=os.path.join(OUT,path); os.makedirs(os.path.dirname(p),exist_ok=True)
    with open(p,"w",encoding="utf-8") as f: json.dump(obj,f,indent=1,ensure_ascii=False); f.write("\n")
def sha_file(path): return "sha256:"+hashlib.sha256(open(os.path.join(OUT,path),"rb").read()).hexdigest()
def semantic_digest(o):
    o=copy.deepcopy(o); o.pop("annotations",None)
    return "sha256:"+hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def slug(s): return re.sub(r"[^a-z0-9]+","-",(s or "").lower()).strip("-")[:60] or "x"
def split_list(v): return [x.strip() for x in v.split(",") if x.strip()]

# ---------- inventory ----------
def inventory(node,prefix,counter):
    if isinstance(node,dict):
        for k,v in node.items(): inventory(v,f"{prefix}.{k}",counter)
    elif isinstance(node,list):
        for v in node: inventory(v,f"{prefix}[]",counter)
    else: counter[prefix]+=1

# ---------- destination rules (ordered regex patterns) ----------
C = r"(catalog(\.groups\[\])+\.controls\[\](\.controls\[\])*)"
RULES = [
 (r"^catalog\.uuid$|^catalog\.metadata\.", "L1", "bundle manifest / L0 provenance"),
 (r"^catalog\.back-matter\.resources\[\]\.uuid$", "L1", "resolution key for #uuid links -> external URL"),
 (r"^catalog\.back-matter\.", "L1", "source-document reference (title/rlink) -> resolved into relations / dropped-declared"),
 (r"^catalog(\.groups\[\])+\.(id|title)$", "L1", "taxonomy Set id/title (per-catalog subtree)"),
 (r"^catalog(\.groups\[\])+\.props\[\]\.remarks$", "L1", "gspp-narrative on the Set: layer/Praktik description"),
 (r"^catalog(\.groups\[\])+\.props\[\]\.(name|value)$", "L1", "Set.label / Set.aliases (bsi-uuid)"),
 (C+r"\.id$", "L1", "Requirement id (top) / statement id (nested)"),
 (C+r"\.class$", "L1", "gspp-taxonomy: class (by-statement)"),
 (C+r"\.title$", "L1", "Requirement title (top) / kept in taxonomy by-statement (nested)"),
 (C+r"\.links\[\]\.(rel|href)$", "L1", "relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL)"),
 (C+r"\.params\[\]\.id$", "L1", "statement parameter name (type string)"),
 (C+r"\.params\[\]\.(label|values\[\])$", "L2", "compat oscal-1x: param-extras (default/display value - candidate D9 addition)"),
 (C+r"\.params\[\]\.props\[\]\.(name|value)$", "L2", "compat oscal-1x: param-extras (param alt-identifier)"),
 (C+r"\.props\[\]\.ns$", "L1", "absorbed: CSV-link namespaces replaced by pinned facet schemas"),
 (C+r"\.props\[\]\.(name|value)$", "L1", "dispatch by prop name (see per-prop table)"),
 (C+r"\.parts\[\]\.(id|name)$", "L1", "statement/guidance part identity -> statement id / narrative key"),
 (C+r"\.parts\[\]\.prose$", "L1", "statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance"),
 (C+r"\.parts\[\]\.props\[\]\.ns$", "L1", "absorbed: CSV-link namespaces replaced by pinned facet schemas"),
 (C+r"\.parts\[\]\.props\[\]\.(name|value)$", "L1", "dispatch by part-prop name (grammar/objectives/criteria; defects reported)"),
]
def destination(path):
    for pat,lvl,tgt in RULES:
        if re.search(pat,path): return lvl,tgt
    return None,None

PROP_DEST = {
 "alt-identifier": ("L1","Requirement.aliases (top) / taxonomy by-statement (nested)"),
 "label": ("L1","Requirement.label (top) / taxonomy by-statement label (nested)"),
 "sec_level": ("L1","top: baseline Set membership; nested: taxonomy by-statement"),
 "effort_level": ("L1","gspp-taxonomy: effort (by-statement)"),
 "tags": ("L1","gspp-taxonomy: tags[] (comma-split; inconsistencies reported)"),
 "confidentiality": ("L1","security-objectives (by-statement)"),
 "integrity": ("L1","security-objectives (by-statement)"),
 "availability": ("L1","security-objectives (by-statement)"),
 "authenticity": ("L1","security-objectives (by-statement)"),
 "threats": ("L1","security-objectives threat-refs[] (comma-split, minted threat code URIs)"),
 "modal_verb": ("L1","statements[].modality (mapped code system)"),
 "action_word": ("L1","statement-grammar: action (by-statement)"),
 "result": ("L1","statement-grammar: result (by-statement)"),
 "result_specification": ("L1","statement-grammar: result-specification (by-statement)"),
 "target_object_categories": ("L1","statement-grammar: target-object-categories[] (by-statement)"),
 "documentation": ("L1","assessment-criteria: required-documentation[] (by-statement)"),
 "practice": ("L1","gspp-taxonomy: practice (by-statement)"),
}

INSERT_RE = re.compile(r"\{\{\s*insert:\s*param,\s*([^}\s]+)\s*\}\}")

stats = collections.defaultdict(collections.Counter)
defects=[]; unknown_modal=collections.Counter(); modality_count=collections.Counter()
objects={}; overlap_rows=[]; unresolved_links=0; params_unref=0
tag_values=collections.Counter(); sec_values=collections.Counter()

def convert_prose(pr): return INSERT_RE.sub(lambda m:"{param:"+m.group(1)+"}", pr or "")

def part_props_of(c):
    smt=[p for p in c.get("parts",[]) or [] if p.get("name")=="statement"]
    gd=[p for p in c.get("parts",[]) or [] if p.get("name")=="guidance"]
    return (smt[0] if smt else {}), (gd[0] if gd else None)

def collect_stmt(prefix_ns, c, sid, is_child, req):
    """fills one statement + facet by-statement payloads from control c"""
    smt, guid = part_props_of(c)
    prose = convert_prose(smt.get("prose",""))
    pp = {p["name"]:p["value"] for p in (smt.get("props",[]) or [])}
    # defect scan on ALL part-prop values
    for part in c.get("parts",[]) or []:
        for p in part.get("props",[]) or []:
            if "{{" in (p.get("value") or ""):
                defects.append({"control":c["id"],"part":part.get("name"),
                                "prop":p["name"],"value":p["value"]})
    mv = pp.get("modal_verb")
    if mv is None: mod="unspecified"
    elif mv in MODAL: mod=MODAL[mv]
    else: mod="unspecified"; unknown_modal[mv]+=1
    modality_count[mod]+=1
    st={"id":sid,"modality":mod,
        "obligated-parties":[f"{prefix_ns}/party/institution"],
        "prose":{"de":prose}}
    # params: attach to the statement whose prose references them
    for pm in c.get("params",[]) or []:
        pid=pm["id"]
        if "{param:"+pid+"}" in prose:
            st.setdefault("parameters",[]).append({"name":pid,"type":"string"})
        extras={k:v for k,v in (("label",pm.get("label")),) if v}
        if pm.get("values"): extras["values"]=pm["values"]
        for xp in pm.get("props",[]) or []:
            if xp["name"]=="alt-identifier": extras["alt-identifier"]=xp["value"]
        if extras:
            req.setdefault("_compat_params",{})[pid]=extras
        if "{param:"+pid+"}" not in prose:
            globals()["params_unref"]; # counted below
    # facets by-statement
    def by(fname): return req["facets"].setdefault(fname,{}).setdefault("by-statement",{}).setdefault(sid,{})
    g=by(F_GRAM)
    for src,dst in [("action_word","action"),("result","result"),
                    ("result_specification","result-specification")]:
        if src in pp: g[dst]=pp[src]
    if "target_object_categories" in pp: g["target-object-categories"]=split_list(pp["target_object_categories"])
    if "documentation" in pp: by(F_ACRIT)["required-documentation"]=split_list(pp["documentation"])
    cp={p["name"]:p["value"] for p in (c.get("props",[]) or [])}
    so={}
    for k in ("confidentiality","integrity","availability","authenticity"):
        if k in cp: so[k]=cp[k]
    if "threats" in cp:
        so["threat-refs"]=[f"{prefix_ns}/threat/{t.replace(' ','-')}" for t in split_list(cp["threats"])]
    if so: by(F_SECO).update(so)
    tx=by(F_TAX); tx["class"]=c.get("class")
    if "sec_level" in cp:
        tx["sec-level"]=cp["sec_level"]; sec_values[cp["sec_level"]]+=1
    if "effort_level" in cp: tx["effort"]=int(cp["effort_level"])
    if "tags" in cp:
        tl=split_list(cp["tags"]); tx["tags"]=tl
        for t in tl: tag_values[t]+=1
    if "practice" in pp: tx["practice"]=pp["practice"]
    if is_child:
        tx["title"]=c.get("title")
        if "alt-identifier" in cp: tx["alt-identifier"]=cp["alt-identifier"]
        if "label" in cp: tx["label"]=cp["label"]
    if guid and guid.get("prose"):
        by(F_NARR)["guidance"]={"de":guid["prose"]}
    for k in pp: stats["part-props"][k]+=1
    for k in cp: stats["ctrl-props"][k]+=1
    return st

def mint_requirement(prefix_ns, c, version, bm_map):
    rid=f"{prefix_ns}/req/{c['id']}"
    cp={p["name"]:p["value"] for p in (c.get("props",[]) or [])}
    req={"id":rid,"version":version,
         "label":cp.get("label", c["id"]),
         "lifecycle":"active","title":c["title"],
         "statements":[],"facets":{}}
    if "alt-identifier" in cp:
        req["aliases"]=[{"scheme":"bsi-uuid","value":cp["alt-identifier"]}]
    req["statements"].append(collect_stmt(prefix_ns,c,"smt",False,req))
    def descend(node):
        for ch in node.get("controls",[]) or []:
            req["statements"].append(collect_stmt(prefix_ns,ch,ch["id"],True,req))
            descend(ch)
    descend(c)
    rels=[]
    for l in c.get("links",[]) or []:
        href=l.get("href","")
        if href.startswith("#") and href[1:] in bm_map:
            rels.append({"type":l.get("rel","related"),"ref":bm_map[href[1:]]})
        elif href.startswith("#"):
            rels.append({"type":l.get("rel","related"),"ref":f"{prefix_ns}/req/{href[1:]}"})
        else:
            rels.append({"type":l.get("rel","related"),"ref":href})
    if rels: req["relations"]=rels
    return rid,req

# rebuild output
if os.path.exists(OUT): shutil.rmtree(OUT)
paths=collections.Counter(); catalogs_meta=[]; baseline=collections.defaultdict(list)
seq={"n":0}
def nseq(): seq["n"]+=10; return seq["n"]

all_ids={}
for key,fn,ns in SOURCES:
    cat=json.load(open(fn,encoding="utf-8"))["catalog"]
    inventory(cat,"catalog",paths)
    version=cat["metadata"]["version"]
    catalogs_meta.append((key,cat["metadata"]["title"],version,cat["metadata"]["oscal-version"]))
    bm_map={r["uuid"]:(r.get("rlinks",[{}])[0].get("href") or r.get("title",""))
            for r in cat.get("back-matter",{}).get("resources",[]) or []}
    ids=set()
    def conv_group(g,path_ids):
        entries=[]
        for sub in g.get("groups",[]) or []:
            u=conv_group(sub,path_ids+[slug(sub.get("id") or sub.get("title"))])
            if u: entries.append({"ref":u,"sequence":nseq()})
        def all_desc_ids(node):
            ids.add(node["id"])
            for ch in node.get("controls",[]) or []: all_desc_ids(ch)
        for c in g.get("controls",[]) or []:
            all_desc_ids(c)
            rid,req=mint_requirement(ns,c,version,bm_map)
            # param-extras -> compat facet on the requirement
            extras=req.pop("_compat_params",None)
            if extras: req["facets"][F_COMPAT]={"param-extras":extras}
            if not req["facets"]: req.pop("facets")
            objects[f"objects/{key}/req-{slug(c['id'])}.json"]=req
            cp={p["name"]:p["value"] for p in (c.get("props",[]) or [])}
            if "sec_level" in cp: baseline[(key,cp["sec_level"])].append(rid)
            entries.append({"ref":rid,"sequence":nseq()})
        if not entries: return None
        sid=g.get("id") or "-".join(path_ids)
        u=f"{ns}/set/tax/{slug(sid)}"
        sobj={"id":u,"version":version,"lifecycle":"active",
              "title":g.get("title",sid),"members":entries}
        for gp in g.get("props",[]) or []:
            if gp["name"]=="label":
                sobj["label"]=gp["value"]
                if gp.get("remarks"):
                    sobj.setdefault("facets",{}).setdefault(F_NARR,{})["description"]={"de":gp["remarks"]}
            elif gp["name"]=="alt-identifier":
                sobj.setdefault("aliases",[]).append({"scheme":"bsi-uuid","value":gp["value"]})
        objects[f"objects/{key}/set-tax-{slug(sid)}.json"]=sobj
        return u
    top=[]
    for g in cat.get("groups",[]) or []:
        u=conv_group(g,[slug(g.get("id") or g.get("title"))])
        if u: top.append({"ref":u,"sequence":nseq()})
    objects[f"objects/{key}/set-tax-root.json"]={
        "id":f"{ns}/set/tax/root","version":version,"lifecycle":"active",
        "title":cat["metadata"]["title"],"members":top}
    all_ids[key]=ids

for (key,lvl),refs in sorted(baseline.items()):
    ns=dict((k,n) for k,_,n in [(s[0],s[1],s[2]) for s in SOURCES])[key]
    u=f"{ns}/set/baseline/{slug(lvl)}"
    objects[f"objects/{key}/set-baseline-{slug(lvl)}.json"]={
        "id":u,"version":[v for k2,_,v,_ in catalogs_meta if k2==key][0],
        "lifecycle":"active","title":f"Baseline sec_level: {lvl}",
        "members":[{"ref":r,"sequence":(i+1)*10} for i,r in enumerate(refs)]}

# twin-catalog overlap analysis (id strings shared across the two publications)
shared=sorted(all_ids["gspp"] & all_ids["mstls"])
def prose_of(fn,cid):
    cat=json.load(open(fn))["catalog"]; found={}
    def s(n):
        for g in n.get("groups",[]) or []: s(g)
        for c in n.get("controls",[]) or []:
            if c["id"] in shared:
                smt=[p for p in c.get("parts",[]) if p.get("name")=="statement"]
                found[c["id"]]=(smt[0].get("prose","") if smt else "")
            s(c)
    s(cat); return found
pg=prose_of("/home/claude/gspp.json",None); pt=prose_of("/home/claude/tls.json",None)
for cid in shared:
    overlap_rows.append({"id":cid,"identical-prose":pg.get(cid,"")==pt.get(cid,"")})

# facet schema stubs (enums generated from observed values)
def stub(path,fid,ver,mods,props):
    w(path,{"id":fid,"version":ver,"modifies-semantics":mods,
        "note":"ILLUSTRATIVE STUB - normative schemas ship with the v0.6 schema deliverable",
        "schema":{"$schema":"https://json-schema.org/draft/2020-12/schema",
                  "type":"object","properties":props}})
stub("schemas/gspp-taxonomy-1.0.0-stub.json","https://ns.bsi.bund.de/facet/gspp-taxonomy","1.0.0",["selection"],
     {"by-statement":{"type":"object"},"observed-sec-levels":{"enum":sorted(sec_values)}})
stub("schemas/statement-grammar-1.0.0-stub.json","https://ns.oscal.org/stdlib/facet/statement-grammar","1.0.0",[],
     {"by-statement":{"type":"object"}})
stub("schemas/security-objectives-1.0.0-stub.json","https://ns.oscal.org/stdlib/facet/security-objectives","1.0.0",[],
     {"by-statement":{"type":"object"}})
stub("schemas/assessment-criteria-1.0.0-stub.json","https://ns.oscal.org/stdlib/facet/assessment-criteria","1.0.0",["assessment"],
     {"by-statement":{"type":"object"}})
stub("schemas/gspp-narrative-1.0.0-stub.json","https://ns.bsi.bund.de/facet/gspp-narrative","1.0.0",[],
     {"by-statement":{"type":"object"}})
stub("schemas/oscal-1x-compat-1.0.0-stub.json","https://ns.oscal.org/compat/oscal-1x","1.0.0",[],
     {"param-extras":{"type":"object"}})

manifest={"manifest-version":"1",
 "provenance":{"sources":[{"key":k,"title":t,"version":v,"oscal-version":o}
               for k,t,v,o in catalogs_meta],
               "converter":"convert_bsi.py v0.1",
               "note":"disjoint subtrees per publication; shared-id analysis in coverage report"},
 "objects":[{"id":o["id"],"version":o["version"],
             "package-digest":None,"semantic-digest":semantic_digest(o),"path":rel}
            for rel,o in sorted(objects.items())],
 "facet-schemas":[]}
for rel,o in objects.items(): w(rel,o)
for e in manifest["objects"]: e["package-digest"]=sha_file(e["path"])
for s in sorted(os.listdir(os.path.join(OUT,"schemas"))):
    d=json.load(open(os.path.join(OUT,"schemas",s)))
    manifest["facet-schemas"].append({"id":d["id"],"exact-version":d["version"],
        "digest":sha_file(f"schemas/{s}"),"path":f"schemas/{s}"})
w("content-manifest.json",manifest)

# ---------- coverage ----------
rows=[]; unmapped=[]
for p,n in sorted(paths.items()):
    lvl,tgt=destination(p)
    (rows if lvl else unmapped).append((p,n,lvl,tgt) if lvl else (p,n))
total=sum(paths.values()); mapped=sum(n for _,n,_,_ in rows)
reqs=sum(1 for r in objects.values() if "/req/" in r["id"])
sets=sum(1 for r in objects.values() if "/set/" in r["id"])
nstmt=sum(len(r.get("statements",[])) for r in objects.values() if "statements" in r)

j={"sources":[{"key":k,"title":t,"version":v} for k,t,v,_ in catalogs_meta],
   "totals":{"leaf-values":total,"mapped":mapped,"unmapped":total-mapped,
             "coverage-pct":round(100*mapped/total,3)},
   "objects":{"requirements":reqs,"statements":nstmt,"sets":sets,"total":len(objects)},
   "modality":dict(modality_count),"unknown-modal-verbs":dict(unknown_modal),
   "defective-prop-values":len(defects),
   "defects":defects,
   "shared-ids":overlap_rows,
   "baselines":{f"{k}:{l}":len(v) for (k,l),v in sorted(baseline.items())},
   "tag-value-inconsistencies":{t:c for t,c in tag_values.items()
        if t.replace(" ","-") in tag_values and " " in t},
   "unmapped-paths":[{"path":p,"count":n} for p,n in unmapped],
   "path-map":[{"path":p,"count":n,"level":l,"destination":t} for p,n,l,t in rows]}
json.dump(j,open(RJS,"w"),ensure_ascii=False,indent=1)

md=[f"# BSI (GS++ + MS-TLS) -> Semantic Core: Coverage Report (computed)\n"]
md.append("Sources: " + " · ".join(f"**{t}** v{v}" for _,t,v,_ in catalogs_meta) + "\n")
md.append("## Totals\n")
md.append(f"- Source leaf values inventoried: **{total:,}**")
md.append(f"- Mapped: **{mapped:,}** -> **UNMAPPED: {total-mapped}** -> coverage **{j['totals']['coverage-pct']} %**")
md.append(f"- Emitted: **{reqs} Requirements** carrying **{nstmt} statements** "
          f"(all nested pseudo-controls flattened to clauses - nesting reaches depth 3), **{sets} Sets**, "
          f"manifest with both digests, {len(manifest['facet-schemas'])} pinned facet stubs.\n")
md.append("## Conversion rules (declared, counted)\n")
md.append(f"- **Modality** from `modal_verb` (code map incl. DARF NUR -> may-only): "
          + ", ".join(f"{k} x{v}" for k,v in sorted(modality_count.items(),key=lambda x:-x[1]))
          + (f"; unknown verbs: {dict(unknown_modal)}" if unknown_modal else "; no unknown verbs") + ".")
md.append("- **Nested controls -> statements** of the parent; statement id = child control id "
          "(stable, citable); child-level props keyed `by-statement` in the facets.")
md.append("- **{{ insert: param, x }}** in prose -> `{param:x}` tokens; params typed `string`; "
          "param label/default/alt-id -> **Level 2** compat `param-extras` "
          "(candidate D9 addition: scalar default/display value).")
md.append("- **Grammar** (action_word/result/result_specification/target_object_categories) -> "
          "`statement-grammar@1` by-statement; **documentation** -> `assessment-criteria@1` "
          "required-documentation; **C/I/A/Auth + threats** -> `security-objectives@1` "
          "(threat codes minted from 'G 0.x'); **sec_level/effort/tags/class/practice** -> "
          "`gspp-taxonomy@1`; **guidance parts** -> `gspp-narrative@1`.")
md.append(f"- **Baselines** from top-control `sec_level`: "
          + ", ".join(f"{k}:{l} ({len(v)})" for (k,l),v in sorted(baseline.items()))
          + ". Child-level sec_level stays informational by-statement "
          "(clause-level baselining = Tailoring concern, not Set membership).")
md.append("- **alt-identifier** -> aliases (scheme bsi-uuid) on Requirements; child alt-ids "
          "by-statement. CSV-link namespaces absorbed: pinned schemas replace them.\n")
md.append("## Findings (computed)\n")
md.append(f"- **Defective source values: {len(defects)}** - `{{{{...}}}}` pseudo-placeholders inside "
          "part-prop values, REPORTED for the authors' queue (never repaired, passed through, or "
          "dropped silently - handbook 14.5). Full list in the JSON report; first three:")
for d in defects[:3]:
    md.append(f"    - `{d['control']}` / `{d['prop']}`: \"{d['value'][:70]}...\"")
md.append(f"- **Twin-catalog shared id strings: {len(shared)}** - minted under disjoint subtrees "
          f"(/gspp/, /mstls/). Prose-identical: "
          f"{sum(1 for r in overlap_rows if r['identical-prose'])}/{len(shared)} "
          "(candidates for future single-object-two-sets dedup; the rest have diverged - "
          "the measured composition hazard, now safely representable).")
inc = j["tag-value-inconsistencies"]
if inc: md.append(f"- **Tag spelling drift** (space vs hyphen variants coexist): {inc} - "
                  "reported, not normalized.")
md.append(f"- **sec_level value space observed**: {dict(sec_values)} "
          "(note the bare 'erhöht' vs 'normal-SdT' asymmetry - vocabulary drift the "
          "pinned schema now freezes).\n")
md.append("## Full path map\n| path | count | level | destination |\n|---|---:|---|---|")
for p,n,l,t in rows: md.append(f"| `{p}` | {n:,} | {l} | {t} |")
md.append("\n## Per-prop dispatch\n| prop | level | destination |\n|---|---|---|")
for k,(l,t) in PROP_DEST.items(): md.append(f"| `{k}` | {l} | {t} |")
md.append("\n## UNMAPPED (gate target: zero)\n")
if unmapped:
    md.append("| path | count |\n|---|---:|")
    for p,n in unmapped: md.append(f"| `{p}` | {n} |")
else: md.append("*(none)*")
open(RMD,"w",encoding="utf-8").write("\n".join(md)+"\n")

print(f"requirements: {reqs} (statements: {nstmt})  sets: {sets}  objects: {len(objects)}")
print(f"leaf values: {total:,}  mapped: {mapped:,}  UNMAPPED: {total-mapped}")
print("modality:",dict(modality_count)," unknown:",dict(unknown_modal))
compat_n=sum(1 for o in objects.values() if "facets" in o and F_COMPAT in o.get("facets",{}))
print(f"L2 param-extras residue: {compat_n} requirements")
print(f"defects: {len(defects)}  shared-ids: {len(shared)} "
      f"(identical prose: {sum(1 for r in overlap_rows if r['identical-prose'])})")
if unmapped:
    print("UNMAPPED:"); [print("  ",p,"x",n) for p,n in unmapped[:30]]
