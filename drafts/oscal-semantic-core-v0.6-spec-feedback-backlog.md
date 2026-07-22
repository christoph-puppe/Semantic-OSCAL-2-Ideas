# OSCAL Semantic Core — v0.6 Spec-Feedback Backlog
### Consolidated open design questions from gate item 1 and the first review round · 2026-07-19

Every item carries its evidence (measured where possible), its
proposed disposition, and its source. This file is the input queue
for the v0.6 specification revision; items leave it only via a
decision recorded in the register.

| # | Item | Evidence | Proposed disposition | Source |
|---|---|---|---|---|
| 10 | **CTL/ODP addressing.** External-catalog ODP assignments (79 CTL overlays) need statement-level addresses in the NIST catalog. | 79 entries parked L2 | Resolves with the NIST catalog conversion (gate 3, see `drafts/gate-3-plan.md`); then decide control-level parameters vs. statement map | CR26 converter |
| 12 | **Localized-text type for human-readable fields — NEEDS AUTHOR DECISION.** Only `statement.prose` and choice labels are `{lang: string}`; `title` (×3,041), Mapping `rationale` (×373), and most facet-payload free text are bare strings. A `text` primitive `{BCP-47: string}` is a NEW kernel primitive touching every human-text field + all 8 converters (blast radius). Payload harmonization **shipped for ISM + CR26** (2026-07-21: T(v) per converter; remaining bare are verbatim L2 quotations, term headwords per the label rule, and stub annotations, all declared in the coverage reports; BSI rerun pending source access). | Field inventory 2026-07-20 (user review) | **Author call (register round-2 flag):** recommendation is adopt the `text` primitive (evidence supports it), but the go-ahead + BSI-rerun sequencing is the author's; not decided unilaterally | Review round 1, finding 3 |
| 18 | **Conformance coverage — gate-4 remainder.** Delivered: facet fail-closed (7), reference-taxonomy (11 incl. #14 alias), lifecycle (36), tailoring (15 incl. #25 op-law), DSSE profile (`dsse-envelope@1`). **125 vectors at HEAD** (see #28). **Remaining:** bundle-composition semver vectors (D3.5) and B.1.8 `conditional-apply` instantiation — both need the engines gate 4 builds. | P9-2 + P9b-7; delivery counted | Author the two remaining families with the gate-4 engines | P9 runs 1+2 |
| 20 | **Relations: constrain extension types to URI shape** *(round-2 partial).* Done: D13 row aligned with B.3 (`remove-relation(required) ⇒ Deviation`); C.8 `supersedes` deleted (register "C.8 rev"). Remaining: the schema types relation `type` as any non-empty string, so a typo'd base code silently becomes a carried extension (P9b-4). **Blocked on the converter rerun** migrating the corpus's bare-word `sharpens` ×28 to a namespaced URI. | P9b-4; `sharpens` ×28 measured | After the rerun: constrain extension relation `type` to a URI shape (base codes ∪ URI) in the schema; add a vector | P9 run 2 |
| 24 | **Tier: signature-verify the `authority-proven` layer** *(round-2 partial).* Done: the reference validator now reports each Tailoring's tier distinctly per spec:399 (register "D13 rev 3"). Remaining: `derive_tier` digest-matches an attestation without verifying its signature, so both authority tiers stay forgeable by a party minting under the content origin. | Demonstrated: `probe_tier.py` flips claimed→proven with a forged unsigned attestation | Verify the DSSE signature in the proven-tier check (gate-4 engine); add prefix-spoof + unsigned-attestation negative vectors | P9c run (2026-07-22), Major P9c-1 |
| 26 | **Facet enforcement: ship real pinned schemas + pin-honoring** *(round-2 partial).* Decision recorded (register "D26"): stdlib strict, non-stdlib against the pin. Remaining: bundles pin permissive illustrative stubs (`additionalProperties` defaults `true`), so framework/compat payloads are under-validated and the reference validator diverges from a pin-honoring sealed tool. | Demonstrated: `cr26/scope` stub accepts a smuggled key; stubs are ILLUSTRATIVE | **Converter rerun** ships pinned schemas with `additionalProperties:false`; fix pin-vs-descriptor precedence | P9c run (2026-07-22), Major P9c-3 |

**Closed 2026-07-21** (review round 1 decisions; register "Amendments —
v0.6 cycle" + spec changelog IV.7): **#1** → D9 rev (parameter
`label`/`default`; residue drains at next converter run) · **#2** → D13
rev (Deviation duties bind at consumption tier; authority Tailorings
exempt; `variants` carrier rejected via the D22 bar) · **#4** → **D22**
(kernel promotion rule normative) · **#5** → D20/D21 rev (supplement
pattern named; `supplements` stdlib relationship extension code) ·
**#7** → D10 rev (`by-statement` keying normative) · **#3** → closed
no-change (D9 closure note: 0 true unit-class crossings measured — the
51 first-pass flags were base-absent variants, resolved under #2's D13
rev; the elapsed/calendar unit-class boundary stays strict) · **#8** →
D10 rev 2 (declarations promoted: security-objectives/effectivity →
`[selection]`, reporting-obligation → `[assessment]`; a tool that cannot
handle a facet must stop working on that data; stubs update at next
converter run) · **#9** → closed, folded into the gate-3 scope statement
(IV.5): seed sets confirm/extend only from counted lifecycle evidence ·
**#11** → closed, delivered: reported to the BSI authors by the project
(companion to the 216/issue #58; never a spec change) · **#6** → closed
at gate 2 (2026-07-21): root-Set hosting normative in the terminology
stdlib descriptor; carrier/tenth-type rejected via the D22 absorption
clause (register "D22-applied") · **#16** → closed (2026-07-21,
register "P9-applied"): reference taxonomy normative — closure-required
(Set members, Tailoring selects/excludes/op targets + statement
existence, Implementation component/requirement + D5 basis-ref, Finding
refs, Mapping scopes when the endpoint is in-bundle) vs. landmark
(Mapping endpoints, party URIs, evidence, attestation subjects);
implemented + 9 vectors; parties stay landmark by the D22 test (0-of-3
corpora publish party objects) · **#17** → closed (2026-07-21,
register "P9-applied"): facet payloads validate against normative
stdlib descriptors or bundle-pinned schemas, `private:` ignored by
definition, unregistered ⇒ error; 7 vectors incl. the P9-1 probe; all
8 bundles green under enforcement · **#19** → closed (2026-07-21,
register "P9-applied", layered per user decision): tier DERIVED from
data — id-origin match = authority-claimed, authority Attestation over
the Tailoring (digest-verified) = authority-proven (proof beats
prefix), else consumer; duties bind at consumer tier; 8 derivation
vectors; op-duty enforcement live in bundle validation (CR26's four
class Tailorings derive authority-claimed). Numbering stays stable —
closed numbers are not reused.

**Closed 2026-07-22** (v0.6 cycle round 2; register "Amendments — v0.6
cycle, round 2" — acts on the P9c re-review + the deep-research open
items): **#13** → `calendar-context@1` stdlib code system seeded (C.9:
us-federal/de-bund/eu-target2; `calendar-ref` SHOULD cite it) · **#14**
→ canonical-alias same-content check implemented in `closure_errors` +
2 reference vectors (register "D2 rev") · **#15** → template
accreditation = declared non-goal, authority-local (register
"R6-applied") · **#21** → Sets unaddressable by operations; `sequence`
struck from the set-field whitelist (schema enum + spec D13 row +
appendix-b; register "D21 rev") · **#22** → anticipated-convergence
path scoped pre-1.0 (register "D22 rev 2") · **#23** → `uses-term`
nearest-Set = fewest membership hops, ties ⇒ Portable-tier error
(register "D22-applied rev") · **#25** → op-law completed for
`set-parameter` bounds/tightening + `remove-relation(required)` in
`tailoring_duty_errors` + 6 tailoring vectors (register "D13 rev 3") ·
**#27** → decimal no-leading-zeros + scale-significance clarified
(schema pattern + spec D3 rev) + 2 parameter vectors · **#28** → count
erratum applied (README + spec → 125; recompute via
validate_core.py). Conformance grew 115 → **125 vectors**.
**Partials (stay open above, narrowed):** #20 (schema URI-shape for
`sharpens` awaits the converter rerun), #24 (signature verification of
the proven tier awaits the gate-4 DSSE engine), #26 (real pinned
schemas + pin-honoring await the converter rerun). **Still open:** #10
(gate 3), #12 (kernel `text` primitive — needs author decision), #18
(gate 4). Numbering stays stable — closed numbers are not reused.

**Standing rule for this file:** items enter with counts, leave with
register entries. An item that can neither be evidenced nor closed
after two gate cycles is deleted — backlogs rot like registries do.
