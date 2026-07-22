# CIS Controls v8.1 -> Semantic Core: Coverage Report (computed)

Source: **CIS Controls** v8.1 (OSCAL 1.1.3) - 18 Controls + 153 Safeguards.

## Totals

- Source leaf values inventoried: **5,493**
- Mapped (declared destination): **5,493**
- **UNMAPPED: 0**  ->  coverage **100.0 %**
- Objects emitted: **171 Requirements** (18 Controls + 153 Safeguards), **34 Sets** (per-control taxonomy + root + 3 IG baselines + 6 asset-class + 6 security-function), manifest with both digests.

## Conversion rules (declared, counted)

- **Safeguards are Requirements, not statements** - IG baselines bind at safeguard level, and Set members reference objects, never statements (the membership argument decides the granularity).
- **Modality word-rule**: unspecified x148, may x10, must x8, should x4, must-not x1. CIS prose is imperative ('Establish and maintain ...'): modal verbs are structurally absent; binding force rides IG membership (the ISM pattern, third confirmation).
- **implementation-group -> baseline Sets** ig1 (56) / ig2 (130) / ig3 (153); declared cumulative in-source: **holds** (checked, not assumed).
- **asset-class / security-function -> category Sets** (data 32, devices 25, documentation 20, network 23, software 24, users 29 | detect 24, govern 25, identify 14, protect 78, recover 6, respond 6).
- **frequency -> assessment-criteria@1 `frequency`** (assessment cadence, gate-2 schema alignment - a fixed stipulation is not an insertion point, so it is facet payload, not a parameter): annually x30, monthly x8, bi-annually x5, weekly x5, quarterly x4, daily x1. Typed-duration mapping deferred: 'bi-annually' is lexically ambiguous (two readings); a code is the honest encoding until CIS defines the period (candidate authors'-queue item).
- **assessment-objective parts -> assessment-criteria@1** objectives[] (top-level x153, nested sub-objectives carried recursively; per-safeguard `assessment-for` links resolved to Requirement URIs); example/guidance -> narrative@1.
- **links rel=required -> typed relations** (safeguard dependencies; dangling x0); rel=reference resolved via back-matter (40 resources, untitled x0, unresolved x0).
- **Payload free text language-tagged** ({en: ...}): example x38, guidance x12, objective x370. Harmonized from the start (backlog #12).
- **Obligated party**: documented default https://ns.cisecurity.org/controls/v8/party/enterprise (CIS binds 'the enterprise' implicitly).

## Findings (computed)

- **Controls carry no implementation-group** (x18: all 18 parents): IG membership exists only at safeguard level - a consumer selecting 'IG1' gets safeguards, never the parent prose; parent Requirements ride along via the taxonomy Sets. Structural fact, REPORTED.
- **IG cumulativity measured**: IG1 < IG2 < IG3 holds exactly (56/130/153).
- Declarative/imperative corpus #3: unspecified x148 of 171 - the ISM finding generalizes (imperative English, force via membership).

## Full path map (every source path, its count, its destination)

| path | count | level | destination |
|---|---:|---|---|
| `cisc.catalog.back-matter.resources[].rlinks[].href` | 40 | L1 | reference resolution table: uuid -> title/URL for relations reference |
| `cisc.catalog.back-matter.resources[].title` | 40 | L1 | reference resolution table: uuid -> title/URL for relations reference |
| `cisc.catalog.back-matter.resources[].uuid` | 40 | L1 | reference resolution table: uuid -> title/URL for relations reference |
| `cisc.catalog.groups[].controls[].controls[].id` | 153 | L1 | Requirement id (URI mint) + per-control taxonomy Set id |
| `cisc.catalog.groups[].controls[].controls[].links[].href` | 257 | L1 | rel=required -> relations required (safeguard URIs); rel=reference -> relations reference (resolved via back-matter) |
| `cisc.catalog.groups[].controls[].controls[].links[].rel` | 257 | L1 | rel=required -> relations required (safeguard URIs); rel=reference -> relations reference (resolved via back-matter) |
| `cisc.catalog.groups[].controls[].controls[].parts[].id` | 356 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].controls[].parts[].links[].href` | 153 | L1 | rel=assessment-for -> assessment-criteria@1 objectives[].assessment-for (resolved to Requirement URI) |
| `cisc.catalog.groups[].controls[].controls[].parts[].links[].rel` | 153 | L1 | rel=assessment-for -> assessment-criteria@1 objectives[].assessment-for (resolved to Requirement URI) |
| `cisc.catalog.groups[].controls[].controls[].parts[].name` | 356 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].controls[].parts[].parts[].id` | 217 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].controls[].parts[].parts[].name` | 217 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].controls[].parts[].parts[].prose` | 217 | L1 | statement -> statements[0].prose.en; objectives/example/guidance -> facet payloads (language-tagged) |
| `cisc.catalog.groups[].controls[].controls[].parts[].prose` | 269 | L1 | statement -> statements[0].prose.en; objectives/example/guidance -> facet payloads (language-tagged) |
| `cisc.catalog.groups[].controls[].controls[].props[].name` | 851 | L1 | dispatch: label -> Requirement.label; implementation-group -> baseline Sets ig1/ig2/ig3; asset-class/security-function -> category Sets; frequency -> assessment-criteria@1 cadence; ns absorbed |
| `cisc.catalog.groups[].controls[].controls[].props[].ns` | 698 | L1 | dispatch: label -> Requirement.label; implementation-group -> baseline Sets ig1/ig2/ig3; asset-class/security-function -> category Sets; frequency -> assessment-criteria@1 cadence; ns absorbed |
| `cisc.catalog.groups[].controls[].controls[].props[].value` | 851 | L1 | dispatch: label -> Requirement.label; implementation-group -> baseline Sets ig1/ig2/ig3; asset-class/security-function -> category Sets; frequency -> assessment-criteria@1 cadence; ns absorbed |
| `cisc.catalog.groups[].controls[].controls[].title` | 153 | L1 | Requirement title |
| `cisc.catalog.groups[].controls[].id` | 18 | L1 | Requirement id (URI mint) + per-control taxonomy Set id |
| `cisc.catalog.groups[].controls[].links[].href` | 36 | L1 | rel=required -> relations required (safeguard URIs); rel=reference -> relations reference (resolved via back-matter) |
| `cisc.catalog.groups[].controls[].links[].rel` | 36 | L1 | rel=required -> relations required (safeguard URIs); rel=reference -> relations reference (resolved via back-matter) |
| `cisc.catalog.groups[].controls[].parts[].id` | 18 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].parts[].name` | 18 | L1 | part dispatch: statement -> statements[0]; assessment-objective (incl. nested sub-objectives) -> assessment-criteria@1 objectives[]; example/guidance -> narrative@1 |
| `cisc.catalog.groups[].controls[].parts[].prose` | 18 | L1 | statement -> statements[0].prose.en; objectives/example/guidance -> facet payloads (language-tagged) |
| `cisc.catalog.groups[].controls[].props[].name` | 18 | L1 | dispatch: label -> Requirement.label; implementation-group -> baseline Sets ig1/ig2/ig3; asset-class/security-function -> category Sets; frequency -> assessment-criteria@1 cadence; ns absorbed |
| `cisc.catalog.groups[].controls[].props[].value` | 18 | L1 | dispatch: label -> Requirement.label; implementation-group -> baseline Sets ig1/ig2/ig3; asset-class/security-function -> category Sets; frequency -> assessment-criteria@1 cadence; ns absorbed |
| `cisc.catalog.groups[].controls[].title` | 18 | L1 | Requirement title |
| `cisc.catalog.groups[].id` | 1 | L1 | root Set id/title |
| `cisc.catalog.groups[].title` | 1 | L1 | root Set id/title |
| `cisc.catalog.metadata.document-ids[].identifier` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.document-ids[].scheme` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.last-modified` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.links[].href` | 3 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.links[].rel` | 3 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.oscal-version` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.props[].name` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.props[].value` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.title` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.metadata.version` | 1 | L1 | bundle manifest / L0 provenance |
| `cisc.catalog.uuid` | 1 | L1 | bundle manifest / L0 provenance |

## UNMAPPED (gate target: zero)

*(none)*
