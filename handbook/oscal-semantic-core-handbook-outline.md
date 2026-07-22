# The OSCAL Semantic Core Handbook — Chapter Outline (v1 plan)
### Companion to specification v0.5 · 2026-07-18

**Purpose.** The specification says *what is normative*; the handbook says
*how to work*. Written after v0.5, updated at the v0.6 executable gate with
measured numbers and real converter output. Audience tags: **[A]**uthority
/ framework author · **[T]**ool implementer · **[C]**onsumer (GRC,
assessors, CISOs) · **[all]**.

Style rules for the whole book: every chapter opens with a task the reader
actually has; every concept is introduced through one of the three measured
corpora (ISM, BSI, CR26) before it is generalized; every "don't" names the
failure it prevents (with the census number where one exists); no chapter
may introduce a concept the specification does not define.

---

## Part One — Orientation

**1. Why this exists [all]**
The adoption evidence in one chapter: RFC-0024's zero-of-100, the props
census (12,059 / 7,759 ns-qualified instances), the 216 invisible defects,
the two-layer paradox (rigid where frameworks differ, contractless where
meaning lives), and the three coping strategies (violate, flatten, route
around). Ends with the north star and the evidence-tier rule the whole
project runs on.

**2. The core in one hour [all]**
The nine types on one diagram; an ISM control as the smallest possible
example (zero facets); the reading order for the rest of the book by
audience. Includes the "what happened to catalogs, profiles, SSPs,
comp-defs, POA&Ms" translation table for OSCAL 1.x veterans.

## Part Two — Authoring content [A]

**3. Identity, versions, and the life of an object**
Choosing and governing an authority namespace; labels and aliases;
canonical-alias vs. replaces (what rebrands may do and revisions may not);
what Authority-tier publication duties cost in practice — with ISM's
namespace as the worked positive example and the deleted FedRAMP registry
as the cautionary tale.

**4. Writing requirements: statements, modality, parameters**
Clause granularity (when one requirement carries several statements — the
BSI 347-nested-controls lesson); the modality lattice as a decision aid,
including DARF NUR / may-only; obligated parties; typed parameters, choice
sets, elapsed vs. calendar durations and the calendar-context obligation;
prose rules, `{param:}` tokens, and why the 216-defect class can no longer
be written.

**5. Sets, hierarchy, and baselines**
Nested RequirementSets as the one taxonomy mechanism (CSF, SCF domains,
CIS, ISM classifications reproduced as examples); sequence and
presentation order; designing baselines as sets instead of inline
membership props — migrating ISM's applicability matrix as the worked
example.

**6. Tailoring without tears**
The operation vocabulary; per-operation weakening rules and when a
Deviation is required (and when deliberately not: excludes are selection);
declared tightening directions; the resolution algorithm, conflict errors,
and chaining; reproducing CR26's four class variants as Tailorings plus
the L4 all-classes view.

**7. Facets: extending without fracturing**
When data belongs in the kernel, a stdlib facet, a framework facet,
`private:`, or annotations — a decision tree with census-anchored
examples; writing and publishing a facet descriptor (schema,
`modifies-semantics`, versioning, deprecation); the gspp-taxonomy facet as
the worked framework example; what the fail-closed rule means for *your*
consumers.

**8. Mappings and crosswalks**
The Mapping object; IR 8477/OLIR relationship semantics with worked
SCF-style examples; statement-level scope; provenance, confidence, and
coexisting contradictory mappings; publishing a crosswalk corpus; import
from the 1.2.2 Mapping Model.

## Part Three — Implementation and assurance [A][C]

**9. Systems, components, and inheritance**
Components and composition; identified authorization contexts and member
scoping; the Implementation edge, per-clause responsibility, CRM patterns;
leveraged authorization and the edge-local boundary rule — a full
SaaS-on-PaaS-on-IaaS worked chain.

**10. Assessment, findings, deviations**
Assessment methods via `assessment-criteria` (including KSI-style
criteria); findings and actions; the Deviation lifecycle as the audited
weakening channel; calendar-aware deadlines in practice.

**11. Integrity, attestation, and air-gaps**
Two digest domains and what each proves; content manifests; sealed-mode
operation end to end; the bi-modal verification state machine (what a
Semantic Match tells an assessor); the DSSE profile checklist; provenance
maps; the XML transit projection for guarded networks — what is and is not
inspectable.

## Part Four — Building tools [T]

**12. Building a validator (the weekend chapter)**
Core tier step by step: schemas, manifest resolution, package digests,
structural primitives, preservation duties; then Portable: JCS, facet
validation, capability declarations and fail-closed, semantic primitives,
tailoring resolution. Ends with the acceptance-test harness and the
conformance corpus — after v0.6, this chapter carries the measured LoC and
hours.

**13. Consuming content safely**
What a Portable consumer may compute and when it must stop; handling
unknown facets, `private:`, annotations; bundle composition and pin
conflicts; rendering, templates, and the annotations-are-chrome rule;
error UX for fail-closed (turning hard stops into actionable messages).

## Part Five — Adoption

**14. Migration playbooks [A][T]**
From OSCAL 1.x (catalogs, profiles, SSPs, comp-defs, POA&Ms, Mapping
Model) with the three guarantee levels made concrete; from CR26 and other
bespoke JSON; the compatibility facet's intended half-life; round-trip
expectations and the published equivalence.

**15. Governance, conformance, and the ecosystem [all]**
Tiers and what each claim entitles a buyer to expect; the registry,
transparency log, semver and deprecation policy; stdlib ownership and the
Canonical Reference Facet arrangement; how to propose changes (primitives,
ops, code systems are versioned sets — the change process is the
anti-#2118 design); the sunset trigger and the 1.x coexistence story.

## Appendices

**A. Shapes reference** — the nine types + sub-objects, field by field.
**B. Primitives, operations, predicates** — one page each, with rationale
and failure messages.
**C. Code systems** — modality (with the lattice diagram), lifecycle,
deviation states, responsibility, mapping relationships, duration units,
confidence.
**D. stdlib facet catalog** — the eight, with schemas, examples, and the
parked candidate's status.
**E. Worked corpora** — KONF.14.1, IEC-CSO-IIR + class tailoring, an ISM
control, an SCF mapping; after v0.6: full-corpus coverage reports.
**F. Objections and answers** — the adversarial-pass FAQ: every rejected
reviewer claim with its documented reason (the "why not CEL / XML / JSON
Patch / exclude-deviations / mapping-as-facet" chapter).
**G. Glossary.**

---

*Production notes:* Chapters 3–8 are gated only on v0.5 (writable now);
Chapters 12 and Appendix E gain their numbers at the v0.6 gate; Chapter 1's
figures re-verify against sources at print time per the project's
evidence rule.
