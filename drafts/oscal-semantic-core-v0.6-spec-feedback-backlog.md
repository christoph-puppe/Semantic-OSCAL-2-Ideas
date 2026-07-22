# OSCAL Semantic Core — v0.6 Spec-Feedback Backlog
### Consolidated open design questions from gate item 1 and the first review round · 2026-07-19

Every item carries its evidence (measured where possible), its
proposed disposition, and its source. This file is the input queue
for the v0.6 specification revision; items leave it only via a
decision recorded in the register.

| # | Item | Evidence | Proposed disposition | Source |
|---|---|---|---|---|
| 1 | **D9: scalar parameter default/display value.** String parameters have no home for label/default (BSI param labels like "regelmäßig", `values[]`). | 179 requirements in L2 `param-extras` residue | Add optional `label`/`default` to the parameter algebra; empty the residue | BSI converter |
| 2 | **D13: authority-published variant ceremony.** When the authority itself publishes per-class prose variants, is `replace-prose(substantive)+Deviation` the right liturgy, or does authority-variance deserve its own shape? | 29 variant-only rules + 5 KSI variants; 51 base-absent variant timeframes | Decide: either bless the Tailoring liturgy for authorities or add a `variants` carrier; drain the L2 payloads accordingly | CR26 converter |
| 3 | **D9: duration-union question — DEMOTED.** Initially flagged as 51 unit-class crossings; refined counting found 0 true crossings (all base-absent → item 2). | 0 measured crossings | Close unless new corpus evidence arrives; keep the unit-class boundary strict | CR26 converter (self-correction) |
| 4 | **Kernel promotion criteria — make normative.** The implicit bar (≥2-of-3 independent encodings · one shared computation · one vocabulary without flattening) is stated only in App. F Q22. | The modality-vs-objectives/evidence/levels analysis | Add as a normative rule (D1-adjacent); future "why isn't X kernel" disputes cite it | Review round 1, finding 1 |
| 5 | **Supplement pattern — name it normatively.** Shadow sets + reference-attachment replace profile add/alter; currently handbook-only (§6.A). | Multi-authority Set membership proven in bundles | Add a named pattern note to D21/D4; consider registering `supplements` as a stdlib relation type | Review round 1, finding 2 |
| 6 | **Terminology hosting shape.** Converter hosts the glossary on the corpus root Set (`glossary-info` block); alternative: a dedicated carrier object. | 75 terms / 188 aliases / 264 refs, all resolving | Decide root-hosting vs. carrier at schema time (gate 2); either way, document | CR26 converter |
| 7 | **`by-statement` keying convention.** All per-clause facet payloads use `by-statement:{sid:…}` — converter-established, spec-silent. | 1,015 statements' payloads across 6 facets | Make the keying pattern normative in facet-authoring guidance | BSI converter |
| 8 | **Declaration audit promotions.** Shipped stubs declare `[]` conservatively; corpora argue for: security-objectives → `[selection]`?, effectivity → `[selection]`?, reporting-obligation → `[assessment]`? (`cr26/scope@1` is the exemplar that already earns `[selection]`.) | App. D.12 table | Decide per facet with the normative schemas (gate 2) | App. D audit |
| 9 | **Seed code-set confirmation.** Finding states and assessment results are deliberately small seed sets. | Lifecycle corpus pending | Confirm/extend with gate-3 evidence; resist state-zoo growth | App. C.3/C.10 |
| 10 | **CTL/ODP addressing.** External-catalog ODP assignments (79 CTL overlays) need statement-level addresses in the NIST catalog. | 79 entries parked L2 | Resolves with the NIST catalog conversion (gate 3); then decide control-level parameters vs. statement map | CR26 converter |
| 11 | **Grammar-prop completeness as source QA.** 9 clauses carry MUSS in prose without `modal_verb` (grammar coverage 99.1 %). | Measured; queued with the 216 | Not a spec change — feeds the authors' queue (BSI#58 companion) | App. E.1 |

**Standing rule for this file:** items enter with counts, leave with
register entries. An item that can neither be evidenced nor closed
after two gate cycles is deleted — backlogs rot like registries do.
