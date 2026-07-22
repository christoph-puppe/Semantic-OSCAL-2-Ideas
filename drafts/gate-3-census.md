# Gate 3 — Field Census: NIST SP 800-53 Rev 5 · 800-53B · CSF 2.0 · IFA lifecycle set
### The converter spec (ch14.4: census first, converter second) · 2026-07-22

Sources fetched 2026-07-22 from `usnistgov/oscal-content@main` (public
domain, NIST) into `sources/nist/` (gitignored by convention, though no
publisher-rights constraint applies). Census harness:
`oscal_conv_lib.inventory()` with depth-normalization
(`controls[]`/`parts[]`/`groups[]` recursion collapsed).

---

## 1. SP 800-53 Rev 5 catalog (`NIST_SP-800-53_rev5_catalog.json`, 10.4 MB)

Catalog version **5.2.0**, OSCAL 1.2.2. Raw: 153 leaf paths, 114,562
leaves; normalized: 73 paths.

**Structure:** 20 groups (families, `class=family`, no nesting) · 324
top-level controls · 872 enhancements (nested exactly 1 deep, never 2)
· 1,196 total · **182 withdrawn** (155 tombstone enhancements + 27
controls; no parts, no params — only labels, `status=withdrawn`, and
lineage links). Control `class`: `SP800-53` ×324 /
`SP800-53-enhancement` ×872.

**Six part names** (with counts at all depths):

| part | count | role |
|---|---:|---|
| `statement` / `item` | 1,016 / 1,122 | the control text, items nested ≤3 deep, ids `{cid}_smt.a.1.a`, print labels (`a.`, `1.`, `(a)`) as props |
| `guidance` | 1,014 | discussion prose, markdown `[X](#uuid)`/`[AC-1](#ac-1)` citation links |
| `assessment-objective` | 3,715 | SP 800-53A determination tree, `sp800-53a`-class labels (`AC-01a.[01]`), ODP insertions |
| `assessment-method` / `assessment-objects` | 2,931 / 2,931 | EXAMINE / INTERVIEW / TEST + newline-separated object lists |

**Control props:** `label` ×3,587 in three spellings — plain (`AC-2(1)`),
`zero-padded` (`AC-02(01)`), `sp800-53a` (`AC-02(01)`; zero-padded and
53a agree — converter verifies the equality) · `sort-id` ×1,196 ·
`implementation-level` (ns rmf) ×1,165 with values `organization` ×764 /
`system` ×401 (controls may carry both) · `contributes-to-assurance`
(ns rmf) ×427, only ever `true` · `status` ×182, only `withdrawn`.

**Links (5 rels):** `related` ×3,512 · `reference` ×838 (→ 201
back-matter resources: uuid/title/citation/rlinks→URL) · `required`
×714+1 (enhancement → its base control) · `incorporated-into` ×166 +
`moved-to` ×34 (withdrawal lineage; **targets may be statements**, e.g.
`ac-2.10 → #ac-2_smt.k`).

**Parameters (1,600) — two layers:**

- **1,458 ODPs** (`ac-01_odp.01`): the SP 800-53A organization-defined
  parameters. `label` key = human text ("personnel or roles"); prop
  `label` = formal ODP id (`AC-01_ODP[01]`, uppercase transform of the
  param id — converter verifies); `guidelines` ×1,327 (prose);
  `alt-identifier` ×1,126; 133 have `select` (97 `one-or-more`, 36
  one), **exactly the 133 without a `label` key**; 0 constraints, 0
  depends-on.
- **142 legacy `_prm_` aggregates** (`ac-1_prm_1`), each carrying
  `aggregates` props pointing at ODPs — the original Rev 5 blanks that
  53A split into ODPs. Prose inserts *both* layers: 2,945
  `{{ insert: param, … }}` tokens (0 malformed), 140 of 142 prm and
  1,387 of 1,458 odp inserted; **73 params never inserted anywhere**
  (71 odp + 2 prm) — declarations without insertion sites.

## 2. SP 800-53B baselines (4 profiles, 6–12 KB each)

Pure selections: `imports[].include-controls[].with-ids[]` — LOW 149 ·
MODERATE 287 · HIGH 370 · PRIVACY 96 — plus `merge.as-is` and
metadata. **Zero `alters`, zero `set-parameters`** (800-53B leaves ODPs
to implementers). Baselines are therefore **Sets, not Tailorings** —
membership is the entire semantic content.

## 3. CSF 2.0 (`NIST_CSF_v2.0_catalog.json`, 350 KB)

56 paths, 4,726 leaves. 6 functions (groups) · 219 controls = 34
categories (top) + 185 subcategories (nested, `class=subcategory`) ·
**91 withdrawn = 12 categories + 79 subcategories** (the 1.1→2.0
restructuring cut at both levels; measured by the converter — ID.GV
even moved to a whole *function*, `#GV`) · every control has one
`statement` part (outcome prose, declarative — no modality words;
**tombstones keep their 1.1 prose**, carried in the annotation) ·
`example` parts ×363 (implementation examples, ns csf, ids
`GV.OC-05.010`) · props: `sort-id` (numeric dotted
`00001.00001.00005`), `label`, `risk-party` (ns csf) ×125 with
`remarks` · links `incorporated_into` ×110 / `moved_to` ×25 —
**underscores where Rev 5 uses hyphens** (source finding, reported
below) · 0 params · group `overview` parts ×6 · back-matter ×4.

## 4. IFA GoodRead lifecycle set (+ leveraged pair + component-def)

| file | model | key content |
|---|---|---|
| `ifa_ssp.json` | SSP | 1 component + 6 inventory items, users/privileges, `implemented-requirements` with `by-components`, `set-parameters` ×5, system-characteristics (FIPS-199 impact), status `operational` |
| `ifa_assessment-plan.json` | AP | activities with steps ×6, reviewed-controls, tasks, assessment-subjects |
| `ifa_assessment-results.json` | AR | observations ×2 (methods/types/collected/expires), **findings ×1** (`target.status.state`), risks ×1, local activities |
| `ifa_plan-of-action-and-milestones.json` | POA&M | poam-items ×2, risks ×2 with **`deadline`**, remediations + tasks with `within-date-range`, characterizations (facets!) |
| `oscal_leveraged-example_ssp.json` | SSP | **`export.provided` + `export.responsibilities`** — the provider side |
| `oscal_leveraging-example_ssp.json` | SSP | **`inherited` + `satisfied`** + `leveraged-authorizations` — the consumer side (D5 basis-ref test) |
| `example-component-definition.json` | CDef | components with protocols + control-implementations |

---

## 5. Adjudication — Rev 5 catalog + baselines (the convergence-table pass)

Target bundle: `converted_examples/US.SP800-53/` · mint
`https://ns.nist.gov/sp800-53/req/{ID}` with ID = uppercase source id
(`AC-2`, `AC-2.1` — **dot form, matching the corpus's existing mapping
endpoints exactly**; the plain NIST spelling `AC-2(1)` goes to
`label`). Version `5.2.0`. Party URIs
`https://ns.nist.gov/sp800-53/party/{organization|system}`.

| source | level | destination |
|---|---|---|
| control `id`/`title` | L1 | Requirement id (URI mint) + title |
| `class` | L1 | encoded structurally (family Set membership + `required` base edge) |
| props `label` (plain) | L1 | `label` |
| props `label` zero-padded / sp800-53a | L3-derivable | mechanical zero-pad of `label`; converter asserts zero-padded == 53a |
| props `sort-id` | L1 | Set member `sequence` (order ×10) |
| props `implementation-level` | L1 | `obligated-parties` mint (organization/system; absent → organization, counted) |
| props `contributes-to-assurance` | L2 | facet `…/facet/rmf@1` `{contributes-to-assurance: true}` |
| props `status` + `incorporated-into`/`moved-to` links | L1 | **tombstones dropped; lineage inverted onto the successor's kernel `replaces[]`** — `incorporated-into` → mode `merged-into`, `moved-to` → mode `renamed`; statement-precision targets + withdrawn label/title preserved in the successor's `annotations["nist-withdrawal"]` |
| parts `statement`/`item` (+ item label props) | L1 | flattened `statements[]` — every prose-bearing item, id = part-id suffix (`smt.a.1.a`), print labels L3-derivable (id-encoded); modality `must` (corpus rule: NIST imperative + baseline-mandatory semantics); `{{ insert: param, x }}` → `{param:x}` |
| parts `guidance` | L2 | facet `…/facet/narrative@1` `guidance[]`, language-tagged; markdown `[X](#uuid)`/`[X](#ctrl)` → `X` (citation rides the `reference` relation), rewrites counted |
| parts `assessment-objective/-method/-objects` | L2 | facet `…/facet/sp800-53a@1`: objective tree `{id, label, prose}` + methods `{method, label, objects[]}`; insertions → `{param:}` tokens |
| `params` (odp + prm) | L1 | statement-scoped kernel `parameters[]` declared **on each statement whose prose inserts them** (the 216 rule is per-statement); select → `choice` + `choices[]` + `cardinality: many` for one-or-more; else `string`; never-inserted (73) declared on the first statement, counted |
| param `guidelines`, `alt-identifier`, `alt-label`, prm `aggregates` | L2 | facet `…/facet/odp@1` per-param admin `{guidelines, alt-identifiers, alt-label, aggregates}` |
| param prop `label` (formal `AC-01_ODP[01]`) | L3-derivable | uppercase transform of param name; converter asserts round-trip |
| links `related` | L1 | relation `related` → minted URI |
| links `reference` | L1 | relation `reference` → **resolved rlink URL** (landmark); resource title/citation table → facet `…/facet/references@1` on the root Set |
| links `required` | L1 | relation `required` → minted URI |
| groups | L1 | 20 family Sets + root Set (D21 nesting); `pm` group `overview` part → narrative facet on the pm Set |
| baselines `with-ids` | L1 | 4 Sets `…/set/baseline/{low,moderate,high,privacy}`, members = minted URIs, sequence = catalog order |
| baseline `merge.as-is`/`imports.href` | L3 | OSCAL-profile mechanics; the selection *is* the Set (counted, declared) |
| metadata / back-matter admin | L1 | bundle manifest / L0 provenance |

**Modality note (fifth corpus).** Live Rev 5 statements are uniformly
imperative ("Develop, document, and disseminate …") with obligation
bound by baseline selection — the *inverse* of the declarative national
pattern (ISM/CIS/CyFun/C5: `unspecified` prose, force via membership).
Here force is in the mood and selection is still membership: modality
`must`, selection rides the baseline Sets. Both patterns confirm D13:
force and selection are separate axes.

## 6. Adjudication — CSF 2.0

Target `converted_examples/US.CSF/` · mint
`https://ns.nist.gov/csf/req/{ID}` (ids `GV.OC-05` as-is; no version in
the URI — lineage is D2's job). Version `2.0`.

| source | level | destination |
|---|---|---|
| functions (6 groups) + `overview` parts | L1 / L2 | function Sets; overview → narrative facet on the Set |
| categories (34) | L1 | **category Sets** (the C5 rule: membership decides granularity); category statement prose → narrative facet on the Set |
| subcategories (185 − 79 withdrawn = 106 live; 12 of 34 categories also withdrawn) | L1 | Requirements, one statement, modality `unspecified` (outcome prose — sixth-corpus confirmation of the declarative pattern), obligated-party default `…/csf/party/organization` |
| `example` parts ×363 | L2 | facet `…/facet/examples@1` `{examples: [{id, prose}]}` |
| props `risk-party` (+remarks) | L2 | facet `…/facet/csf@1` |
| props `sort-id`/`label` | L1 | member sequence / `label` |
| `status` + `incorporated_into`/`moved_to` | L1 | tombstone inversion onto successor `replaces[]` (as Rev 5) |
| back-matter ×4 / metadata | L1 | references facet on root Set / provenance |

## 7. Pre-registered findings (from census alone)

1. **CSF/Rev5 rel-code divergence:** `incorporated_into`/`moved_to`
   (underscore) vs `incorporated-into`/`moved-to` (hyphen) — the same
   publisher, the same semantic, two spellings. Report upstream.
2. **73 never-inserted params** (71 odp + 2 prm): declarations without
   insertion sites — ODPs defined for assessment that the control text
   never binds lexically.
3. **Withdrawn tombstones cited elsewhere:** count of corpus mapping
   endpoints that hit withdrawn Rev 5 ids — measured by the converter's
   cross-check; a resolver follows `replaces[]` backwards.
4. **#10 ambiguity measure:** ODPs inserted in ≥2 statements would make
   the (requirement, odp) → statement address ambiguous — the converter
   counts them; the count decides control-level pool vs statement map.

## 8. What gate 3 measures for the backlog

- **#10:** the statement-declaration map + ambiguity count (§7.4) +
  the 79 CR26 CTL entries re-addressed against minted statement ids.
- **#9:** finding/assessment state seeds vs the IFA corpus's actual
  states (AR finding `target.status.state`, POA&M risk states,
  remediation lifecycle).
- **#16 promotion:** with Rev 5 in-bundle, CR26/SCF mapping endpoints
  that were landmark become closure-checkable — re-run and report.

---

## 9. Outcome (2026-07-22, same day)

All three converters delivered census-first and green — see the
computed coverage reports beside each bundle, spec IV.9, and the
register ("Amendments — gate 3"). Headlines: **UNMAPPED 0 on all three
corpora** (115,680 + 4,726 + 835 leaves) · **zero kernel-schema changes
forced** (customer test passed) · #10 drained by measurement (§7.4:
multi-declared = 0) · all 373 corpus mapping endpoints resolve (§7.3:
withdrawn hits = 0) · #9 confirmed with zero enum additions · two
reference-validator defects exposed and fixed (tier wrapper-laundering,
choice-many list values; 125 → 129 vectors) · the pre-registered
findings of §7 all landed, plus five more source findings (see IV.9).
