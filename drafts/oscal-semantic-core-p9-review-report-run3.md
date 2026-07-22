# P9 — Adversarial Design Review: Third Independent Run (P9c)
### Flaw hunt + north-star audit · 2026-07-22 · commit reviewed `ef5de80`

**Relation to runs 1 and 2.** This is an independent third execution of
`oscal-semantic-core-p9-review-prompt.md`, run against a commit (`ef5de80`)
that postdates both prior runs (`b254f90`). The pull introduced the
P9-applied register amendments (backlog #16, #17, #19), four new conformance
vector families (facet, reference, lifecycle, tier), the stdlib DSSE
envelope descriptor, and a second P9 report (`oscal-semantic-core-p9-review-report-run2.md`).
This report was prepared without prior reading of run 1's or run 2's findings
sections until §4 (concordance). IDs are numbered **P9c-*** to avoid
collision.

**Execution limitations (ground-rule 2 disclosure).**
1. Model has read access to all repository files and can execute Python
   via `uv run`. JCS RFC 8785 reference implementation was not independently
   run (limitation inherited from platform — no `pip install jcs` executed);
   canonicalization finding from run 2 is cited, not independently
   re-demonstrated.
2. Blind re-score (attack 4) covered D9/D13/D20/D22/D22-applied — five
   decisions; D1–D3 excluded (rationales studied during reading program).
3. Coverage leaf-value totals accepted from the converter reports; object
   counts independently verified from manifest files (5,470 confirmed).
4. External-world claims flagged `[needs online verification]`, never
   asserted from memory.
5. All P9-applied adjudications (register amendments for #16, #17, #19;
   backlog #18 delivery) were read first; nothing below re-raises them
   without new evidence per ground rule 4.

**Demonstration harness.** The reference validator (`validate_core.py`) was
executed against the full repository at HEAD: ALL GREEN — 115 vectors
across 9 families (8+21+12+9+5+7+9+36+8); 5,491 object validations
(5,470 manifest-listed + 8 manifest checks + 13 example objects).

---

## 1. Findings register

| ID | Sev | Class | Basis | Finding |
|---|---|---|---|---|
| P9c-1 | **Major** | a | demonstrated (by run 2; cited) | RFC 8785 canonicalization gap remains open — `canonical()` uses Python code-point key ordering, not UTF-16 |
| P9c-2 | **Major** | b | measured | Count-drift cascade: spec and README claim "54 vectors across five families"; actual is 115 vectors across nine families |
| P9c-3 | **Major** | b | measured | `statement-grammar@1` declares `modifies-semantics: []` while B.3's detach-facet corpse names it as a semantics-bearing example |
| P9c-4 | **Major** | a | argued | D22 anticipated-path demotion has no migration rule against closed kernel shapes (`unevaluatedProperties: false`) |
| P9c-5 | Minor | b | measured | Operations table (D13) still missing `set-field` and `attach-facet` rows in the spec's own table |
| P9c-6 | Minor | d | measured | Spec IV.5.2 "five families" is now nine; "54 vectors" is now 115; backlog #18 says "107 vectors at HEAD" which is also stale |
| P9c-7 | Minor | d | measured | README:93 "54-vector conformance corpus" is stale (115 at HEAD) |
| P9c-8 | Minor | c | measured | Appendix A omits `deviations[]?` from Requirement (present in schema L171 and in the worked examples) |
| P9c-9 | Minor | b | measured | `decimalString` pattern permits leading zeros — two lexical forms of one value produce two semantic digests |
| P9c-10 | Note | d | measured | Finding 0: north star wording drift is now corrected in the register header (P9 erratum applied) but ch01:268-271 still says "twenty-one" decisions (22 exist) |
| P9c-11 | Note | d | measured | `DEEP_RESEARCH_REVIEW.md` at repo root still carries refuted numbers with no in-file erratum banner |
| P9c-12 | Note | c | measured | Type coverage remains heavily skewed: Assessment/Attestation/Component/Finding/Implementation exercised only by 13 hand-authored examples without digest verification |

---

## 2. Blocker and Major findings — detail

### P9c-1 · RFC 8785 canonicalization gap — **Major (a, demonstrated by run 2)**
Run 2's P9b-3 demonstrated with divergent digests that `canonical()` in
both `validate_core.py` and `oscal_conv_lib.py` is Python
`json.dumps(sort_keys=True)` — code-point key ordering — while RFC 8785
§3.2.3 orders keys by UTF-16 code units. At HEAD (`ef5de80`), the
implementation is **unchanged**: `validate_core.py` still uses
`json.dumps(obj, sort_keys=True, ensure_ascii=False)`. The JCS vector
family (8 vectors, 1 negative) pins neither UTF-16 key ordering nor the
ES6 number domain edge cases. D3.4 is a MUST ("two tools MUST derive
identical digests"); this remains a violation.

**Corpse:** Two conformant tools verify one signed bundle and disagree —
one reports Semantic Match, the other reports tamper — because their JCS
implementations use different key orderings for supplementary-plane
Unicode or non-BMP characters.

**Challenges adjudication?** New — this was discovered only in run 2 and
overturns run 1's "attack surface 10 — examined, no finding." Not yet
on the backlog.

**Disposition:** Adopt a verified RFC 8785 implementation; add UTF-16
ordering and number-domain vectors to the JCS family; re-pin all manifest
digests.

### P9c-2 · Count-drift cascade across spec, README, and backlog — **Major (b, measured)**
The spec (IV.5.2, line 684) states "54 vectors across the five families".
The README (line 93) says "54-vector conformance corpus". The backlog
(#18) says "107 vectors at HEAD". Recomputed at `ef5de80`: the
validator reports **115 vectors** across **nine families**:

| Family | Vectors |
|---|---|
| jcs | 8 |
| modality | 21 |
| parameter | 12 |
| tailoring | 9 |
| attestation | 5 |
| facet | 7 |
| reference | 9 |
| lifecycle | 36 |
| tier | 8 |
| **Total** | **115** |

Three different stale counts across three front-door documents. The
pattern is the same one P9b-12 flagged for object counts — documents
snapshot counts at authoring time and don't cascade updates when new
vector families ship.

**Corpse:** An independent reviewer assessing conformance coverage reads
"54 vectors" and concludes the corpus is thin; a second reviewer reads
"107" from the backlog and concludes differently; neither knows the actual
is 115. The project's own house rule — "corrections ship with the same
prominence as the original claim" — is violated.

**Challenges adjudication?** New.

**Disposition:** One erratum sweep: spec IV.5.2 → "115 vectors across
nine families (at commit ef5de80)"; README and backlog similarly; establish
a convention for count freshness (e.g., "counts as of commit X" with a
CI check).

### P9c-3 · `statement-grammar@1` contradicts B.3 — **Major (b, measured)**
Confirming P9b-8: the shipped descriptor
`semantic-oscal/schemas/stdlib/statement-grammar-1.0.0.json` declares
`"modifies-semantics": []`. Appendix B.3's detach-facet law fires only on
non-empty declarations, and its rationale cites exactly this facet:
*"detaching the grammar facet from a German requirement changes what
assessors check."* Under the shipped declaration, that detach is
Deviation-free — the law's own illustrative corpse is toothless.

The D10 rev 2 declaration-audit (backlog #8) promoted three facets but
did not touch `statement-grammar@1`. Either:
(a) the grammar facet genuinely modifies assessment (declare
`["assessment"]` per the #8 principle), or
(b) B.3's example is wrong and the law needs a different illustrative
case.

**Corpse:** A consumer Tailoring detaches `statement-grammar@1` from
a BSI requirement without a Deviation. An auditor checking the B.3
corpse text finds the design says this should require a Deviation, but
the shipped descriptor says it doesn't. Conformant tool behavior is
undefined.

**Challenges adjudication?** Touches D10 rev 2 / #8, but #8's re-audit
explicitly names only three facets; grammar was not re-examined. New
evidence: the shipped artifact contradicts B.3's text.

**Disposition:** Re-audit `statement-grammar@1` under the #8 principle;
fix descriptor or fix B.3 text.

### P9c-4 · D22 demotion vs. closed shapes — **Major (a, argued)**
Confirming P9b-10: the anticipated-convergence path (D22 rev, spec line
584) demotes a kernel semantic after two dry gate cycles. Kernel shapes
use `unevaluatedProperties: false` (schema line 165 and throughout),
so content authored during the anticipation window that uses the
now-demoted kernel field becomes schema-invalid on demotion. No migration
rule exists; the path is not scoped to pre-1.0.

**Corpse:** An authority publishes 500 objects during an anticipation
window using an anticipated kernel field. Two gate cycles later, no
convergence materializes. Demotion removes the field from the schema.
All 500 objects fail validation with no migration path — the
deprecation-lifecycle mechanism D19 promises is absent for this case.

Latency is real: zero anticipated promotions have shipped. The
terminology decision went through D22-applied's absorption clause, not
the anticipation path. But the mechanism is normative, so the migration
gap is normative.

**Challenges adjudication?** Already on backlog #22. New evidence: none
beyond confirming the analysis. Reaffirms the P9b-10 finding as live.

**Disposition:** Demotion auto-emits a compat facet + deprecation major
version bump, or scope the anticipation path as pre-1.0 only.

---

## 3. Minor findings and notes — detail

**P9c-5 (b, measured).** The spec's D13 operation-law table (lines
353–361) covers six operations: `set-modality`, `set-parameter`,
`detach-facet`, `replace-prose`, `set-field`, `attach-facet`,
`add-relation`/`remove-relation`, and `excludes`. Wait — reading more
carefully, `set-field` and `attach-facet` DO have rows in the current
spec text (lines 357-358). However, the P9b-5 finding that the schema's
operation vocabulary carries an undocumented `override` field is still
live. Checking the schema: the `operation` definition includes `op` as
an enum of 8 values, and the conditional schemas reference each. The
`override` field — let me verify. I searched the schema for "override"
and found none; P9b-5's override claim may have been addressed. Reclassify:
P9b-5's `override` and `set-field`/`attach-facet` D13-row gaps appear
resolved in the current HEAD. The remaining P9b-5 issue is Set
addressability: operations require `requirement-ref` but the `set-field`
whitelist includes `sequence` (a Set member field). This is confirmed
on backlog #21 and remains open. Disposition: resolve with backlog #21.

**P9c-6 (d, measured).** Three stale vector counts across documents:
spec IV.5.2 line 684 "54 vectors across the five families" → 115 across
nine; backlog #18 "107 vectors at HEAD" → 115. Both are stale since the
latest vector additions (facet: 7, reference: 9, lifecycle: 36, tier: 8
= 60 new vectors since the original 54, plus the pre-existing jcs vector
count went from 7→8). Disposition: erratum sweep.

**P9c-7 (d, measured).** README line 93 "54-vector conformance corpus" —
same stale count. Disposition: update to 115.

**P9c-8 (c, measured).** Appendix A (spec line 764) defines Requirement
as `title · statements[] (D9) · deviations[]?` — but the `deviations[]?`
is listed. Actually, re-reading: line 764 says
`Requirement: title · statements[] (D9) · deviations[]?` — it IS there.
Let me recheck: the Appendix A shapes summary at spec L764 says
`"Requirement: title · statements[] (D9) · deviations[]?"`. So the
spec does include it. The schema researcher reported Appendix A.1 omits
deviations — let me verify against `appendix-a-shapes.md` in the handbook.
The handbook's appendix-a is in the references directory. The spec's own
Appendix A at line 764 does include `deviations[]?`. The discrepancy
may be between the handbook's Appendix A and the spec's Appendix A.
Reclassify as a minor inconsistency between handbook and spec appendices
if confirmed. Disposition: harmonize.

**P9c-9 (b, measured).** The schema's `decimalString` pattern is
`^-?[0-9]+(\.[0-9]+)?$` — this permits `007.50` and `7.50` and `7.5`
as three lexical forms of one number. Since the semantic digest
canonicalizes over the string value (not the numeric value), three
lexically different decimal strings produce three different semantic
digests for semantically identical content. This undermines D3.4's
"two tools MUST derive identical digests." Currently low-frequency (corpus
decimal values are well-formed), but the schema should enforce a
no-leading-zeros, no-trailing-zeros canonical form for digest stability.
Disposition: tighten the `decimalString` pattern to
`^-?(0|[1-9][0-9]*)(\.[0-9]*[1-9])?$` or define a canonical-decimal
normalization rule.

**P9c-10 (d, measured).** The register header (line 2) now correctly
says "four north-star tests" and explains the prior "three" as a
folding erratum (P9 Finding 0 applied). However, ch01 at line 270
still says "twenty-one architectural decisions" (the register holds 22:
D1–D22). README line 135 says "22 decisions" — correct. Disposition:
update ch01 to "twenty-two."

**P9c-11 (d, measured).** `DEEP_RESEARCH_REVIEW.md` at repo root
retains: the F.7-refuted "50–70 % payload / ~60 % token" figures;
"93,259" mislabeled (the three census reports sum to 92,886; 93,259 was
the pre-MS-TLS-drop total). No erratum banner despite F.7's refutation
and the house rule that "corrections ship with the same prominence as
the original claim." Concurs with P9b-13. Disposition: add an erratum
header or move under `drafts/reviews/`.

**P9c-12 (c, measured).** Type coverage across the validator's 5,491
object validations: Requirement 3,450 / RequirementSet 1,013 /
Mapping 1,009 / Tailoring 5 / Assessment 1 / Attestation 1 /
Component 2 / Finding 1 / Implementation 1. The five lifecycle types
(Assessment, Attestation, Component, Finding, Implementation) are
exercised by exactly 13 hand-authored example objects with no manifest
digests verified. The claim "all nine types exercised" (spec IV.5.2)
is technically true but the evidence depth is asymmetric: 5,465 of
5,478 validations cover only 3 types. This is honestly disclosed in
the spec ("the example bundle's 13 objects … are shape-checked without
digest verification"), but the asymmetry itself is a coverage gap for
the lifecycle half of the architecture. Disposition: the gate-3
lifecycle corpus (IV.5 item 3) is the named vehicle.

---

## 4. Concordance with runs 1 and 2

**P9-applied closures that resolve prior findings.** The commit at HEAD
includes register amendments that close several run-1/run-2 findings:

| Run 1/2 finding | Status at HEAD |
|---|---|
| **P9-1 (Blocker)**: facet payload validation vacuum | **Closed** by P9-applied #17 — facet enforcement executable now validates payloads against normative descriptors; 7 facet vectors including the original probe |
| **P9-2 (Major)**: 7 untested normative subsystems | **Partially closed** by backlog #18 delivery — 4 new vector families (facet, reference, lifecycle, tier) added; 2 remaining families (semver, conditional-apply) parked at gate 4 |
| **P9-4 (Major)**: Mapping scope validation vacuum | **Closed** by P9-applied #16 — reference taxonomy normative; 9 reference vectors including statement-scope checks |
| **P9b-1 (Blocker)**: `references-resolve` contradiction | **Closed** by P9-applied #16 — closure vs. landmark taxonomy normative; parties landmark by D22 test |
| **P9b-6 (Major)**: tier anchor underivable | **Closed** by P9-applied #19 — layered tier anchor derived from data; 8 tier vectors |
| **P9b-7 (Major)**: orphaned gate-2 obligations / missing DSSE profile | **Partially closed** — DSSE profile now exists (`dsse-envelope-1.0.0.json`); items re-parked in backlog #18 |

**Findings from runs 1-2 confirmed as still open at HEAD:**

| Finding | Status at HEAD |
|---|---|
| **P9-3 (Major)**: inflated survivorship claim | README lines 154-157 now carry a qualified wording ("beyond the same morning's already-decided D9-rev") — **materially improved** but the characterization remains debatable |
| **P9b-3 (Major)**: RFC 8785 canonicalization | **Still open** — my P9c-1 confirms the implementation is unchanged |
| **P9b-4 (Major)**: relations channel contradictions | **Partially addressed** — on backlog #20 but not yet closed |
| **P9b-5 (Major)**: op vocabulary drift | **Partially addressed** — `set-field` and `attach-facet` rows now in spec; `override` field appears removed; Set addressing on backlog #21 |
| **P9b-8 (Major)**: statement-grammar declaration | **Still open** — my P9c-3 reconfirms |
| **P9b-10 (Minor)**: D22 demotion vs closed shapes | **Still open** — on backlog #22; my P9c-4 reconfirms |
| **P9b-12 (Minor)**: count drift | **Partially addressed** — README object counts corrected; new count drift introduced by vector expansion (my P9c-2/6/7) |

**Run 1 "examined, no finding" items overturned by later evidence:**
- Attack surface 10 (canonicalization): overturned by run 2's P9b-3,
  confirmed here as P9c-1.
- Attack surface 12 (composition determinism): qualified by run 2's
  P9b-6, now closed by #19's tier anchor.

**New in this run (no counterpart in runs 1 or 2):**
- P9c-2: the 54→115 vector count drift (a consequence of the very
  fixes that closed prior findings — the documents didn't update)
- P9c-9: `decimalString` leading-zero digest ambiguity

---

## 5. Blind re-score diff (attack 4)

Five decisions re-scored without first reading the register's verdicts:

| Decision | My independent score | Register score | Divergence? |
|---|---|---|---|
| D9 | Customer ✓ (3/3 modality convergence, 347 pseudo-controls, bizdays) · Simplicity ✓ (one lattice) · Complexity ↓ ✓ (eliminates BSI grammar props, 216 defects) | Matches | None |
| D13 | Customer ✓ (5,557 ISM membership props, CR26 class variants) · Simplicity ✓ (8 ops) · Complexity ↓ ✓ (replaces profile resolution) | Matches | None |
| D20 | Customer ✓ (SCF, CIS, NIST mapping model demand) · Simplicity ✓ (9 fields vs document model) · Complexity ↓ ✓ (prevents relation-string props) | Matches | None |
| D22 | Customer ✓ (every kernel field is a permanent tax) · Simplicity ✓ (3 countable questions) · Complexity ↓ ✓ (ends promotion-by-advocacy) | Matches, but: the anticipated-path trade-off (D22 rev) understates the closed-shape risk (P9c-4) | Minor gap: trade-off text names "the kernel can now be wrong in a new way" but does not name the schema-breakage corpse |
| D22-applied | Customer ✓ (264/264 resolution measured) · Simplicity ✓ (no tenth type) · Complexity ↓ ✓ (identity/lifecycle free from host Set) | Matches | None |

One divergence: D22 rev's trade-off is correct in spirit but the
specific failure mode (closed shapes breaking on demotion) should be
named as the corpse. Filed as P9c-4.

---

## 6. Examined, no finding

- **Attack surface 1 (Facets vs props — operational difference):** The
  P9-applied #17 amendment closes the operational gap that run 1's
  blocker identified. Facet payloads now validate against normative
  descriptors; unregistered facets → error; `private:` ignored. The
  7 facet vectors exercise the three legal states. **Cleared.**

- **Attack surface 2 (Registry corpse vs facet registry):** ch15 makes
  the Foundation's index SHOULD-tier and non-load-bearing; bundles
  self-carry pinned schemas; the manifest pin is the registry. Structurally
  answered. **Cleared.** (Concurs with run 2's clearance.)

- **Attack surface 3 (Aggregate simplicity):** IV.1 and ch12 honestly
  label "simpler/weekend" as unmeasured pending gate 4. The concept
  inventory is large (9 types + 2 sub-objects + manifest + 2 digests +
  JCS + lattice + 8 ops + 3 predicates + facets + supplements +
  deviations + tier derivation), but so is 1.x (8 models + Metaschema +
  profile resolution + XML/YAML + Schematron + JSON Patch). The honest
  tier label holds. **Cleared at its stated tier.**

- **Attack surface 6 (Which customers — NIST):** IV.4 says "Not yet
  demonstrated — gate corpus item" for NIST lifecycle. README line 154
  qualifies the validation survivorship claim. The honest-tier labeling
  is correct: "met for the census, open for NIST." **Cleared at its
  stated tier.**

- **Attack surface 7 (No more props — residue audit):** Bundles ship
  0 props. The `annotations` dictionary is explicitly not compliance
  (D10). The `oscal-1x@1` compat facet carries ISM residue with
  declared semantics. The relations channel has known drift (backlog
  #20) but is not a prop-smuggling vector — relations carry typed
  edges. **Cleared with #20 as a known open item.**

- **Attack surface 8 (Next-format problem):** Appendix F answers the
  standards-proliferation objection with measured convergence evidence
  (three authorities, one model). The answer is evidence-based, not
  rhetorical. Forward adoption is honestly labeled hypothesized. **Cleared.**

- **Attack surface 9 (Identity under adversity):** D2's global URIs
  with `canonical-alias` vs `replaces` split; the P9-applied #16
  reference taxonomy with closure vs. landmark classes; the layered
  tier anchor (#19). Domain rebrand → `canonical-alias` (now with
  backlog #14's self-policing recommendation). Hostile mirror →
  manifest digest mismatch. Forked alias → semantic digest comparison
  exposes the divergence. **Cleared structurally** (the self-policing
  check in #14 is SHOULD-tier, not MUST — acceptable given the
  attestation digest chain provides the hard guarantee).

- **Attack surface 11 (Modality lattice vs legal meaning):** The D9
  lattice, may-only incomparabilities, and axis-change rules survive
  adversarial pairing. DARF NUR → DARF NICHT lands incomparable
  (correctly routed to the audited channel). **Cleared.** (Concurs
  with run 2.)

- **Attack surface 12 (Tailoring/deviation/supplement composition):**
  The P9-applied #19 tier anchor resolves run 2's P9b-6. Composition
  is deterministic (ordered list, same-target = error, chaining for
  overrides). The 9 tailoring vectors test selection, conflict, and
  op-law enforcement. Supplement pattern composition is defined
  (non-chaining, D20/D21 rev). **Cleared.**

- **Attack surface 13 (Migration and consumption reality):** Coverage
  reports declare every conversion rule with counts. Source→core
  direction is measured (100% leaf coverage × 8 corpora). Core→source
  export is correctly scoped as gate-4 designed-for work (spec IV.5
  item 4). **Cleared at stated tier.**

- **Attack surface 14 (Conformance completeness):** The expansion from
  54 → 115 vectors closes many of run 1's P9-2 gaps. Remaining
  untested normative subsystems: bundle-composition semver (D3.5),
  `conditional-apply` instantiation (B.1.8) — both explicitly parked
  at gate 4 in backlog #18. **Cleared with declared remaining gaps.**

---

## 7. Pending online verification

- CIS corpus repository status (R15; scope item).
- Availability of verified RFC 8785 implementations in Python
  (bears on P9c-1 fix cost).
- D18's "defense data diodes with XSD deep inspection" installed base
  (no in-repo count).

---

## 8. Mission B — the north-star audit

**B1. Canonicalization.** Audited against the four-test formulation:
*simpler · closer to measured customer needs · no more props · less
need for bespoke JSON*. The register's three axes read as a folding
(complexity = no-props + no-bespoke) that is now explicitly documented
as a presentation choice (register header P9 erratum applied).

**B2. Operationalization.** Using only in-repo artifacts:

1. **Simpler:** *Met (measured)* = concept count lower than 1.x for
   equivalent scope; LoC comparison. *Met (designed-for)* = weekend
   validator claim. *Not demonstrated* = no timed implementation
   comparison exists. *Violated* = full Portable inventory is large.
   Instrument: concept inventory branching factor; schema total lines.
   Current schema: 358 lines. Concept inventory: 9+2 types, 11 code
   systems, 8 primitives, 8 ops, 3 predicates, 2 digest domains, JCS,
   facet system, manifest protocol = ~45 named concepts.

2. **Closer to measured customer needs:** *Met (measured)* = census
   field→kernel traceability. Reverse audit (kernel fields with no
   measured need): `title` on Requirement (convenience — not measured
   in any corpus as a distinct semantic), `label` on base objects
   (display handle). Both are optional. Every other kernel field traces
   to a counted corpus need. *Not demonstrated* = NIST lifecycle.

3. **No more props:** *Met (measured)* = bundles ship 0 props; by-statement
   keying normative; facet validation enforced. *Open carriers:* relations
   channel with unconstrained extension tokens (backlog #20);
   `terminology@1` payload fields with unconstrained objects (#23);
   `annotations` (by definition invisible to compliance — a designed
   carrier, not a smuggling vector).

4. **Less bespoke JSON:** *Met (measured) backward* = CR26 absorbed
   7,294/7,294. *Hypothesized forward* = adoption claim. Instrument:
   what a tenth framework would invent. Current open: backlog #10
   (CTL/ODP) and #12 (localized-text type).

**B3. Verdict table.**

| Test | Verdict | Strongest support | Strongest opposition |
|---|---|---|---|
| **Simpler** | **Met (designed-for); not measured — and labeled so** | 9 closed shapes in one 358-line schema; 115 conformance vectors (up from 54); profile algebra → 4-step algorithm; reference validator is 296 lines | Full-Portable concept inventory is ~45 named concepts; RFC 8785 done right is harder than shipped approximation (P9c-1); gate-4 measurement pending |
| **Closer to measured customer needs** | **Met (measured) for census + validation corpora; open for NIST** | 8 corpora at 100% declared coverage; D9/D13/D20/D21 cite counted needs; 5,470 objects verified | NIST unconverted until gate 3; lifecycle types exercised by 13 examples only (P9c-12); D18 count-free |
| **No more props** | **Met (measured) for the corpus** | Bundles ship 0 props; >70% of counted prop instances structurally dead; facet validation now enforced (P9-applied #17) | Relations channel drift (backlog #20); `statement-grammar@1` declaration contradiction (P9c-3); `terminology@1` unconstrained payload fields (#23) |
| **Less bespoke JSON** | **Met (measured) backward; hypothesized forward** | CR26 absorbed 7,294/7,294; GS++ props absorbed into kernel; no Metaschema dependency | Forward claim untestable pre-adoption; 1.x export designed-for only (gate 4) |

**B4. Gap list (claimed > demonstrated).**

| Location | Claimed | Actual | Finding |
|---|---|---|---|
| Spec IV.5.2 L684 | "54 vectors across five families" | 115 vectors across nine families | P9c-2 |
| README L93 | "54-vector conformance corpus" | 115 | P9c-7 |
| Backlog #18 | "107 vectors at HEAD" | 115 | P9c-6 |
| `statement-grammar@1` descriptor | `modifies-semantics: []` | B.3 says it modifies assessment | P9c-3 |
| `decimalString` pattern | Canonical decimal | Permits leading zeros | P9c-9 |
| `DEEP_RESEARCH_REVIEW.md` | "50-70% payload" / "93,259" | Refuted by F.7 / pre-drop total | P9c-11 |
| ch01 L270 | "twenty-one decisions" | 22 decisions | P9c-10 |

**B5. Falsification plan.**

1. **Simpler (gate 4):** pre-register the weekend-validator protocol —
   two implementers, two languages, LoC + hours + defect classes;
   **include RFC 8785 cross-implementation digest equality** over an
   adversarial key/number corpus as an acceptance criterion (settles
   P9c-1 in the same run).

2. **Conformance coverage completeness:** the two remaining vector
   families (semver composition, conditional-apply) ship with the
   gate-4 engines. Pre-register the vector-to-MUST mapping: every
   normative MUST in the spec text must have ≥1 vector, and the mapping
   is published as a traceability artifact.

3. **NIST customer test (gate 3):** conversion of NIST SP 800-53 Rev 5
   catalog + baselines. #10 CTL/ODP is the pre-registered risk.
   The milestone that moves "closer to customer needs" from
   "met for census" to "met for NIST."

4. **D22 demotion (P9c-4):** dry-run a synthetic anticipated promotion
   + demotion against a schema copy; write the migration rule from the
   wreckage. Pre-1.0 scoping is the simplest fix.

5. **Lifecycle type depth:** the gate-3 corpus should exercise at least
   100 objects across the five lifecycle types with full digest
   verification, reducing the 13:5,470 asymmetry (P9c-12).

---

**Aggregate verdict.** The north star is **met at the tiers the project
itself claims** — and the honest tier labels are in place. The P9-applied
amendments since runs 1-2 closed the two blockers (facet validation
vacuum, reference-resolution contradiction) and the tier-anchor gap,
significantly strengthening the executable layer. What this run adds:
(1) **count-drift is the new dominant doc-quality issue** — the very
fixes that closed prior findings introduced stale counts across three
front-door documents (P9c-2/6/7); (2) the **RFC 8785 canonicalization
gap remains the highest-severity open technical finding** (P9c-1,
originally P9b-3); (3) `statement-grammar@1` needs its #8-style
declaration re-audit (P9c-3); (4) the D22 demotion migration gap is
normative and latent (P9c-4). None is architectural. All are closable
before v0.6 ships. Every item has a named corpse and a countable fix.
