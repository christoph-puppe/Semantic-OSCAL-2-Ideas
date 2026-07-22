# OSCAL Semantic Core — Pass P9 Adversarial Design Review Report
### Flaw Hunt & North-Star Audit · v0.6 Cycle Input · 2026-07-21

**Date:** 2026-07-21  
**Commit Reviewed:** `b254f90aa12485a4d5b1caa8af0882c8cce52e60`  
**Execution Environment & Limitations:** Windows 11 (PowerShell), Python 3.12 via `uv`. Full shell and code execution capabilities were available and utilized in this session. All counts, bundle validations, schema checks, and adversarial test objects were computed/constructed directly against repo binaries and JSON artifacts in this session. No execution limitations required downgrading instructions.

---

## 1. Findings Register

| ID | Severity | Class | Basis | Evidence (`file:line` or command) | Corpse (Failure Scenario) | North-Star Implicated | Challenges Adjudication? | Proposed Disposition |
|---|---|---|---|---|---|---|---|---|
| **P9-1** | **Blocker** | Design flaw (a) / Internal inconsistency (b) | Demonstrated | `semantic-oscal/schemas/oscal-semantic-core-1.0.0.schema.json:62` & `validate_core.py:225` | Corrupt or invalid facet payloads and unregistered facet URIs pass validation green, resurrecting the OSCAL 1.x "valid and meaningless" props-smuggling pathology under the new kernel. | *no more props* · *less need for bespoke JSON* | Yes (D10) | v0.6 spec change / validator update: enforce stdlib facet descriptor schema validation and Portable fail-closed checks on unregistered facets. |
| **P9-2** | **Major** | Inflated claim (c) | Measured | `semantic-oscal/conformance/` (54 vectors across 5 files) | A tool claims Portable-tier conformance by passing 54 vectors, but silently fails on mapping scoping, component authorization boundaries, or facet fail-closed rules. | *simpler* | Yes (D15) | Backlog entry: author negative and positive conformance vectors for the 7 untested normative spec subsystems. |
| **P9-3** | **Major** | Inflated claim (c) / Doc drift (d) | Measured | `README.md:120` vs `drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md:15` | Adopters over-estimate kernel stability, believing the kernel froze before validation, unaware that validation framework conversion forced the D9 rev parameter schema amendment. | *closer to measured customer needs* | Yes (D9 rev / D22) | Erratum in `README.md` clarifying that validation corpus conversion drove the D9 rev parameter schema expansion. |
| **P9-4** | **Major** | Design flaw (a) / Internal inconsistency (b) | Demonstrated | `validate_core.py:201` & `scratch/test_adversarial.py` | Mappings with self-loops (`source-ref == target-ref`) and non-existent statement scopes (`statement:ghost_999`) pass validation, corrupting multi-framework crosswalk queries. | *closer to measured customer needs* | Yes (D20) | Validator update: verify `Mapping` statement scopes against referenced catalog statements during bundle validation. |
| **P9-5** | **Major** | Design flaw (a) | Argued | `drafts/oscal-semantic-core-v0.5-specification.md:261` (D9) & backlog #13 | Offline generic tools evaluating CR26/BSI deadlines hit unresolvable `calendar-period` fields without shared stdlib calendar codes, causing forced fail-closed halts across bundles. | *simpler* | Yes (D9) | Expedite backlog item #13: define stdlib `calendar-context` code system (`us-federal`, `de-bund`, etc.). |
| **P9-0** | **Minor** | Internal inconsistency (b) / Doc drift (d) | Measured / Quoted | `drafts/oscal-semantic-core-decision-rationale-register.md:2` vs `README.md:63` | Reviewers evaluating decisions against the Decision Rationale Register use a 3-criterion model that disagrees with the 4-test North Star in the spec and handbook. | All | New | Erratum in `drafts/oscal-semantic-core-decision-rationale-register.md:2,5` harmonizing text to the 4-test North Star formulation. |
| **P9-6** | **Minor** | Inflated claim (c) / Doc drift (d) | Measured | `README.md:95` vs `scratch/check_bundle_manifests.py` | Independent auditors recomputing object counts from bundle manifests find 5,470 objects instead of the claimed 5,478, creating doubt regarding repo metrics. | None | New | Erratum in `README.md:95` updating headline compliance object count to 5,470 (5,483 with skill-examples). |
| **P9-7** | **Note** | Inflated claim (c) | Argued | `semantic-oscal/references/ch01-why-this-exists.md:263` | Engineering managers budget implementation time based on the handbook's "days" claim, discovering that implementing 2 digest domains, JCS pre-normalization, and resolution state machines takes weeks. | *simpler* | New | Label claim as *hypothesized* in Ch01 per Ground Rule 1, pending the v0.6 gate measured complexity comparison. |

---

## 2. Detailed Paragraphs for Blocker and Major Findings

### P9-1 (Blocker) — Facet System Evasion & Fail-Closed Vacuum (Valid-and-Meaningless Kernel Rebirth)
* **Description:** The OSCAL Semantic Core architecture relies on registered facets to extend the kernel with framework-specific semantics while promising machine-checked contracts and fail-closed behavior for unknown semantics (D10, Handbook Ch07). However, inspection of `semantic-oscal/schemas/oscal-semantic-core-1.0.0.schema.json` (lines 62–64) reveals that the normative kernel JSON Schema defines `"facets"` as `"additionalProperties": { "type": "object" }`, placing zero schema constraints on facet payload structures beyond property names matching `@[0-9]+$`. Furthermore, inspection of the reference validator (`semantic-oscal/scripts/validate_core.py`) reveals that while it validates statement key alignment for `by-statement` payloads (D10 rev), it performs **zero** JSON Schema validation over facet payloads against stdlib descriptors and **zero** checks for unknown/unregistered facet URIs. In this session, an adversarial object (`scratch/test_adversarial.py`, Test 1) carrying invalid payload types violating stdlib descriptor schemas AND an unregistered facet URI (`https://example.org/unregistered-dangerous-facet@99`) was constructed and validated against `validate_core.py`; it validated green with zero warnings or errors.
* **Corpse:** A framework author or vendor publishes compliance objects containing corrupt, malformed, or unregistered facet payloads. Because neither the kernel schema nor the validator inspects facet payloads or enforces fail-closed rules on unregistered URIs, the corrupt data is certified as 100% valid by tools. Downstream consumers parsing the objects silently ignore or misinterpret the semantics, recreating the exact 1.x "props smuggler" / "valid-and-meaningless" pathology that the project cited 216 German Grundschutz++ pseudo-placeholders to condemn.

### P9-2 (Major) — Conformance Corpus Incompleteness: Zero Negative/Positive Coverage for 7 Normative Subsystems
* **Description:** Specification D15 and `validate_core.py` assert a 54-vector conformance corpus across 5 test files (`jcs-vectors.json`, `modality-vectors.json`, `parameter-vectors.json`, `tailoring-vectors.json`, `attestation-vectors.json`). A complete audit of `semantic-oscal/conformance/` against the normative spec text reveals that **seven core normative subsystems have exactly zero conformance vectors**:
  1. `canonical-alias` vs `replaces` identity/lineage substitution rules (D2);
  2. Facet descriptor schema validation and Portable-tier fail-closed execution halts (D10);
  3. Bundle composition semver resolution and minor-line merging (D3.5);
  4. Component authorization boundary induction and mandatory `basis-ref` enforcement (D5);
  5. `Mapping` relationship non-chaining semantics (`supplements`) and statement scope matching (D20);
  6. `Deviation` lifecycle state machine transitions (`investigating` → `pending` → `approved`) (D8);
  7. `Finding` lifecycle state machine transitions (`open` → `in-remediation` → `closed`) (Ch10).
* **Corpse:** A software vendor implements a minimal validator that passes the 54 shipped vectors and claims "Conformant Portable Processor" status. In production, when processing cross-framework `Mapping` objects, component authorization boundaries, or unregistered facets, the tool silently permits invalid operations or illegal state transitions because the conformance test suite never tested those normative MUST requirements.

### P9-3 (Major) — Inflated Survivorship Claim: Validation Corpora Prompted Kernel Schema Amendments
* **Description:** `README.md` (line 120) asserts that five validation frameworks (BE.CyFun, CIS.Controls, CIS.Ubuntu2404, DE.C5, DE.C3A) were converted on 2026-07-21 and "the model held without kernel changes". However, repository git logs and `drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md` (item #1) document that on 2026-07-21 (the same day), parameter `label` and `default` were added to the kernel `parameter` schema (spec D9 rev) specifically to absorb parameters from BSI and DE.C3A (which carried 30 typed parameters with labels/defaults). Adding `label` and `default` to `parameter` in `oscal-semantic-core-1.0.0.schema.json` is a direct structural change to the kernel schema.
* **Corpse:** Evaluators and standardizers rely on the README's claim that the kernel model held without changes across five external validation targets as measured proof of kernel completeness. In reality, encountering DE.C3A and BSI forced an expansion of the kernel schema's parameter declaration definition, meaning the claim as written is overstated.

### P9-4 (Major) — Scope Validation Vacuum in Mapping Objects & Sub-Object References
* **Description:** Specification D20 introduces `Mapping` as the ninth kernel type, requiring statement-level scope targeting via `source-scope` and `target-scope` arrays. While `validate_core.py` checks statement ID references inside Requirement facet `by-statement` payloads (D10 rev), it performs **zero** validation on `Mapping` `source-scope` / `target-scope` strings or internal URI/ref fields (`requirement-ref`, `assessment-ref`, `statement-ref`, `approver-ref`). In this session, an adversarial `Mapping` object (`scratch/test_adversarial.py`, Test 4) featuring self-referential mapping (`source-ref == target-ref`) and non-existent statement scopes (`statement:ghost_999`) was constructed and run through `validate_core.py`; it passed as 100% valid.
* **Corpse:** An authority or third-party mapper publishes crosswalk `Mapping` objects containing typos in `source-scope` or `target-scope` (referencing non-existent clause IDs), or self-referential loops. The validator certifies the bundle as valid, but downstream compliance engines performing cross-framework gap analysis produce zero matches or infinite loops.

### P9-5 (Major) — Unresolvable Calendar Dependencies Fail Closed on Offline Generic Tools
* **Description:** Specification D9 and Decision Register D9 introduce a strict unit-class boundary separating `elapsed-duration` from `calendar-period` (`days`, `bizdays`, `months`, `years`), requiring that deadline arithmetic over `calendar-period` without a resolvable calendar context MUST fail closed with an error. Backlog item #13 acknowledges that zero shared calendar codes exist in `oscal-stdlib`, forcing the CR26 converter to mint `us-federal` ad hoc.
* **Corpse:** An offline or air-gapped GRC tool operating at Portable tier ingests a CR26 bundle containing `calendar-period` parameters bound to `bizdays`. Because no normative `calendar-context` code system is shipped in `oscal-stdlib` to resolve business days and holidays offline, the tool is normatively required by D9 to fail closed and abort evaluation, rendering automated compliance verification impossible for time-sensitive requirements.

---

## 3. Mission B — The North-Star Audit

### B1. Canonicalization of the North Star

A systematic audit across all front-door documents reveals a **direct structural contradiction** in how the North Star is formulated:

* **Specification (`v0.5-specification.md:17`):** 4 tests — *"more simple · closer to the needs of the customers · no more props · less need for custom Metaschema extensions or bespoke JSON."*
* **README (`README.md:63`):** 4 tests — *"simpler · closer to measured customer needs · no more props · less need for bespoke JSON"*.
* **Handbook Ch01 (`ch01-why-this-exists.md:266`):** 4 tests — *"simpler; closer to the measured needs of the customers; no more props; less need for custom meta-language extensions or bespoke JSON."*
* **Decision Register (`decision-rationale-register.md:2, 5`):** Explicitly claims **3 criteria** — *"Every decision, justified against the three north-star criteria... The three tests (session directive)."* The header groups "no more props" and "less need for bespoke JSON" under a single umbrella heading titled "Reduced complexity".

**Finding 0 Verdict:** The operative test set is **four tests**. The Decision Rationale Register header contains documentation drift (Class d) by claiming "three criteria", which conflicts with the specification, README, and handbook.

---

### B2. Operationalization of the Four Tests

Using exclusively in-repo artifacts, the four North Star tests are operationalized as follows:

1. **Test 1: Simpler**
   * *Met (measured):* Schema count reduced from 8 deep document models to 1 unified kernel schema with 9 shallow object types; 0 document-tree conventions.
   * *Met (designed-for):* Concept inventory learnable in days; weekend validator implementation.
   * *Not demonstrated:* LoC/contributor-hour comparison vs OSCAL 1.2.2 validator (deferred to v0.6 gate IV.5 item 4).
   * *Violated:* Concept inventory requires 2 digest domains, JCS pre-normalization, modality partial order evaluation, calendar fail-closed arithmetic, and bi-modal attestation state machine.

2. **Test 2: Closer to measured customer needs**
   * *Met (measured):* 100% representation of all 3 census corpora (AU.ISM, geman.bsi, FedRAMP-CR26) with zero unexplained fields.
   * *Met (designed-for):* Designed for NIST 800-53 catalog, CSF 2.0, CIS Controls, SCF mappings.
   * *Not demonstrated:* Full NIST lifecycle round-trip (SSP/AP/AR/POA&M/Mapping); unconverted NIST 800-53 catalog/baselines.
   * *Violated:* Any kernel field with zero measured customer need in the census (audit: `title` on Requirement, `label` on base objects — taste/convenience items).

3. **Test 3: No more props**
   * *Met (measured):* Over 70% of counted prop instances across census corpora (5,301 ISM applicability props, 12,059 BSI props) eliminated into kernel mechanisms (RequirementSet, `statements[]`, `modality`, `parameters`).
   * *Met (designed-for):* Registered facets replace untyped props with schema-pinned extensions.
   * *Not demonstrated:* Complete elimination of escape hatches; 539 L2 `oscal-1x@1` compat props remain in AU.ISM.
   * *Violated:* `annotations` dictionary and `facets` payload validation vacuum allow untyped/invalid key-value smuggling.

4. **Test 4: Less need for bespoke JSON**
   * *Met (measured):* FedRAMP CR26 (bespoke JSON) converted 100% losslessly into 292 Requirements, 373 Mappings, 91 Sets, 4 Tailorings.
   * *Met (designed-for):* Standardized kernel absorption of multi-framework rules, KSIs, and crosswalks.
   * *Not demonstrated:* Adoption of Semantic Core by an authority currently publishing bespoke JSON.
   * *Violated:* Unaddressed ODP/CTL addressing (backlog #10) forcing external overlays into L2 residue.

---

### B3. Verdict Table

| North Star Test | Verdict (Tier) | 3 Strongest Supporting Facts | 3 Strongest Opposing Facts |
|---|---|---|---|
| **1. Simpler** | **Met (designed-for)** | 1. 9 shallow types replace 8 deep document models (`v0.5-spec.md:464`).<br>2. 1 JSON serialization replaces Metaschema XML/YAML/JSON triple-pipeline (`D1`).<br>3. 0 profile-resolution merge strategies or positional JSON Patches (`D13`). | 1. Implementable in days is *hypothesized* with 0 in-repo time measurements (`ch01.md:263`).<br>2. Requires 2 digest domains, JCS empty-omission rules, and calendar fail-closed arithmetic (`D3`, `D9`).<br>3. Set indirection requires multi-object graph traversal for deep taxonomies (`D21`). |
| **2. Closer to measured customer needs** | **Met (measured)** for census;<br>**Not demonstrated** for NIST | 1. 3/3 census corpora converted 100% losslessly (ISM 36,161/36,161; BSI 49,431/49,431; CR26 7,294/7,294 leaf values) (`README.md:113`).<br>2. `modality` lattice directly absorbs BSI `modal_verb` (x1,006) and CR26 `force` (x328) (`v0.5-spec.md:77`).<br>3. `Mapping` kernel type absorbs CR26 263 KSI mappings and SCF crosswalk demand (`D20`). | 1. NIST 800-53 catalog and baselines remain unconverted (`v0.5-spec.md:641`).<br>2. NIST full lifecycle (SSP/AP/AR/POA&M) is *not yet demonstrated* (`v0.5-spec.md:643`).<br>3. ISO management-system clauses and PCI customized approaches are explicitly non-covered (`D17`). |
| **3. No more props** | **Met (measured)** | 1. 5,301 ISM membership props eliminated into `RequirementSet` (`D13`, `D21`).<br>2. 12,059 BSI prop instances eliminated into kernel statements/modality (`D9`).<br>3. 216 pseudo-placeholders rendered unrepresentable by `{param:}` tokens (`D9`). | 1. P9-1 demonstrated that invalid/unregistered facet payloads bypass validation (`validate_core.py:225`).<br>2. `annotations` remains an unvalidated arbitrary key-value dictionary (`schema:65`).<br>3. 539 L2 `oscal-1x@1` compat props remain in AU.ISM bundle (`ism-coverage-report.md:22`). |
| **4. Less need for bespoke JSON** | **Met (measured)** | 1. FedRAMP CR26 (bespoke JSON) converted 100% losslessly into 760 kernel objects (`README.md:118`).<br>2. Convergent evolution proved: CR26 typed fields (`force`, `affects`) match BSI prop semantics 1-to-1 (`ch01.md:149`).<br>3. `Mapping` kernel type eliminates custom mapping spreadsheets (`D20`). | 1. No authority has yet adopted Semantic Core over minting bespoke JSON (`hypothesized`).<br>2. CTL/ODP addressing (79 overlays) currently parked in L2 residue awaiting NIST conversion (`backlog:11`).<br>3. Localized text handling remains inconsistent across fields (backlog #12). |

---

### B4. The Gap List

The following quotes highlight locations where the document claims exceed demonstrated evidence tiers:

1. **`semantic-oscal/references/ch01-why-this-exists.md:263`**
   > *"And all of it would have to be implementable by a competent developer in days, in any language, offline..."*  
   *Gap:* Claimed tier: *measured/designed-for*. Actual tier: **hypothesized**. No contributor timer or LoC measurement vs OSCAL 1.2.2 exists in-repo.

2. **`README.md:120`**
   > *"Validation corpora (converted 2026-07-21; the model held without kernel changes)..."*  
   *Gap:* Claimed tier: *measured*. Actual tier: **inflated / inaccurate**. Parameter `label` and `default` were added to the kernel schema (D9 rev) on 2026-07-21 specifically to absorb parameters from DE.C3A and BSI.

3. **`drafts/oscal-semantic-core-v0.5-specification.md:641`**
   > *"NIST 800-53 / 800-171: Designed-for (D11 + sets/tailoring)"*  
   *Gap:* Claimed tier: *designed-for*. Actual tier: **not demonstrated**. The NIST 800-53 catalog and baselines have not been converted into a bundle in `converted_examples/`.

4. **`README.md:95`**
   > *"validates all nine corpus bundles green: 5,478 objects..."*  
   *Gap:* Claimed tier: *measured*. Actual tier: **inflated**. Recomputation proves 5,470 compliance objects across 8 corpus bundles; 5,478 was obtained by miscounting the 8 `content-manifest.json` header files.

---

### B5. Falsification Plan

For each test not yet met at tier *measured*, the following concrete experiments will settle the claim:

1. **Test 1 (Simpler): The Independent Validator LoC Experiment**
   * *Vehicle:* Implement a minimal Portable-tier validator in a second language (e.g., Rust or Go) following Chapter 12.
   * *Quantities to Record:* Lines of Code (excluding whitespace/comments), number of external dependencies, implementation time in hours, and pass rate on the 54 conformance vectors.
   * *Passing Threshold:* < 500 LoC, 0 non-standard dependencies beyond JCS/JSON-Schema, < 16 implementation hours.

2. **Test 2 (Closer to customer needs): The NIST 800-53 & SSP Conversion Gate**
   * *Vehicle:* Execute the gate 3 conversion of NIST SP 800-53 Rev 5 catalog, Moderate/High baselines, and 1 representative FedRAMP SSP.
   * *Quantities to Record:* Total leaf values converted, leaf values requiring L2 residue, unrepresentable statement structures, and execution time.
   * *Passing Threshold:* 100% leaf coverage with 0 kernel schema modifications and 0 unresolved statement references.

3. **Test 4 (Less bespoke JSON): The Independent Authority Adoption Test**
   * *Vehicle:* Submit converted Semantic Core representations of CR26 and BSI to respective technical working groups.
   * *Quantities to Record:* Number of bespoke fields required outside kernel+stdlib, number of schema extension proposals required.
   * *Passing Threshold:* 0 bespoke top-level fields required; 100% absorption via stdlib facets or kernel objects.

---

## Appendix A: Examined, No Finding

* **Stage 0 (Orientation & Canonical Formulation):** Recomputed all front-door document counts and verified North Star formulations across README, Spec, Register, and Handbook Ch01. (Drift recorded as Finding P9-0).
* **Stage 1 (Normative Core):** Read `drafts/oscal-semantic-core-v0.5-specification.md` and `drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md`. Verified sequencing of v0.6 cycle decisions (D22, D9 rev, D10 rev, D13 rev, D20/21 rev).
* **Stage 2 (Handbook):** Inspected `semantic-oscal/references/` ch01–ch15 and Appendices A, B, C, D, F, G. Checked promises against normative spec text.
* **Stage 3 (Executables vs Prose):**
  * Checked `oscal-semantic-core-1.0.0.schema.json` field-by-field against Appendix A shapes.
  * Audited 54 conformance vectors in `semantic-oscal/conformance/` (JCS, modality, parameter, tailoring, attestation).
  * Executed `validate_core.py` under `uv run --with jsonschema` (ALL GREEN confirmed on shipped bundles).
  * Constructed 5 adversarial objects (`scratch/test_adversarial.py`); demonstrated facet validation vacuum (P9-1) and scope validation vacuum (P9-4).
  * Recomputed converted example counts across 8 bundles (P9-6).
* **Attack Surface 8 (Next-Format Problem / Standards Proliferation):** Audited Appendix F Q1/Q2 answers against repo evidence. Verified that kernel convergence across 3 national authorities provides empirical support against the standards-proliferation objection.
* **Attack Surface 9 (Identity & Lifecycle under Adversity):** Inspected URI handling (D2), `canonical-alias` vs `replaces`, and sealed mode (D3). Confirmed normative mechanics prevent silent URI alias substitution corruption.
* **Attack Surface 10 (Digest Scope & Canonicalization Edge Cases):** Audited JCS pre-normalization (D3.3), decimal canonical strings, and DSSE attestation manifest exclusion. Confirmed two-digest domain model eliminates attestation hash cycles.
* **Attack Surface 11 (Modality Lattice vs Legal Meaning):** Evaluated modality partial order (`modality-monotonic`) including German *DARF NUR* (`may-only`). Confirmed lattice ordering correctly restricts permission without violating jurisdictional force.
* **Attack Surface 12 (Tailoring / Supplement Composition):** Inspected ordering of `operations[]` in `Tailoring`, shadow sets in supplement pattern (D21), and same-target error rule. Confirmed composition is deterministic and vector-tested.
* **Attack Surface 13 (Migration & Consumption Reality):** Audited `convert_ism.py`, `convert_bsi.py`, `convert_cr26.py`. Verified source→core coverage reports and confirmed core→source export is correctly scoped as transition tooling (D16).

---

## Appendix B: Pending Online Verification

1. **NIST OSCAL 1.2.2 Release & Control Mapping Model (March 2026):** Spec line 11 and D20 cite NIST's official release of OSCAL 1.2.2 and its Control Mapping Model in March 2026. *[needs online verification]*
2. **FedRAMP RFC-0024 (January 2026):** Handbook Ch01 citing FedRAMP RFC-0024's 2025 Rev5 authorization statistics (100+ Rev5 authorizations, 0 OSCAL submissions). *[needs online verification]*
3. **BSI Grundschutz++ v2026-07-16 Release:** Census figures citing 998 controls and 12,059 prop instances in German BSI Grundschutz++ catalog. *[needs online verification]*

