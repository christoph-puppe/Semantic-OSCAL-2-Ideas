# OSCAL Semantic Core — v0.6 Spec-Feedback Backlog
### Consolidated open design questions from gate item 1 and the first review round · 2026-07-19

Every item carries its evidence (measured where possible), its
proposed disposition, and its source. This file is the input queue
for the v0.6 specification revision; items leave it only via a
decision recorded in the register.

| # | Item | Evidence | Proposed disposition | Source |
|---|---|---|---|---|
| 10 | **CTL/ODP addressing.** External-catalog ODP assignments (79 CTL overlays) need statement-level addresses in the NIST catalog. | 79 entries parked L2 | Resolves with the NIST catalog conversion (gate 3); then decide control-level parameters vs. statement map | CR26 converter |
| 12 | **Localized-text type for human-readable fields.** Only `statement.prose` and choice labels are `{lang: string}`; `title` (×3,041), Mapping `rationale` (×373), and most facet-payload free text are bare strings — converter payloads were internally inconsistent (BSI guidance tagged ×1,004 vs CR26 description bare ×180; ISM compat carried 300 bare `prose` beside 1,150 tagged). | Field inventory 2026-07-20 (user review) | Introduce a `text` primitive `{BCP-47: string}` for kernel human-text fields; normative facet-authoring rule: payload free text MUST be text-typed, identifiers stay strings. Payload harmonization **shipped for ISM + CR26** (2026-07-21: T(v) per converter; zero bare fields in authored payloads — remaining bare are verbatim L2 quotations, term headwords per the label rule, and stub annotations, all declared in the coverage reports; BSI rerun pending source access). Kernel `text` primitive decides at v0.6 | Review round 1, finding 3 |
| 13 | **stdlib `calendar-context` code system.** `calendar-period` computation fails closed without a resolvable calendar (D9 — correct by design), but no shared registry exists: the CR26 converter minted `us-federal` ad hoc, and cross-jurisdiction tools have no common codes to resolve against. | 16 CR26 objects carry converter-minted `calendar-ref: …/calendar/us-federal`; zero shared codes exist | Define a stdlib `calendar-context` code system (us-federal, de-bund, …) with pinned bizday/holiday semantics; `calendar-ref` values SHOULD cite it; fail-closed rule unchanged | Review round 2 (deep research), vuln 1 / rec 3 |
| 14 | **`canonical-alias` verifiability.** `canonical-alias` asserts *same content* — and content sameness is checkable (semantic digests compared modulo `id` and the alias record itself) — but no rule requires the check, so a mis-issued alias for a revision that changed meaning silently misaligns every consumer. | D2 trade-off named at v0.5 ("authorities must govern stable URIs"); the check costs one digest comparison | Normative SHOULD: a validator holding both objects verifies the same-content claim; mismatch ⇒ reported error — the rebrand assertion becomes self-policing instead of trusted | Review round 2 (deep research), vuln 3 |
| 16 | **Normative reference taxonomy (closure vs. landmark).** B.1.1 as written condemns the shipped corpus: 635+373 Mapping endpoint refs and every party URI resolve to nothing in-bundle, yet all bundles are green — the validator implements closure only for Set members (added in the P9 cycle: 14,508/14,508 close). | P9b-1 (Blocker) + P9-4; probes demonstrated | Define closure-required refs (Set members, component-ref, requirement-ref, assessment-ref, capability refs, Mapping source-scope/target-scope against in-bundle endpoints) vs. landmark refs (Mapping endpoints, party/authority URIs, external evidence); implement the taxonomy + negative vectors; decide whether parties deserve a typed home | P9 runs 1+2 |
| 17 | **Facet-payload validation + unregistered-facet fail-closed.** The kernel schema constrains facet payloads to `type: object` only; the validator checks by-statement keys but validates zero payloads against stdlib descriptors and flags zero unregistered facet URIs — an adversarial object with a corrupt payload and `unregistered-dangerous-facet@99` validates green. | P9-1 (Blocker, demonstrated); P9b-9 corner (bundles pinned pre-promotion stubs — fixed for CR26 in the P9 cycle) | Portable-tier rule executable: validate known-facet payloads against pinned descriptors; unregistered registered-space facets ⇒ dangerous-by-default handling; negative vectors | P9 run 1 |
| 18 | **Conformance coverage expansion + DSSE profile.** Seven normative subsystems have zero vectors (canonical-alias/replaces, facet fail-closed, bundle composition semver, authorization basis-ref induction, supplements non-chaining + Mapping scopes, Deviation state machine, Finding state machine); three Appendix-B items parked "at gate 2" were orphaned by its closure (B.1.3 negative corpus, B.1.8 conditional-apply, B.1.7 DSSE profile — D7 calls the DSSE profile normative; no such artifact ships); no shape-disjointness vector family. | P9-2 + P9b-7; 54→56 vectors at HEAD | Author the missing vector families; ship the stdlib DSSE profile or down-tier D7's wording; add a disjointness family | P9 runs 1+2 |
| 19 | **Tailoring tier anchor.** D13-rev binds Deviation duties to the publisher's tier, but no artifact carries the tier — vectors stipulate it as test metadata; two conformant tools can disagree on one bundle's validity. | P9b-6 (argued); register's "one question decides the duty" is unanswerable from data | Define the anchor normatively (candidates: id-prefix match against the selected Set's authority; attestation signer as the stronger anchor); vectors where tier is derived, not stipulated | P9 run 2 |
| 20 | **Relations channel coherence.** Spec D13 calls relations free/informative; B.3 computes semantics on `required` removal; App A types relation `type` as open token; schema enforces no URI shape on extensions (a typo'd base code silently becomes a carried extension); C.8 base vocabulary includes `supersedes` — the concept D2 split into canonical-alias/replaces after P7-B4 proved it unsafe. | P9b-4 (measured, three-way contradiction) | Align the D13 row with B.3/C.8; constrain extension relation types to URI shape in the schema; delete or rename C.8 `supersedes` | P9 run 2 |
| 21 | **Set addressing in operations.** Every operation requires `requirement-ref`, so Sets are unaddressable — yet the set-field whitelist includes `sequence`, which lives on Set members; ch06 §6.2 also promises a version-pin ("the specification says SHOULD") that no operation field carries. | P9b-5 (measured); whitelist now a schema enum, D13 rows added (P9 cycle) | Define Set addressing (target-ref generalization) or strike `sequence` from the whitelist; add the version-pin field or delete the ch06 sentence | P9 run 2 |
| 22 | **D22 demotion vs. closed shapes.** The anticipated-convergence path demotes after two dry cycles, but kernel shapes are closed (`unevaluatedProperties: false`) — content authored during the anticipation window becomes schema-invalid on demotion; no migration rule; not scoped to pre-1.0. | P9b-10 (argued); latent — zero anticipated promotions shipped | Demotion auto-emits a compat facet + deprecation major, or scope the path pre-1.0 | P9 run 2 |
| 23 | **`uses-term` nearest-Set resolution.** The terminology hosting rule says "nearest hosting Set" with no distance metric or tiebreak; under the supplement pattern a Requirement can sit in two glossary-hosting Sets — two conformant tools resolve one term to two definitions. | P9b-11 (argued); collision realistic since D21 supplement pattern | Define distance (membership hops); ties ⇒ Portable-tier validation error, or explicit precedence rule | P9 run 2 |
| 15 | **Renderer-template accreditation ownership.** Template pins + digests (D7 `rendering.template-ref{id,version,digest}`) make render-tampering *detectable*, but no governance role *accredits* a template as faithfully rendering the graph — ch15 names no owner. | The rendering TCB is pinned but unowned; L4 outputs are what humans sign | Name the owner in ch15 (an authority accredits templates for its own corpora; the registry lists accredited template digests) — or record an explicit non-goal with rationale | Review round 2 (deep research), vuln 4 |

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
clause (register "D22-applied"). Numbering stays stable — closed numbers
are not reused.

**Standing rule for this file:** items enter with counts, leave with
register entries. An item that can neither be evidenced nor closed
after two gate cycles is deleted — backlogs rot like registries do.
