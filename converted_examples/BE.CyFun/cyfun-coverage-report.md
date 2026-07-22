# CyFun (BASIC + ESSENTIAL) -> Semantic Core: Coverage Report (computed)

Sources: **CyFun 2025 BASIC Resolved** + **CyFun 2025 ESSENTIAL Resolved** v2025-12-12 (OSCAL 1.1.3, resolved by Comply0) - one corpus, two membership levels.

## Totals

- Source leaf values inventoried: **4,312**
- Mapped (declared destination): **4,312**
- **UNMAPPED: 0**  ->  coverage **100.0 %**
- Objects emitted: **218 Requirements**, **124 Sets** (taxonomy + 3 cumulative baselines + 2 marker Sets), manifest with both digests.

## Conversion rules (declared, counted)

- **Modality word-rule** over shall-language statements (shall->must per ISO convention): must x208, should x7, unspecified x2, must-not x1.
- **ESSENTIAL is the requirement superset** (218 controls); BASIC (34) contributes membership evidence only - no duplicate objects, no twin ids (the GS++/MS-TLS lesson applied preventively).
- **assurance-level -> cumulative baseline Sets** basic (34) < important (+103) < essential (+82); key-measures (29) and governance-measures (21) -> marker Sets.
- **Group narrative** (overview parts x22) -> Level 2 compat facet oscal-1x@1 on the nearest Set (ISM pattern); residue KPI starts at 22.
- **Obligated party**: documented default https://ns.ccb.belgium.be/cyfun/party/organisation (CyFun binds the organisation implicitly).
- **Payload free text language-tagged** per corpus language ({en: ...}): prose x22. Harmonized from the start (backlog #12).
- `sort-id` absorbed by document order -> members[].sequence; `label` props -> kernel labels; cyfun.eu prop namespace absorbed (kernel fields need none).

## Findings (computed)

- **Twin-catalog check (preventive): 34 shared ids, 34 identical, drift 0** - no silent divergence between the two published resolutions; the corpse stayed dead.
- **BASIC-only controls: 0** (memberships beyond ESSENTIAL would be a resolution defect): none.
- **Duplicated assurance-level props x1**: [('ID.AM-5.1', ['basic', 'important'])] - one control carries two level declarations; REPORTED for the CCB/tooling queue (source defect class: duplicated prop).
- **BASIC-file membership vs. declared level**: 0 controls sit in the BASIC resolution without carrying assurance-level=basic: [] - membership and level declaration disagree; REPORTED (the applicability-vs-profile split, CyFun edition).
- **Declarative/imperative modality**: unspecified x2 of 218 - binding force rides the assurance-level baseline Sets where prose carries no modal verb (ISM pattern).

## Full path map (every source path, its count, its destination)

| path | count | level | destination |
|---|---:|---|---|
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].id` | 252 | L1 | Requirement id (URI mint) + label |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].parts[].id` | 252 | L1 | statements[0] (id suffix, prose.en + modality word-rule over shall-language) |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].parts[].name` | 252 | L1 | statements[0] (id suffix, prose.en + modality word-rule over shall-language) |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].parts[].prose` | 252 | L1 | statements[0] (id suffix, prose.en + modality word-rule over shall-language) |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].props[].name` | 822 | L1 | dispatch: label -> Requirement.label; sort-id absorbed -> sequence; assurance-level -> cumulative baseline Sets; key-measures/governance-measures -> marker Sets; ns absorbed |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].props[].ns` | 318 | L1 | dispatch: label -> Requirement.label; sort-id absorbed -> sequence; assurance-level -> cumulative baseline Sets; key-measures/governance-measures -> marker Sets; ns absorbed |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].props[].value` | 822 | L1 | dispatch: label -> Requirement.label; sort-id absorbed -> sequence; assurance-level -> cumulative baseline Sets; key-measures/governance-measures -> marker Sets; ns absorbed |
| `cyfun.*.catalog.groups[].groups[].groups[].controls[].title` | 252 | L1 | Requirement title |
| `cyfun.*.catalog.groups[].groups[].groups[].id` | 118 | L1 | Set id |
| `cyfun.*.catalog.groups[].groups[].groups[].props[].name` | 236 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].groups[].groups[].props[].value` | 236 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].groups[].groups[].title` | 118 | L1 | Set title |
| `cyfun.*.catalog.groups[].groups[].id` | 39 | L1 | Set id |
| `cyfun.*.catalog.groups[].groups[].parts[].name` | 39 | L2 | compat facet oscal-1x@1: function/category overview narrative on the Set (language-tagged {en}) |
| `cyfun.*.catalog.groups[].groups[].parts[].prose` | 39 | L2 | compat facet oscal-1x@1: function/category overview narrative on the Set (language-tagged {en}) |
| `cyfun.*.catalog.groups[].groups[].props[].name` | 78 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].groups[].props[].value` | 78 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].groups[].title` | 39 | L1 | Set title |
| `cyfun.*.catalog.groups[].id` | 12 | L1 | Set id |
| `cyfun.*.catalog.groups[].props[].name` | 12 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].props[].value` | 12 | L1 | group props: label -> Set label; sort-id absorbed by document order -> members[].sequence |
| `cyfun.*.catalog.groups[].title` | 12 | L1 | Set title |
| `cyfun.*.catalog.metadata.document-ids[].identifier` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.document-ids[].scheme` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.last-modified` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.links[].href` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.links[].rel` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.oscal-version` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.props[].name` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.props[].value` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.title` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.metadata.version` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |
| `cyfun.*.catalog.uuid` | 2 | L1 | bundle manifest / L0 provenance (incl. resolution-tool note; document-ids -> aliases on the root Set) |

## UNMAPPED (gate target: zero)

*(none)*
