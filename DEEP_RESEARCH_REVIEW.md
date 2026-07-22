# Comprehensive Deep Research & Technical Review: Semantic OSCAL (v0.5 Specification)

**Date:** 2026-07-21  
**Repository:** [Semantic-OSCAL-2-Ideas](https://github.com/christoph-puppe/Semantic-OSCAL-2-Ideas.git)  
**Target Specification:** OSCAL Semantic Core v0.5 normative draft  

---

## Executive Summary & Verdict

**Verdict:** **Pre-1.0 (v0.5 Specification), Evidence-Gated, High Technical Viability.** 

The **OSCAL Semantic Core** specification presents a rigorously engineered, empirically validated alternative to the legacy OSCAL 1.x architecture. By replacing **eight deep, nested document models** with a **graph of nine shallow, globally identified kernel objects**, the project directly resolves the defining paradox of OSCAL 1.x: *rigidity where frameworks legitimately differ, and contractlessness where semantic meaning lives*.

### Key Strengths & Achievements
1. **Empirical Rigor**: Unlike legacy standards designed via committee consensus, every normative primitive traces directly to a measured failure or quantitative requirement across **8 converted corpora** (93,259 values, 0 unexplained fields).
2. **Elimination of "Props" Pathology**: Replaces over 22,000 unvalidated, schema-less `props` across ACSC ISM, BSI Grundschutz++, and FedRAMP CR26 with typed kernel primitives and registered facets.
3. **Cryptographic Integrity Realism**: Solves signature breakage from legitimate repackaging via a **dual-digest architecture** (`package-digest` vs. `semantic-digest`) and bi-modal verification (*Full Match* vs. *Semantic Match*).

### Primary Gaps to Reach 1.0 (v0.6 Executable Gate)
- Executable JSON Schemas (Draft 2020-12) and the lines-of-code benchmark comparing a Semantic Core validator against an OSCAL 1.x validator ("the weekend validator test") remain the primary pending deliverable.

---

## Deep-Dive Section Findings

### 1. Architectural & Graph Model Integrity

#### Kernel vs. Document Model ([drafts/oscal-semantic-core-v0.5-specification.md](drafts/oscal-semantic-core-v0.5-specification.md))
- **9 Kernel Types**: `Requirement`, `RequirementSet`, `Tailoring`, `Mapping`, `Component`, `Implementation`, `Assessment`, `Finding`, `Attestation` (plus `Deviation` & `Authorization` sub-objects).
- **Documents as Renderings (L4)**: Replaces deep document trees with flat records linked via global URIs. Documents (e.g., SSPs, SARs, Catalogs) become presentation-layer views generated from graph queries rather than transport units.
- **Elimination of Profile Merge Algebra**: Eliminates OSCAL 1.x profile resolution, inheritance cascades, and positional JSON Patch fragility. Tailoring operations (`set-modality`, `set-parameter`, `replace-prose`, `detach-facet`, `excludes`) use **identity addressing** (`requirement-ref` + `statement-id`), making overrides deterministic and reordering-resistant.

#### Three-Layer Separation ([drafts/oscal-semantic-core-decision-rationale-register.md](drafts/oscal-semantic-core-decision-rationale-register.md))
```
+-----------------------------------------------------------------------+
|  Kernel (Normative, Fixed)                                           |
|  Modality, statements, typed parameters, membership, history, mapping |
+-----------------------------------------------------------------------+
|  Facets (Registered, Schema-Pinned, Fail-Closed)                      |
|  security-objectives@1, assessment-criteria@1, terminology@1, etc.   |
+-----------------------------------------------------------------------+
|  Annotations (Non-normative Chrome)                                   |
|  Rendering hints (e.g., do_not_link), web navigation, UI metadata     |
+-----------------------------------------------------------------------+
```
- **Passive Core vs. Fail-Closed Portable Tier (D15)**: The **Core** tier is strictly passive—it validates kernel schema, verifies package digests, resolves local references, and *preserves unknown facets without evaluating compliance math*. All semantic evaluations begin at the **Portable** tier, where missing capability declarations or unhandled semantics fail closed.

#### Identity & Addressing Split (D2, D5)
- **URI Equality**: Identity URIs are string-compared opaque tokens (never dereferenced over network), enabling 100% offline verification in air-gapped environments.
- **Alias vs. Lineage Split**:
  - `canonical-alias`: Identity equivalence (authority-asserted rebrands, safe auto-substitution).
  - `replaces[]`: Lineage history (`revised`, `split-from`, `merged-into`). Auto-substitution is explicitly forbidden to prevent silent corruption of attestations and findings.
- **Authorization Scoping**: System boundaries attach via `authorizations[]` with explicit `includes[]` component scoping, and inheritance edges carry a required `basis-ref` pointing to a specific `authorization-id`.

---

### 2. Empirical Evidence & Corpus Validation

#### Coverage Analysis across 8 Corpora ([converted_examples/](converted_examples/))

| Corpus / Authority | Source Version | Inventoried Leaf Values | Mapped Values | UNMAPPED | Coverage % | Key Emitted Objects | Coverage Report Link |
|---|---|---|---|---|---|---|---|
| **AU.ISM** | v2026.06.18 | 36,161 | 36,161 | 0 | **100.0%** | 1,150 Reqs, 322 Sets | [ism-coverage-report.md](converted_examples/AU.ISM/ism-coverage-report.md) |
| **BE.CyFun** | v2025-12-12 | 4,312 | 4,312 | 0 | **100.0%** | 218 Reqs, 124 Sets | [cyfun-coverage-report.md](converted_examples/BE.CyFun/cyfun-coverage-report.md) |
| **CIS.Controls** | v8.1 | 5,493 | 5,493 | 0 | **100.0%** | 171 Reqs, 34 Sets | [cisc-coverage-report.md](converted_examples/CIS.Controls/cisc-coverage-report.md) |
| **CIS.Ubuntu2404** | v1.0.0 | 20,698 | 20,698 | 0 | **100.0%** | 312 Reqs, 635 Mappings, 79 Sets | [cisb-coverage-report.md](converted_examples/CIS.Ubuntu2404/cisb-coverage-report.md) |
| **DE.C3A** | v1.0 | 1,093 | 1,093 | 0 | **100.0%** | 30 Reqs, 9 Sets | [c3a-coverage-report.md](converted_examples/DE.C3A/c3a-coverage-report.md) |
| **DE.C5** | vC5:2026 | 5,868 | 5,868 | 0 | **100.0%** | 623 Reqs, 190 Sets | [c5-coverage-report.md](converted_examples/DE.C5/c5-coverage-report.md) |
| **FedRAMP CR26** | v2026.07.14.01 | 7,294 | 7,294 | 0 | **100.0%** | 292 Reqs, 373 Mappings, 91 Sets, 4 Tailorings | [cr26-coverage-report.md](converted_examples/FedRAMP-CR26/cr26-coverage-report.md) |
| **geman.bsi** (GS++) | v2026-07-16 | 49,431 | 49,431 | 0 | **100.0%** | 651 Reqs (999 statements), 162 Sets | [bsi-coverage-report.md](converted_examples/geman.bsi/bsi-coverage-report.md) |

#### Props Elimination Mechanism ([drafts/prop-census-three-authorities-v0.3-input-r2.md](drafts/prop-census-three-authorities-v0.3-input-r2.md))
Over **70% of legacy OSCAL prop instances** disappear with zero replacement construct because they were workarounds for missing core primitives:
- **Membership Matrices** (5,301 ISM props) → `RequirementSet` membership.
- **Modality & Binding Force** (`modal_verb` ×1,006, `force` ×328) → `statements[].modality` lattice.
- **Revision History** (2,202 ISM props, CR26 `updated[]`) → Native L0 versioning.
- **Nested Controls** (347 pseudo-controls in BSI) → `statements[]` collection.

#### Exposure of Source Defects (Not Hidden in Props)
- **BSI Grundschutz++**: Identified 213 `{{...}}` pseudo-placeholders in prop values as authoring defects and reported them in [bsi-coverage-report.md](converted_examples/geman.bsi/bsi-coverage-report.md) without silent laundering.
- **CIS Ubuntu Benchmark**: Identified empty statement prose across all 312 rules; statement prose was explicitly minted from titles and flagged in [cisb-coverage-report.md](converted_examples/CIS.Ubuntu2404/cisb-coverage-report.md).

---

### 3. Cryptographic Integrity & Dual-Digest Model

#### Dual-Digest Architecture ([semantic-oscal/references/ch11-integrity-attestation-airgaps.md](semantic-oscal/references/ch11-integrity-attestation-airgaps.md))
Legacy OSCAL digital signatures fail when transport tools strip non-normative metadata or format JSON. Semantic OSCAL introduces two distinct SHA-256 digest domains per object in `content-manifest.json`:
1. `package-digest`: SHA-256 over raw delivered bytes (includes annotations and formatting).
2. `semantic-digest`: SHA-256 over canonical **JCS** (RFC 8785) serialization of the object **excluding `annotations`**.

```
                           +------------------------+
                           |  Delivered Object      |
                           +-----------+------------+
                                       |
                   +-------------------+-------------------+
                   |                                       |
                   v                                       v
         [ Raw Bytes ]                             [ Exclude Annotations ]
                   |                                       |
                   v                                       v
        package-digest SHA-256                    JCS Pre-Normalization
                   |                                       |
                   v                                       v
        (Package Integrity)                      semantic-digest SHA-256
                                                           |
                                                           v
                                                 (Normative Integrity)
```

#### Bi-Modal Verification State Machine (D7)
- **Full Match**: Signature valid AND `content-manifest-digest` matches bundle. Proves exact byte-for-byte state as signed.
- **Semantic Match**: Signature valid AND all `subject-semantic-digests` match, but `content-manifest-digest` differs. Proves compliance meaning is 100% untampered, even if chrome/annotations were stripped in transit.
- **Failed**: Any signature mismatch or semantic digest discrepancy.

#### Out-of-Band Attestation & Air-Gap Support
- **Cycle-Free Signatures**: Attestations and DSSE envelopes sit **beside** `content-manifest.json`, eliminating the self-referential hashing cycle.
- **Sealed Mode**: Manifests pin exact facet schemas (URI + SHA-256 digest). Core validators operate fully offline without external network or DNS resolution.

---

### 4. Migration Path & Ecosystem Viability

#### 3-Level Migration Guarantee Framework ([semantic-oscal/references/ch14-migration-playbooks.md](semantic-oscal/references/ch14-migration-playbooks.md))
1. **Level 1: Native Mapping**: Direct 1-to-1 representation in kernel objects.
2. **Level 2: Compatibility Facet**: Framework-specific properties preserved in registered compatibility facets with a clear deprecation clock.
3. **Level 3: Opaque Preservation**: Preserved in `private:` annotations to prevent compliance math corruption while preserving raw data.

#### Bidirectional Migration & Export Feasibility
- **Up-conversion**: 100.0% proven across 8 corpora representing catalogs, benchmarks, and bespoke JSON.
- **Down-conversion**: Semantic Core objects compile back to syntactically valid OSCAL 1.2.2 JSON/XML for legacy regulatory submission while keeping Semantic Core as the single-source-of-truth graph.
- **Profile Merge Semantics Gap**: Profiles depending on legacy OSCAL 1.x `use-first`/`combine` merge strategies must be resolved in 1.x *before* migration into Semantic Core ([ch14-migration-playbooks.md](semantic-oscal/references/ch14-migration-playbooks.md)).

---

### 5. Adversarial Stress-Testing & Open Flaws

#### Resolved Issues (Review Passes & Backlog Closures)
- **Manifest Hash Cycle (P7-B1)**: Resolved by placing attestations outside the content manifest (D3).
- **Core Passive Tier (P7-B3 / P8-E1)**: Resolved by forbidding semantic computation at Core tier (D15).
- **Modality Partial Order (P8-E2)**: Resolved by defining a normative partial order lattice supporting obligations, prohibitions, restrictions (`may-only` / `DARF NUR`), and unmonotone moves requiring a `Deviation` (D9).
- **Kernel Promotion Bar (D22)**: Established normative rules requiring ≥ 2-of-3 census authority encodings, shared computation, and non-flattening vocabulary before any candidate enters the kernel.

#### Active Open Backlog Items ([drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md](drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md))
- **Item #6 (Terminology Hosting Shape)**: Re-scoped under D22 anticipated-convergence path. Pending decision on dedicated carrier object vs. root-Set hosting.
- **Item #10 (CTL/ODP Addressing)**: Statement-level addresses for 79 CTL overlays to resolve during the NIST catalog conversion.
- **Item #12 (Localized-Text Primitive)**: Defining `text` (`{BCP-47: string}`) for human-readable fields (`title`, `rationale`) to replace inconsistent string definitions across converted corpora.

---

## Critical Vulnerabilities & Blindspots

1. **Calendar Dependency in Deadline Arithmetic (D9)**:
   - *Risk*: `calendar-period` (e.g., `3 bizdays`) relies on external holiday/business calendars.
   - *Consequence*: Without a resolved calendar context, deadline evaluation MUST fail closed. Tools operating in different jurisdictions without explicitly attached calendar references will halt.
2. **Third-Party Facet Diode Inspection (D18)**:
   - *Risk*: Strict XML transit projection (XSD inspection at cross-domain guards) only covers kernel + `oscal-stdlib`.
   - *Consequence*: Third-party custom facets pass through guards as opaque payloads, requiring custom guard policies per facet publisher.
3. **Over-Reliance on Authority Diligence for Alias Rebrands (D2)**:
   - *Risk*: `canonical-alias` allows tools to auto-substitute control identifiers.
   - *Consequence*: If an authority incorrectly issues a `canonical-alias` for a control revision that actually altered normative requirements, consumer implementations will be silently misaligned.

---

## Actionable Recommendations for v0.6 Specification Cycle

### Priority 1: High Impact / Immediate
1. **Deliver the Executable v0.6 Proof Gate**:
   - Complete normative JSON Schemas (2020-12) for all 9 kernel objects and stdlib facets.
   - Conduct the lines-of-code / contributor-hour benchmark comparing a Semantic Core validator against an OSCAL 1.2.2 reference validator.
2. **Formalize the `text` Primitive (Backlog Item #12)**:
   - Adopt `{ "<BCP-47-lang>": "string" }` as the normative primitive for all human-targeted fields (`title`, `rationale`, `description`) across kernel objects and registered facets.

### Priority 2: Medium Impact / Next Cycle
3. **Standardize Calendar Context Attachments**:
   - Define a standard `calendar-context` code system within `oscal-stdlib` to allow `calendar-period` deadline calculations to execute fail-closed without ambiguity in cross-jurisdictional deployments.
4. **Publish Bidirectional Export Test Suites**:
   - Create automated verification tests validating that Semantic Core graph objects compile losslessly to OSCAL 1.2.2 JSON/XML target formats.
