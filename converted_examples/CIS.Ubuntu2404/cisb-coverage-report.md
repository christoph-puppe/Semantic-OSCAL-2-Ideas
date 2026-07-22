# CIS Ubuntu 24.04 Benchmark -> Semantic Core: Coverage Report (computed)

Source: **CIS Ubuntu Linux 24.04 LTS Benchmark** v1.0.0 (OSCAL 1.1.3) - 312 hardening rules, 116 back-matter resources.

## Totals

- Source leaf values inventoried: **20,698**
- Mapped (declared destination): **20,698**
- **UNMAPPED: 0**  ->  coverage **100.0 %**
- Objects emitted: **312 Requirements**, **635 Mapping objects**, **79 Sets** (section taxonomy + 4 profile baselines), manifest with both digests.

## Conversion rules (declared, counted)

- **Profile membership recovered from links**: per-rule reference links resolve to back-matter PROFILE resources -> baseline Sets (Level 1 \- Server (251), Level 1 \- Workstation (245), Level 2 \- Server (312), Level 2 \- Workstation (309)) - the ISM applicability pattern, benchmark edition.
- **CIS_Controls cross-references -> 635 Mapping objects** (relationship supports, confidence draft, 8.6 untyped-import rule): v8 targets x323 resolve into the sibling CIS Controls bundle (zero-padded safeguard ids); v7 targets x312 minted under https://ns.cisecurity.org/controls/v7 (no converted corpus yet - declared external).
- **Audit/Remediation -> assessment-criteria@1** (audit script + remediation script, method automated x291/manual x21 from rule markings); Description/Rationale -> narrative@1; References markings -> external-references@1 (citation labels, kept bare by the identifier rule).
- **Statement prose minted from title x312**: every source statement part is empty - the rule title IS the norm ('Ensure ...'); minting is declared, not silent. Modality unspecified x312 (imperative corpus; force rides profile membership).
- **xccdf ids -> aliases** (scheme xccdf) - the benchmark's second identifier scheme, typed.
- **Section narrative** (overview parts x73) -> Level 2 compat facet oscal-1x@1.
- **Obligated party**: documented default https://ns.cisecurity.org/benchmark/ubuntu-24.04-lts/party/system-administrator.
- **Payload free text language-tagged** ({en: ...}): audit x312, description x312, prose x73, rationale x312, remediation x312. Harmonized from the start (backlog #12).

## Findings (computed)

- **Empty statement prose x312 (all rules)**: the CIS OSCAL export carries the norm only in the title; statement parts exist but are empty. REPORTED for the CIS tooling queue; the converter mints prose from the title, declared per rule above.
- **Mixed-version control references**: the benchmark cross-references CIS Controls v7 AND v8 (x312 vs x323) - a live example of why Mapping objects carry explicit versioned targets.
- **Unresolved link targets x0** (counted; kept as references where resolvable).

## Full path map (every source path, its count, its destination)

| path | count | level | destination |
|---|---:|---|---|
| `cisb.catalog.back-matter.resources[].description` | 5 | L1 | resolution table: profiles -> baseline Sets; safeguard resources -> Mapping targets; documents -> reference URLs (descriptions recorded in the table) |
| `cisb.catalog.back-matter.resources[].props[].class` | 154 | L1 | resource kind dispatch: xccdf profile marking | CIS_Controls version + safeguard number | document markings |
| `cisb.catalog.back-matter.resources[].props[].name` | 216 | L1 | resource kind dispatch: xccdf profile marking | CIS_Controls version + safeguard number | document markings |
| `cisb.catalog.back-matter.resources[].props[].value` | 216 | L1 | resource kind dispatch: xccdf profile marking | CIS_Controls version + safeguard number | document markings |
| `cisb.catalog.back-matter.resources[].rlinks[].href` | 186 | L1 | resolution table: profiles -> baseline Sets; safeguard resources -> Mapping targets; documents -> reference URLs (descriptions recorded in the table) |
| `cisb.catalog.back-matter.resources[].title` | 67 | L1 | resolution table: profiles -> baseline Sets; safeguard resources -> Mapping targets; documents -> reference URLs (descriptions recorded in the table) |
| `cisb.catalog.back-matter.resources[].uuid` | 116 | L1 | resolution table: profiles -> baseline Sets; safeguard resources -> Mapping targets; documents -> reference URLs (descriptions recorded in the table) |
| `cisb.catalog.groups[].groups[].groups[].controls[].id` | 142 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].controls[].links[].href` | 540 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].controls[].links[].rel` | 540 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].class` | 833 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].id` | 975 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].links[].href` | 286 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].links[].rel` | 286 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].name` | 975 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].props[].class` | 177 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].props[].name` | 1,152 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].props[].value` | 1,152 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].controls[].parts[].prose` | 568 | L1 | Description/Rationale -> narrative@1; Audit script -> assessment-criteria@1.audit; Remediation -> assessment-criteria@1.remediation (language-tagged) |
| `cisb.catalog.groups[].groups[].groups[].controls[].props[].class` | 142 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].controls[].props[].name` | 426 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].controls[].props[].value` | 426 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].controls[].title` | 142 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].id` | 122 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].links[].href` | 397 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].links[].rel` | 397 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].class` | 724 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].id` | 846 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].links[].href` | 280 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].links[].rel` | 280 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].name` | 846 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].props[].class` | 120 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].props[].name` | 966 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].props[].value` | 966 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].parts[].prose` | 488 | L1 | Description/Rationale -> narrative@1; Audit script -> assessment-criteria@1.audit; Remediation -> assessment-criteria@1.remediation (language-tagged) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].props[].class` | 122 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].props[].name` | 366 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].props[].value` | 366 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].controls[].title` | 122 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].id` | 48 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].links[].href` | 180 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].links[].rel` | 180 | L1 | reference links resolved via back-matter: profile resources -> baseline Set membership (Level 1/2 Server/Workstation); document resources -> relations reference |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].class` | 288 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].id` | 336 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].links[].href` | 102 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].links[].rel` | 102 | L1 | CIS_Controls part links -> Mapping objects (v8 -> sibling CIS Controls bundle; v7 -> v7 namespace) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].name` | 336 | L1 | part dispatch (statement/desc/rationale, assessment-method, guidance kinds) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].props[].class` | 71 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].props[].name` | 407 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].props[].value` | 407 | L1 | part labels (Description/Rationale/Audit/Remediation/CIS Controls/References) -> facet keys; method TEST -> assessment-criteria; References markings -> external-references@1 payload (citation labels, kept bare) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].parts[].prose` | 192 | L1 | Description/Rationale -> narrative@1; Audit script -> assessment-criteria@1.audit; Remediation -> assessment-criteria@1.remediation (language-tagged) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].props[].class` | 48 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].props[].name` | 144 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].props[].value` | 144 | L1 | dispatch: label -> Requirement.label; marking xccdf_id -> aliases (scheme xccdf); marking automated|manual -> assessment-criteria@1 method (class attr on markings absorbed with the value) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].controls[].title` | 48 | L1 | Requirement id (URI mint) + title; statement prose minted from title (source statement empty - declared + counted) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].id` | 12 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].parts[].id` | 12 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].parts[].name` | 12 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].parts[].prose` | 12 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].props[].name` | 12 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].props[].value` | 12 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].groups[].groups[].title` | 12 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].groups[].groups[].id` | 27 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].groups[].groups[].parts[].id` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].parts[].name` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].parts[].prose` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].groups[].props[].name` | 27 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].groups[].props[].value` | 27 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].groups[].title` | 27 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].groups[].id` | 27 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].groups[].parts[].id` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].parts[].name` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].parts[].prose` | 27 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].groups[].props[].name` | 27 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].props[].value` | 27 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].groups[].title` | 27 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].id` | 7 | L1 | section Set id/title |
| `cisb.catalog.groups[].groups[].parts[].id` | 7 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].parts[].name` | 7 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].parts[].prose` | 7 | L2 | compat facet oscal-1x@1: section overview narrative on the Set (language-tagged {en}) |
| `cisb.catalog.groups[].groups[].props[].name` | 7 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].props[].value` | 7 | L1 | group label -> Set label |
| `cisb.catalog.groups[].groups[].title` | 7 | L1 | section Set id/title |
| `cisb.catalog.groups[].id` | 1 | L1 | section Set id/title |
| `cisb.catalog.groups[].title` | 1 | L1 | section Set id/title |
| `cisb.catalog.metadata.document-ids[].identifier` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.document-ids[].scheme` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.last-modified` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.links[].href` | 6 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.oscal-version` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.props[].name` | 3 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.props[].ns` | 2 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.props[].value` | 3 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.remarks` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.title` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.metadata.version` | 1 | L1 | bundle manifest / L0 provenance |
| `cisb.catalog.uuid` | 1 | L1 | bundle manifest / L0 provenance |

## UNMAPPED (gate target: zero)

*(none)*
