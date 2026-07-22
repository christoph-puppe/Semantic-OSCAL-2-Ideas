# C5:2026 -> Semantic Core: Coverage Report (computed)

Source: **Cloud Computing Compliance Criteria Catalogue (C5:2026)** vC5:2026 (OSCAL 1.2.2, published 2026-03-30).

## Totals

- Source leaf values inventoried: **5,868**
- Mapped (declared destination): **5,868**
- **UNMAPPED: 0**  ->  coverage **100.0 %**
- Objects emitted: **623 Requirements**, **190 Sets** (18 domains + 168 criteria + root + 3 class Sets), manifest with both digests.

## Conversion rules (declared, counted)

- **Criteria are Sets, class children are Requirements** - the basic/additional split binds per child, so membership decides granularity (the CIS-safeguard argument, second confirmation).
- **class -> membership Sets**: additional-complement (132), additional-sharpen (29), basic (462); Basic is the certification baseline Set.
- **Modality word-rule**: unspecified x593, may x17, must x9, should x4. C5 prose is declarative present tense ('The cloud service provider maintains ...') - the ISM pattern, fourth corpus confirmation; force rides the class Sets.
- **sharpened-basic-criterion -> typed `sharpens` relation**: resolved x28, broken targets x0; sharpen-class children WITHOUT the pointer prop x1 (['am-10-01as']).
- **corresponding parts (x60) -> c5/corresponding@1** on the criterion Set: customer-side duties - measured CRM evidence for the shared-responsibility model (handbook ch09).
- **guidance(-N) parts -> narrative@1** guidance[] (children with 2+ guidance parts exist; all carried).
- **Obligated party**: documented default https://ns.bsi.bund.de/c5/party/cloud-service-provider (C5 binds the provider; customer duties live in the corresponding facet, deliberately NOT as obligated-parties).
- **Payload free text language-tagged** ({en: ...}): corresponding x60, guidance x474. Harmonized from the start (backlog #12).

## Findings (computed)

- **Defective source ids: 6 x `gc-undefined`** - six title-only stubs in the GC group share one id (an id collision inside a single authoritative publication; the twin-catalog corpse in miniature). Parked as a Level-2 compat payload on the GC domain Set, REPORTED for the C5 authors' queue: Information on applicable law, jurisdiction, countries, part; Information on availability and incident handling during reg; Information on recovery parameters in emergency operation; Information on the approach to ensuring service availability; Information on how investigation requests from government ag; Information on certifications or attestations.
- **Sharpening pointer gap x1**: ['am-10-01as'] is additional-sharpen class but carries no sharpened-basic-criterion prop - the machine-readable sharpening graph has one missing edge; REPORTED.
- Declarative corpus #4: unspecified x593 of 623 - convergent with ISM/CIS/CyFun-partial: national frameworks state duties declaratively and bind force via membership.

## Full path map (every source path, its count, its destination)

| path | count | level | destination |
|---|---:|---|---|
| `c5.catalog.groups[].controls[].controls[].class` | 623 | L1 | class -> membership Sets: baseline/basic | tax/additional-sharpen | tax/additional-complement |
| `c5.catalog.groups[].controls[].controls[].id` | 623 | L1 | Requirement id (URI mint) + label derivation + title |
| `c5.catalog.groups[].controls[].controls[].parts[].id` | 1,097 | L1 | statement -> statements[0].prose.en; guidance(-N) -> narrative@1 guidance[] (language-tagged) |
| `c5.catalog.groups[].controls[].controls[].parts[].name` | 1,097 | L1 | statement -> statements[0].prose.en; guidance(-N) -> narrative@1 guidance[] (language-tagged) |
| `c5.catalog.groups[].controls[].controls[].parts[].prose` | 1,097 | L1 | statement -> statements[0].prose.en; guidance(-N) -> narrative@1 guidance[] (language-tagged) |
| `c5.catalog.groups[].controls[].controls[].props[].name` | 28 | L1 | sharpened-basic-criterion -> typed relation `sharpens` -> sibling basic criterion URI |
| `c5.catalog.groups[].controls[].controls[].props[].value` | 28 | L1 | sharpened-basic-criterion -> typed relation `sharpens` -> sibling basic criterion URI |
| `c5.catalog.groups[].controls[].controls[].title` | 623 | L1 | Requirement id (URI mint) + label derivation + title |
| `c5.catalog.groups[].controls[].id` | 174 | L1 | criterion Set id/title (parents) | parked-L2 stub titles (gc-undefined defect class) |
| `c5.catalog.groups[].controls[].parts[].id` | 60 | L1 | corresponding parts -> c5/corresponding@1 on the criterion Set (customer-side duties; CRM evidence; language-tagged) |
| `c5.catalog.groups[].controls[].parts[].name` | 60 | L1 | corresponding parts -> c5/corresponding@1 on the criterion Set (customer-side duties; CRM evidence; language-tagged) |
| `c5.catalog.groups[].controls[].parts[].prose` | 60 | L1 | corresponding parts -> c5/corresponding@1 on the criterion Set (customer-side duties; CRM evidence; language-tagged) |
| `c5.catalog.groups[].controls[].parts[].title` | 60 | L1 | corresponding parts -> c5/corresponding@1 on the criterion Set (customer-side duties; CRM evidence; language-tagged) |
| `c5.catalog.groups[].controls[].title` | 174 | L1 | criterion Set id/title (parents) | parked-L2 stub titles (gc-undefined defect class) |
| `c5.catalog.groups[].id` | 18 | L1 | domain Set id/title |
| `c5.catalog.groups[].title` | 18 | L1 | domain Set id/title |
| `c5.catalog.metadata.last-modified` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.oscal-version` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].addresses[].addr-lines[]` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].addresses[].city` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].addresses[].country` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].addresses[].postal-code` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].links[].href` | 3 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].links[].rel` | 3 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].links[].text` | 2 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].name` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].short-name` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].type` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.parties[].uuid` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.props[].name` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.props[].value` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.published` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.responsible-parties[].party-uuids[]` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.responsible-parties[].role-id` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.roles[].id` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.roles[].title` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.title` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.metadata.version` | 1 | L1 | bundle manifest / L0 provenance |
| `c5.catalog.uuid` | 1 | L1 | bundle manifest / L0 provenance |

## UNMAPPED (gate target: zero)

*(none)*
