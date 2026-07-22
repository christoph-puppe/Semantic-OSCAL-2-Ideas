# BSI (GS++ + MS-TLS) -> Semantic Core: Coverage Report (computed)

Sources: **Anwenderkatalog Grundschutz++** v2026-07-03T09:11:21.450351+00:00 · **Entwurf Mindeststandard Bund TLS** v2026-04-23T13:28:32.097584+00:00

## Totals

- Source leaf values inventoried: **49,804**
- Mapped: **49,804** -> **UNMAPPED: 0** -> coverage **100.0 %**
- Emitted: **658 Requirements** carrying **1015 statements** (all nested pseudo-controls flattened to clauses - nesting reaches depth 3), **167 Sets**, manifest with both digests, 6 pinned facet stubs.

## Conversion rules (declared, counted)

- **Modality** from `modal_verb` (code map incl. DARF NUR -> may-only): should x626, may x225, must x155, unspecified x9; no unknown verbs.
- **Nested controls -> statements** of the parent; statement id = child control id (stable, citable); child-level props keyed `by-statement` in the facets.
- **{{ insert: param, x }}** in prose -> `{param:x}` tokens; params typed `string`; param label/default/alt-id -> **Level 2** compat `param-extras` (candidate D9 addition: scalar default/display value).
- **Grammar** (action_word/result/result_specification/target_object_categories) -> `statement-grammar@1` by-statement; **documentation** -> `assessment-criteria@1` required-documentation; **C/I/A/Auth + threats** -> `security-objectives@1` (threat codes minted from 'G 0.x'); **sec_level/effort/tags/class/practice** -> `gspp-taxonomy@1`; **guidance parts** -> `gspp-narrative@1`.
- **Baselines** from top-control `sec_level`: gspp:erhöht (134), gspp:normal-SdT (517), mstls:normal-SdT (7). Child-level sec_level stays informational by-statement (clause-level baselining = Tailoring concern, not Set membership).
- **alt-identifier** -> aliases (scheme bsi-uuid) on Requirements; child alt-ids by-statement. CSV-link namespaces absorbed: pinned schemas replace them.

## Findings (computed)

- **Defective source values: 216** - `{{...}}` pseudo-placeholders inside part-prop values, REPORTED for the authors' queue (never repaired, passed through, or dropped silently - handbook 14.5). Full list in the JSON report; first three:
    - `GC.1.1` / `result_specification`: "nach {{einem anerkannten Standard}}..."
    - `GC.9.1.1` / `result`: "die {{Rollen und Zuständigkeiten}} im Rahmen des ISMS..."
    - `GC.9.1.1.1` / `result`: "die Zuständigkeit für Informationssicherheit {{einer unabhängigen Pers..."
- **Twin-catalog shared id strings: 11** - minted under disjoint subtrees (/gspp/, /mstls/). Prose-identical: 1/11 (candidates for future single-object-two-sets dedup; the rest have diverged - the measured composition hazard, now safely representable).
- **Tag spelling drift** (space vs hyphen variants coexist): {'Compliance Management': 6} - reported, not normalized.
- **sec_level value space observed**: {'normal-SdT': 779, 'erhöht': 227} (note the bare 'erhöht' vs 'normal-SdT' asymmetry - vocabulary drift the pinned schema now freezes).

## Full path map
| path | count | level | destination |
|---|---:|---|---|
| `catalog.back-matter.resources[].rlinks[].hashes[].algorithm` | 2 | L1 | source-document reference (title/rlink) -> resolved into relations / dropped-declared |
| `catalog.back-matter.resources[].rlinks[].hashes[].value` | 2 | L1 | source-document reference (title/rlink) -> resolved into relations / dropped-declared |
| `catalog.back-matter.resources[].rlinks[].href` | 2 | L1 | source-document reference (title/rlink) -> resolved into relations / dropped-declared |
| `catalog.back-matter.resources[].title` | 2 | L1 | source-document reference (title/rlink) -> resolved into relations / dropped-declared |
| `catalog.back-matter.resources[].uuid` | 2 | L1 | resolution key for #uuid links -> external URL |
| `catalog.groups[].controls[].class` | 7 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].controls[].controls[].class` | 6 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].controls[].controls[].controls[].class` | 4 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].controls[].controls[].controls[].id` | 4 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].controls[].controls[].controls[].parts[].name` | 4 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].controls[].controls[].controls[].parts[].prose` | 4 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].controls[].controls[].controls[].props[].name` | 8 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].controls[].controls[].props[].value` | 8 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].controls[].controls[].title` | 4 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].controls[].controls[].id` | 6 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].controls[].controls[].parts[].id` | 2 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].controls[].controls[].parts[].name` | 7 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].controls[].controls[].parts[].props[].name` | 7 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].controls[].controls[].parts[].props[].ns` | 7 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].controls[].controls[].parts[].props[].value` | 7 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].controls[].controls[].parts[].prose` | 7 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].controls[].controls[].props[].name` | 15 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].controls[].props[].ns` | 3 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].controls[].controls[].props[].value` | 15 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].controls[].title` | 6 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].controls[].id` | 7 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].controls[].links[].href` | 1 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].controls[].links[].rel` | 1 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].controls[].params[].id` | 3 | L1 | statement parameter name (type string) |
| `catalog.groups[].controls[].params[].label` | 3 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].controls[].params[].props[].name` | 3 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].controls[].params[].props[].value` | 3 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].controls[].params[].values[]` | 1 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].controls[].parts[].id` | 14 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].controls[].parts[].name` | 14 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].controls[].parts[].props[].name` | 45 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].controls[].parts[].props[].ns` | 45 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].controls[].parts[].props[].value` | 45 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].controls[].parts[].prose` | 14 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].controls[].props[].name` | 33 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].props[].ns` | 19 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].controls[].props[].value` | 33 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].controls[].title` | 7 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].groups[].controls[].class` | 651 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].groups[].controls[].controls[].class` | 326 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].groups[].controls[].controls[].controls[].class` | 19 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].class` | 2 | L1 | gspp-taxonomy: class (by-statement) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].id` | 2 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].id` | 4 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].name` | 4 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].props[].name` | 7 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].props[].ns` | 7 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].props[].value` | 7 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].parts[].prose` | 4 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].props[].name` | 6 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].props[].ns` | 4 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].props[].value` | 6 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].controls[].controls[].title` | 2 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].groups[].controls[].controls[].controls[].id` | 19 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].groups[].controls[].controls[].controls[].links[].href` | 8 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].controls[].controls[].links[].rel` | 8 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].controls[].controls[].params[].id` | 4 | L1 | statement parameter name (type string) |
| `catalog.groups[].groups[].controls[].controls[].controls[].params[].label` | 4 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].groups[].controls[].controls[].controls[].params[].props[].name` | 4 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].controls[].controls[].params[].props[].value` | 4 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].id` | 37 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].name` | 37 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].props[].name` | 95 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].props[].ns` | 95 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].props[].value` | 95 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].controls[].parts[].prose` | 37 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].groups[].controls[].controls[].controls[].props[].name` | 131 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].controls[].props[].ns` | 112 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].controls[].props[].value` | 131 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].controls[].title` | 19 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].groups[].controls[].controls[].id` | 326 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].groups[].controls[].controls[].links[].href` | 66 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].controls[].links[].rel` | 66 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].controls[].params[].id` | 73 | L1 | statement parameter name (type string) |
| `catalog.groups[].groups[].controls[].controls[].params[].label` | 73 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].groups[].controls[].controls[].params[].props[].name` | 73 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].controls[].params[].props[].value` | 73 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].controls[].params[].values[]` | 1 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].groups[].controls[].controls[].parts[].id` | 651 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].parts[].name` | 651 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].controls[].parts[].props[].name` | 1,622 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].parts[].props[].ns` | 1,622 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].parts[].props[].value` | 1,622 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].controls[].parts[].prose` | 651 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].groups[].controls[].controls[].props[].name` | 2,579 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].props[].ns` | 2,253 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].controls[].props[].value` | 2,579 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].controls[].title` | 326 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].groups[].controls[].id` | 651 | L1 | Requirement id (top) / statement id (nested) |
| `catalog.groups[].groups[].controls[].links[].href` | 189 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].links[].rel` | 189 | L1 | relations[] {type=rel, ref} (#control -> req URI; #uuid -> back-matter URL) |
| `catalog.groups[].groups[].controls[].params[].id` | 144 | L1 | statement parameter name (type string) |
| `catalog.groups[].groups[].controls[].params[].label` | 144 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].groups[].controls[].params[].props[].name` | 144 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].params[].props[].value` | 144 | L2 | compat oscal-1x: param-extras (param alt-identifier) |
| `catalog.groups[].groups[].controls[].params[].values[]` | 1 | L2 | compat oscal-1x: param-extras (default/display value - candidate D9 addition) |
| `catalog.groups[].groups[].controls[].parts[].id` | 1,302 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].parts[].name` | 1,302 | L1 | statement/guidance part identity -> statement id / narrative key |
| `catalog.groups[].groups[].controls[].parts[].props[].name` | 3,303 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].parts[].props[].ns` | 3,303 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].parts[].props[].value` | 3,303 | L1 | dispatch by part-prop name (grammar/objectives/criteria; defects reported) |
| `catalog.groups[].groups[].controls[].parts[].prose` | 1,302 | L1 | statements[].prose.de ({{insert}} -> {param:}) / gspp-narrative guidance |
| `catalog.groups[].groups[].controls[].props[].name` | 5,240 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].props[].ns` | 4,589 | L1 | absorbed: CSV-link namespaces replaced by pinned facet schemas |
| `catalog.groups[].groups[].controls[].props[].value` | 5,240 | L1 | dispatch by prop name (see per-prop table) |
| `catalog.groups[].groups[].controls[].title` | 651 | L1 | Requirement title (top) / kept in taxonomy by-statement (nested) |
| `catalog.groups[].groups[].id` | 139 | L1 | taxonomy Set id/title (per-catalog subtree) |
| `catalog.groups[].groups[].props[].name` | 278 | L1 | Set.label / Set.aliases (bsi-uuid) |
| `catalog.groups[].groups[].props[].value` | 278 | L1 | Set.label / Set.aliases (bsi-uuid) |
| `catalog.groups[].groups[].title` | 139 | L1 | taxonomy Set id/title (per-catalog subtree) |
| `catalog.groups[].id` | 23 | L1 | taxonomy Set id/title (per-catalog subtree) |
| `catalog.groups[].props[].name` | 43 | L1 | Set.label / Set.aliases (bsi-uuid) |
| `catalog.groups[].props[].remarks` | 20 | L1 | gspp-narrative on the Set: layer/Praktik description |
| `catalog.groups[].props[].value` | 43 | L1 | Set.label / Set.aliases (bsi-uuid) |
| `catalog.groups[].title` | 23 | L1 | taxonomy Set id/title (per-catalog subtree) |
| `catalog.metadata.last-modified` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.links[].href` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.links[].rel` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.links[].text` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.oscal-version` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.parties[].email-addresses[]` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.parties[].name` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.parties[].type` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.parties[].uuid` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.props[].name` | 5 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.props[].ns` | 3 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.props[].value` | 5 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.remarks` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.responsible-parties[].party-uuids[]` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.responsible-parties[].role-id` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.roles[].id` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.roles[].title` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.title` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.metadata.version` | 2 | L1 | bundle manifest / L0 provenance |
| `catalog.uuid` | 2 | L1 | bundle manifest / L0 provenance |

## Per-prop dispatch
| prop | level | destination |
|---|---|---|
| `alt-identifier` | L1 | Requirement.aliases (top) / taxonomy by-statement (nested) |
| `label` | L1 | Requirement.label (top) / taxonomy by-statement label (nested) |
| `sec_level` | L1 | top: baseline Set membership; nested: taxonomy by-statement |
| `effort_level` | L1 | gspp-taxonomy: effort (by-statement) |
| `tags` | L1 | gspp-taxonomy: tags[] (comma-split; inconsistencies reported) |
| `confidentiality` | L1 | security-objectives (by-statement) |
| `integrity` | L1 | security-objectives (by-statement) |
| `availability` | L1 | security-objectives (by-statement) |
| `authenticity` | L1 | security-objectives (by-statement) |
| `threats` | L1 | security-objectives threat-refs[] (comma-split, minted threat code URIs) |
| `modal_verb` | L1 | statements[].modality (mapped code system) |
| `action_word` | L1 | statement-grammar: action (by-statement) |
| `result` | L1 | statement-grammar: result (by-statement) |
| `result_specification` | L1 | statement-grammar: result-specification (by-statement) |
| `target_object_categories` | L1 | statement-grammar: target-object-categories[] (by-statement) |
| `documentation` | L1 | assessment-criteria: required-documentation[] (by-statement) |
| `practice` | L1 | gspp-taxonomy: practice (by-statement) |

## UNMAPPED (gate target: zero)

*(none)*
