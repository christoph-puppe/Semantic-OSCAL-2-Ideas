# C3A -> Semantic Core: Coverage Report (computed)

Source: **BSI C3A Criteria enabling Cloud Computing Autonomy** v1.0 (OSCAL 1.2.2, published 2026-05-03) - GS++ grammar family.

## Totals

- Source leaf values inventoried: **1,093**
- Mapped (declared destination): **1,093**
- **UNMAPPED: 0**  ->  coverage **100.0 %**
- Objects emitted: **30 Requirements** carrying **30 typed parameters**, **9 Sets**, manifest with both digests.

## Conversion rules (declared, counted)

- **Modality from `modal_verb` code map** (GS++ Verbindlichkeitssprache): must x30.
- **Parameters carry first-class `label` + `default`** (D9 rev, backlog #1) - the x30 params land with labels ('Normreferenzen') and default values in the kernel; the param-extras residue class never opens for this corpus (only the parameter alt-identifier uuids wait there, x30 objects).
- **Grammar props -> statement-grammar@1** by-statement (action-word/result); sec_level -> baseline Set (normal-SdT (30)); effort_level/tags -> c3a/taxonomy@1; alt-identifier -> aliases (scheme bsi-uuid); CSV-link prop namespaces absorbed - pinned stubs replace them (the GS++ lesson).
- **Obligated party**: documented default https://ns.bsi.bund.de/c3a/party/cloud-dienstanbieter.
- **Payload free text language-tagged** per corpus language ({de: ...}): guidance x15. Harmonized from the start (backlog #12).

## Findings (computed)

- **Fused class variants x10**: statement prose interleaves 'C1: ... C2: ...' cloud-class variants inside ONE statement string (['SOV-1-01', 'SOV-1-02', 'SOV-1-03', 'SOV-2-02', 'SOV-2-03', 'SOV-3-01', 'SOV-4-01', 'SOV-4-02', 'SOV-4-04', 'SOV-5-05']) - the CR26 varies_by_class need, encoded as prose fusion; candidate for statement split or class Tailorings at source. REPORTED.
- **Multiple modal_verb props on one statement x0**: [] - a statement carrying two binding strengths is the fusion's machine-readable shadow; converter takes the first, declared. REPORTED.
- **Multi-value params x0** (none) - first value becomes `default`, rest would need `choice`; counted.

## Full path map (every source path, its count, its destination)

| path | count | level | destination |
|---|---:|---|---|
| `c3a.catalog.groups[].controls[].class` | 30 | L1 | Requirement id (URI mint) + title; class -> category Set |
| `c3a.catalog.groups[].controls[].id` | 30 | L1 | Requirement id (URI mint) + title; class -> category Set |
| `c3a.catalog.groups[].controls[].params[].id` | 30 | L1 | parameter {name, type string, label, default} - D9-rev first-class label/default (no param-extras residue) |
| `c3a.catalog.groups[].controls[].params[].label` | 30 | L1 | parameter {name, type string, label, default} - D9-rev first-class label/default (no param-extras residue) |
| `c3a.catalog.groups[].controls[].params[].props[].name` | 30 | L2 | compat param-extras: parameter alt-identifier uuid (no kernel home on parameters; declared waiting room) |
| `c3a.catalog.groups[].controls[].params[].props[].ns` | 30 | L2 | compat param-extras: parameter alt-identifier uuid (no kernel home on parameters; declared waiting room) |
| `c3a.catalog.groups[].controls[].params[].props[].value` | 30 | L2 | compat param-extras: parameter alt-identifier uuid (no kernel home on parameters; declared waiting room) |
| `c3a.catalog.groups[].controls[].params[].values[]` | 30 | L1 | parameter {name, type string, label, default} - D9-rev first-class label/default (no param-extras residue) |
| `c3a.catalog.groups[].controls[].parts[].id` | 45 | L1 | statement -> statements[0]; guidance -> narrative@1 |
| `c3a.catalog.groups[].controls[].parts[].name` | 45 | L1 | statement -> statements[0]; guidance -> narrative@1 |
| `c3a.catalog.groups[].controls[].parts[].props[].name` | 98 | L1 | grammar props (modal_verb -> statements[0].modality via code map; action_word/result -> statement-grammar@1 by-statement) |
| `c3a.catalog.groups[].controls[].parts[].props[].ns` | 98 | L1 | grammar props (modal_verb -> statements[0].modality via code map; action_word/result -> statement-grammar@1 by-statement) |
| `c3a.catalog.groups[].controls[].parts[].props[].value` | 98 | L1 | grammar props (modal_verb -> statements[0].modality via code map; action_word/result -> statement-grammar@1 by-statement) |
| `c3a.catalog.groups[].controls[].parts[].prose` | 45 | L1 | statements[0].prose.de | narrative guidance (language-tagged) |
| `c3a.catalog.groups[].controls[].props[].name` | 120 | L1 | dispatch: alt-identifier -> aliases (scheme bsi-uuid); sec_level -> baseline Set; effort_level/tags -> taxonomy@1; CSV-link namespaces absorbed (pinned stubs replace them) |
| `c3a.catalog.groups[].controls[].props[].ns` | 120 | L1 | dispatch: alt-identifier -> aliases (scheme bsi-uuid); sec_level -> baseline Set; effort_level/tags -> taxonomy@1; CSV-link namespaces absorbed (pinned stubs replace them) |
| `c3a.catalog.groups[].controls[].props[].value` | 120 | L1 | dispatch: alt-identifier -> aliases (scheme bsi-uuid); sec_level -> baseline Set; effort_level/tags -> taxonomy@1; CSV-link namespaces absorbed (pinned stubs replace them) |
| `c3a.catalog.groups[].controls[].title` | 30 | L1 | Requirement id (URI mint) + title; class -> category Set |
| `c3a.catalog.groups[].id` | 6 | L1 | domain Set id/title |
| `c3a.catalog.groups[].title` | 6 | L1 | domain Set id/title |
| `c3a.catalog.metadata.last-modified` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.oscal-version` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].addresses[].addr-lines[]` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].addresses[].city` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].addresses[].country` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].addresses[].postal-code` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].links[].href` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].links[].rel` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].name` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].short-name` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].type` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.parties[].uuid` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.props[].name` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.props[].value` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.published` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.responsible-parties[].party-uuids[]` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.responsible-parties[].role-id` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.roles[].id` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.roles[].title` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.title` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.metadata.version` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |
| `c3a.catalog.uuid` | 1 | L1 | bundle manifest / L0 provenance (roles/parties -> publisher identity) |

## UNMAPPED (gate target: zero)

*(none)*
