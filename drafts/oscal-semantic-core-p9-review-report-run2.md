# P9 — Adversarial Design Review: Second Independent Run (P9b)
### Flaw hunt + north-star audit · 2026-07-21 · commit reviewed `b254f90`

**Relation to run 1.** This is an independent second execution of
`oscal-semantic-core-p9-review-prompt.md`. All findings below were
derived and demonstrated before reading run 1's report
(`oscal-semantic-core-p9-review-report.md`, commit `bbb2b16`); the
concordance in §4 was added afterwards, and ids are numbered **P9b-***
to avoid colliding with run 1's register. Two independent runs of one
prompt make agreements replication evidence and disagreements data —
§4 lists both.

**Limitations (ground-rule 2 disclosure).**
1. Run in the prompt-authoring session, not a fresh one. Finding
   P9b-14 and parts of P9b-12 were pre-identified during prompt
   authoring and are marked ⚠.
2. Blind re-score (attack 4) used D13/D18/D20/D21/D22; D1–D3 excluded
   (rationales read during prompt authoring).
3. Leaf-value coverage totals are accepted from the coverage reports;
   emitted-object counts were independently re-verified for all eight
   corpora and match exactly.
4. External-world claims flagged `[needs online verification]`, never
   asserted.
5. Review-round-1/-2 adjudications (backlog #13–#15, F.7) were read
   first; nothing below re-raises them without new evidence.

**Demonstration harness.** An adversarial bundle (5 wrong probes +
1 positive control + 1 clean twin) was built in the session scratchpad
and run through `validate_core.py`: **8 pass, 1 fail — the only
failure is the positive control** (unbound `{param:}` token), proving
the greens are genuine acceptance, not a broken rig. A separate probe
compared the validator's canonicalization against the `jcs` RFC 8785
reference implementation.

---

## 1. Findings register

| ID | Sev | Class | Basis | Finding |
|---|---|---|---|---|
| P9b-1 | **Blocker** | b | measured | `references-resolve` (B.1.1) as normatively written is violated by every green bundle |
| P9b-2 | **Major** | a | demonstrated | Validator accepts duplicate statement ids, twin objects under one id, dangling members, lawless ops |
| P9b-3 | **Major** | a | demonstrated | Semantic-digest canonicalization is not RFC 8785 — digests diverge cross-implementation |
| P9b-4 | **Major** | b | measured | Relations channel: D13 "free/informative" vs B.3/C.8 computed semantics vs open tokens; C.8 `supersedes` resurrects the D2-split concept |
| P9b-5 | **Major** | b | measured | Operation vocabulary drift: D13 table missing `set-field`/`attach-facet`; whitelist unenforceable; undocumented `override` field; Sets unaddressable |
| P9b-6 | **Major** | a | argued | Tailoring tier (authority/consumer) decides Deviation duties but is not derivable from any artifact |
| P9b-7 | **Major** | c | measured | Gate-2 closure orphans three obligations parked "at gate item 2"; D7's normative DSSE profile does not exist |
| P9b-8 | Major | b | measured | `statement-grammar@1` declares `modifies-semantics: []` while B.3's detach law names detaching it as its corpse |
| P9b-9 | Minor | b | measured | Manifest-pinned facet stubs contradict normative stdlib declarations in shipped bundles |
| P9b-10 | Minor | a | argued | D22 anticipated-path demotion has no migration rule against closed kernel shapes |
| P9b-11 | Minor | a | argued | `uses-term` "nearest hosting Set" lacks metric and tiebreak under multi-membership |
| P9b-12 | Minor | d | measured | Count-drift set: 216 vs 213 · 93,259 vs 92,886 · "21 decisions" · "11 open items" · "3,066" · "5,478" ⚠(partly) |
| P9b-13 | Minor | c/d | measured | `DEEP_RESEARCH_REVIEW.md` retains refuted/wrong numbers at repo root with no in-file erratum |
| P9b-14 | Note | d | measured | ⚠ Finding 0: north star stated as three and as four tests; ch01 misdescribes the register (concurs with run 1's P9-0) |
| P9b-15 | Note | b/c | measured | Tier-labeling and schema-drift nits (nine-item list) |

---

## 2. Blocker and Major findings — detail

### P9b-1 · `references-resolve` fails its own proof corpus — **Blocker (b, measured)**
Appendix B.1.1: *"every reference string in every object must land on
a manifest entry … a bundle that doesn't close doesn't validate"*, and
"Exercised: … all three converter bundles close (3,066 objects)."
Recomputed at HEAD: **CIS.Ubuntu2404 — 635/635 Mappings carry endpoint
refs with no manifest entry; FedRAMP-CR26 — 373/373; every corpus
carries party URIs** (`obligated-parties`, `approver-ref`, `signer`,
`performer-ref`) that resolve to nothing — parties have no kernel type
and no manifest entries. Under the primitive as written, all nine
green bundles are invalid; the delivered validator escapes the
contradiction only by not implementing the primitive (probe C: a Set
member naming a nonexistent URI validates green). The "all bundles
close" claim is false for any reading including mapping endpoints or
parties; the 3,066 count is stale (5,470 at HEAD).
**Corpse:** a consumer resolves a baseline against a bundle whose
member was silently dropped — the 1.x dangling-reference failure
returns wearing a green checkmark.
**Disposition:** v0.6 normative reference taxonomy — closure-required
refs (Set `members[].ref`, `component-ref`, `requirement-ref`,
`assessment-ref`, capability refs) vs. landmark-permitted refs
(Mapping endpoints, party/authority URIs, external evidence); then
implement + negative vectors; decide whether parties deserve a typed
home. (Run 1's P9-4 demonstrates the Mapping-scope corner of the same
vacuum; this finding adds that the normative *text* already condemns
the shipped corpus.)

### P9b-2 · Five wrong constructs validate green — **Major (a, demonstrated)**
(A) Requirement with two statements both `id: "s1"` — every
identity-addressed mechanism (by-statement keys, `statement-id` ops,
`statement-refs`) becomes ambiguous; (B) **two objects with one id and
different meaning at two paths** — the twin-catalog corpse, accepted
because `unique-within` (B.1.3; Core-required per the D15 matrix) is
unimplemented; (C) dangling member ref (P9b-1); (D) consumer Tailoring
issuing `set-field` on `obligated-parties` (off the B.3 whitelist)
plus `attach-facet` with a selection-changing payload, no Deviation —
no operation-law checking exists in bundle validation; (E)
`detach-facet` naming no facet — schema conditionals cover
set-parameter/set-modality/replace-prose/set-field but not
attach/detach/add-relation/remove-relation.
Mitigating fact (measured): the real corpora are clean — **0 duplicate
ids, 0 unresolved member refs across 14,508 member references**. The
exposure is the ecosystem's first second producer.
**Disposition:** implement `unique-within` + op-law checks + the four
missing schema conditionals; add each probe as a negative vector.

### P9b-3 · Canonicalization is not RFC 8785 — **Major (a, demonstrated)**
`canonical()` in both `validate_core.py` and `oscal_conv_lib.py` is
Python `json.dumps(sort_keys=True)` — code-point key ordering. RFC
8785 §3.2.3 orders keys by **UTF-16 code units**. Demonstrated against
the `jcs` reference library: for an object whose keys are
`ﬁ…` (U+FB01) and `😀…` (U+1F600), the two implementations emit
different member order and **different semantic digests**
(`sha256:264f48ef…` vs `sha256:494925e5…`). D3.4 is a MUST ("two tools
MUST derive identical digests"); the JCS vector family (7 vectors,
1 negative) pins neither key ordering nor the ES6 number domain.
Frequency today is low (corpus keys are ASCII) — but this is the
integrity foundation and `attestation-binds` inherits it. This
overturns run 1's "attack surface 10 — examined, no finding".
**Corpse:** two conformant tools verify one signed bundle and disagree
— Semantic Match vs. tamper.
**Disposition:** adopt a verified RFC 8785 implementation in validator
+ converter lib (manifest digests re-pin at the next converter run);
add UTF-16-ordering and number-domain vectors.

### P9b-4 · The relations channel contradicts itself — **Major (b, measured)**
Three statements cannot all stand: spec D13 table —
`add-relation`/`remove-relation` **free** ("relations are
informative"); Appendix B.3 — "typed edges only (C.8 codes); removal
of a `required` edge ⇒ **Deviation**"; spec Appendix A — `type (open
token…)`. C.8 supplies the coherent shape (stdlib base codes with
computed semantics + namespaced URI-typed extensions that tools "carry
and display but do not compute") — but the kernel schema enforces no
namespacing, so a typo'd base code (`requird`) silently becomes a
carried extension instead of failing `code-from`: C.4's own measured
drift corpse, reborn inside the one deliberately open surface. And
C.8's base vocabulary includes **`supersedes`** — the conflated
concept D2 explicitly split into `canonical-alias` vs `replaces` after
P7-B4 proved it unsafe; a second, un-split lineage carrier now exists
beside the kernel fields.
**Disposition:** v0.6 — align the D13 row with B.3/C.8; constrain
extension relation types to URI shape in the schema; delete or rename
C.8 `supersedes`.

### P9b-5 · Operation vocabulary: promise > contract > delivery — **Major (b, measured)**
The schema ships eight ops; the spec's D13 law table covers six — no
`set-field` row, no `attach-facet` row — while Appendix A calls the
vocabulary "D13 vocabulary". Appendix B.3 has the missing laws
(set-field: "whitelisted non-normative fields only (title, label,
sequence, annotations)"; attach/detach symmetric Deviation duty), but
the whitelist exists nowhere machine-readable — not in the schema
(`field: string`), not in vectors, not in the validator (probe D
green). Every operation requires `requirement-ref`, so **Sets are
unaddressable** — yet the whitelist includes `sequence`, which lives
on Set members. The operation schema carries an undocumented
**`override`** field appearing in no spec/handbook/vector text, while
ch06 §6.4 says "chaining is the only override path". ch06 §6.2 claims
"pin the target's exact version … (the specification says SHOULD)" —
no version-pin field exists on operations. ch06 §6.3 states the
detach duty only; B.3 states attach+detach (handbook-internal drift).
**Disposition:** v0.6 — add the two D13 rows, encode the whitelist as
a schema enum, define Set addressing or strike `sequence`, remove or
document `override`, add the version-pin field or delete the ch06
sentence.

### P9b-6 · Tailoring tier decides duties but is not derivable — **Major (a, argued)**
D13 rev / B.1.6 bind Deviation duties to the *publisher's tier*
("Authority-tier Tailorings owe none"). No artifact carries that tier:
`tailoring-vectors.json` encodes it as test metadata
(`"tier": "consumer"`), and bundle validation performs no duty
checking at all. Nothing in spec, schema, or manifest defines how a
validator decides a given Tailoring's tier. The register's D13(rev)
line "one question decides the duty: who published the Tailoring?" is
unanswerable from data. This qualifies run 1's "attack surface 12 —
composition confirmed deterministic and vector-tested": determinism
holds only once the tier is stipulated out-of-band.
**Corpse:** two conformant Portable tools disagree on the same
bundle's validity — the implementation-defined-behavior pattern D15
exists to abolish.
**Disposition:** v0.6 — define the tier anchor normatively (candidate:
authority-tier iff the Tailoring's id URI shares the authority prefix
of the Set it selects; attestation signer as the stronger anchor); add
vectors where tier is derived, not stipulated.

### P9b-7 · Gate-2 closure orphaned its parked obligations — **Major (c, measured)**
Three Appendix-B passages park work "at gate item 2", which IV.5.2 now
declares DELIVERED: B.1.3 — "corpus negative cases are gate-item-2
work" (absent; `unique-within` also unimplemented); B.1.8 — "corpus
instantiation is gate-item-2 work" (absent; `conditional-apply`
unimplemented in the delivered executable); B.1.7 — "Envelope
verification awaits the DSSE profile (gate item 2)" (absent — and D7
says "the stdlib DSSE profile **remains normative**" while no such
artifact exists among the six shipped stdlib descriptors). IV.5.2's
delivered list is accurate for what it enumerates; the parked items
silently lost their home. Related: the kernel schema's own description
says shape-disjointness is "exercised by the conformance corpus" — no
vector family covers it (54 = 7+21+12+9+5). (Complementary to run 1's
P9-2, which maps seven untested normative subsystems.)
**Disposition:** re-park each item explicitly (gate 3/4 or backlog
rows with counts); ship the DSSE profile or down-tier D7's wording;
add a disjointness vector family.

### P9b-8 · `statement-grammar@1` contradicts B.3's own corpse — Major (b, measured)
Shipped descriptor: `modifies-semantics: []`. B.3's detach-facet law
fires only on non-empty declarations, and its rationale names its
corpse: *"detaching the grammar facet from a German requirement
changes what assessors check."* Under the shipped declaration, exactly
that detach is Deviation-free. Either the grammar facet modifies
assessment (declare `[assessment]` per the #8 audit's own principle:
"a semantics-bearing facet declaring `[]` is the silent-ignore corpse
wearing a conformance badge") or B.3's example is wrong.
**Disposition:** re-audit `statement-grammar@1` under the #8
declaration audit; fix descriptor or B.3 text.

---

## 3. Minor findings and notes — detail

**P9b-9 (b, measured).** Shipped bundles pin facet-schema *stubs*
whose declarations contradict the normative stdlib: the CR26 bundle
pins `reporting-obligation` with `[]` (normative `[assessment]`) and
`effectivity` with `[]` (normative `[selection]`). D3 makes manifest
pins the trust anchor, so a pin-honoring Portable tool reads the
pre-promotion declarations — a live divergence between pinned truth
and normative truth until the recorded converter rerun; fail-closed
behavior differs by which source a tool trusts. (Sharper corner of the
facet-trust vacuum run 1 files as its P9-1.)

**P9b-10 (a, argued).** D22's anticipated-convergence path demotes a
kernel semantic after two dry gate cycles — but kernel shapes are
closed (`unevaluatedProperties: false`), so content authored during
the anticipation window becomes schema-invalid on demotion. No
migration/deprecation rule; not scoped to pre-1.0. Latent today (zero
anticipated promotions shipped; terminology landed as a facet via the
absorption clause). Disposition: demotion emits a compat facet
automatically + a deprecation major, or scope the path pre-1.0.

**P9b-11 (a, argued).** `terminology@1`: "`uses-term` relations
resolve against the terminology payload of the **nearest** hosting Set
in the bundle" — no distance metric, no tiebreak. The supplement
pattern makes collision realistic: a Requirement directly a member of
an upstream root Set and a shadow Set, each hosting a glossary — both
"nearest"; two conformant tools resolve one term to two definitions.
Disposition: define distance (membership hops), ties ⇒ Portable-tier
validation error, or explicit precedence.

**P9b-12 (d, measured).** Count drift, each recomputed this session:
- README:133 "surfaces all **216** pseudo-placeholders" — the linked
  report states **213** and explains why (216 was census GS++ **+
  MS-TLS**; MS-TLS dropped 2026-07-21; census GS++-only was always
  213). The flagship number needs a census/corpus split wherever it
  appears as a live-corpus claim.
- Appendix F Q20 "93,259 values" — the three current census reports
  sum to **92,886** (36,161 + 49,431 + 7,294); 93,259 is the pre-drop
  census total. (Feeds P9b-13: the deep-research review copies 93,259
  and mislabels it as the 8-corpus total, which is actually 130,350.)
- ⚠ README:101 "21 decisions" and ch01:270 "twenty-one" — the register
  holds 22.
- README:102 "11 open items" — 5 are open (#10, #12–#15).
- B.1.1 "3,066 objects" — 5,470 at HEAD.
- IV.5.2/README:95 "5,478 object validations, both digests re-verified
  per object" — 5,478 = 5,470 objects + 8 manifest validations
  (concurs with run 1's P9-6), and the example bundle's 13 objects —
  the only instances of Assessment/Finding/Implementation/Attestation/
  Component — are shape-checked only (no manifest, no digest
  verification), so the "both digests" clause does not cover them.
- README:95 "nine corpus bundles" = 8 corpus bundles + the example
  bundle (IV.5.2 words it precisely).
- Spec header "five adversarial passes and one validating pass" beside
  an eight-entry lineage; now further outdated by review rounds 1–2.
Disposition: one erratum sweep.

**P9b-13 (c/d, measured).** `DEEP_RESEARCH_REVIEW.md` sits at repo
root carrying: the F.7-refuted "50–70 % payload / ~60 % token"
figures; "93,259" mislabeled as the 8-corpus total while the table on
the same page sums to **130,350**; present-tense down-conversion
claims that IV.5.4 correctly re-tiers as gate-4 work. The refutation
lives in Appendix F.7; the refuted numbers live at the front door with
no banner — prominence inverted against the house rule ("corrections
ship with the same prominence as the original claim").
Disposition: erratum header in the file pointing at F.7, or move it
under `drafts/reviews/` with an adjudication note.

**P9b-14 (d, measured) ⚠ Finding 0.** North star arity: register:2/5
say three tests; spec:17–22 lists four clauses then names three
scoring axes; ch01:266–270 and README:63 say four — and ch01:269-270
claims the register "scores all twenty-one architectural decisions
against exactly those four tests" (it scores three axes; there are 22
decisions). Concurs with run 1's P9-0 and its disposition (harmonize
on the four-test wording; make the register's folding explicit).

**P9b-15 (b/c, measured, list).**
1. Schema `calendarUnit` includes `weeks`; spec D9 lists
   `days|bizdays|months|years` — schema exceeds spec.
2. B.1.5 requires declared parameters be "referenced or explicitly
   marked display-only" — no such marking exists in the schema, and
   the declared-but-unreferenced direction is unimplemented.
3. `decimalString` permits leading zeros — two lexical forms of one
   value ⇒ two semantic digests; pin a no-leading-zeros rule.
4. `terminology@1` payload fields `note`/`notes`/`glossary-info` are
   unconstrained objects (prop-bags inside a pinned schema); its
   `definition` lang-map lacks the kernel's BCP-47 propertyNames
   pattern.
5. `contentManifest.renderings` items are unconstrained.
6. Finding `actions[].due` is `type: object` in the schema; Appendix A
   says `date | calendar-period` — a plain date string is
   schema-invalid though spec-legal.
7. D18 is the only register entry whose Customer line carries no count
   ("defense data diodes … installed base"
   [needs online verification]).
8. `may-only` ships with ×0 corpus instances — honestly disclosed in
   F Q12, unlabeled in spec D9/register D9.
9. The JCS vector family is the thinnest of the five (7 vectors,
   1 negative) while guarding the digest foundation (see P9b-3).

---

## 4. Concordance with run 1 (`oscal-semantic-core-p9-review-report.md`)

**Replications (independent agreement).** Finding 0 (their P9-0 = my
P9b-14, same evidence lines); the 5,470-vs-5,478 recount (their P9-6 =
my P9b-12, same decomposition including the 5,483 figure); ch01's
"days" claim unlabeled (their P9-7; folded into my Mission B and
P9b-15 context); validator ALL GREEN reproduced identically; both runs
built adversarial objects that validated green — different probes,
same conclusion: the executable proves less than the prose claims.

**Run 1 findings this run confirms and did not independently file.**
Their **P9-1** (facet payloads and unregistered facet URIs pass green
— their Blocker) — my probes D and P9b-9 touch the same vacuum from
the operation and pinned-stub sides; their object-level probe is the
cleanest demonstration and stands. Their **P9-2** (seven normative
subsystems with zero vectors) — systematic superset of my P9b-7
vector-gap notes; both should merge in triage. Their **P9-3**
(survivorship: the D9-rev parameter change landed the same day as the
validation conversions, so "the model held without kernel changes" is
overstated) — my analysis reached the same timeline and under-filed
it; their finding is correct and mine defers to it. Their **P9-4**
(Mapping scope strings unvalidated, self-loops green) — same vacuum
as my P9b-1's scope corner; merge in triage. Their **P9-5**
(calendar-context) re-raises adjudicated backlog #13 as an expedite
recommendation — flagged here per ground rule 4; no new evidence, so
it is a priority statement, not a new finding.

**Contradictions (run 1 "examined, no finding" overturned by
demonstration here).**
1. Run 1, attack surface 10: "Confirmed two-digest domain model …"
   — the cycle-freedom holds, but the canonicalization beneath both
   digests is not RFC 8785 (my P9b-3, demonstrated with divergent
   digests). The no-finding verdict does not survive.
2. Run 1, attack surface 12: "composition is deterministic and
   vector-tested" — determinism holds only once the publisher tier is
   stipulated out-of-band (my P9b-6), and two of the eight ops have no
   law in the spec's own table (my P9b-5).

**New in this run (no counterpart in run 1).** P9b-1 (the B.1.1
normative-text contradiction with 1,008 external mapping endpoints +
party URIs, and the false "all bundles close" claim), P9b-2's
identity-uniqueness probes (duplicate statement ids; twin objects,
one id), P9b-3 (RFC 8785), P9b-4 (relations contradictions +
`supersedes`), P9b-5 (op-vocabulary drift + `override`), P9b-6 (tier
anchor), P9b-7 (orphaned gate-2 obligations + missing DSSE profile),
P9b-8 (statement-grammar declaration vs B.3), P9b-9 (pinned stubs),
P9b-10 (demotion vs closed shapes), P9b-11 (nearest-Set ambiguity),
P9b-12's 216/213 and 93,259/92,886 items, P9b-13 (DEEP file erratum
prominence).

---

## 5. Blind re-score diff (attack 4)

D20, D21: scores match the register. Divergences, all filed: **D13** —
"who published the Tailoring?" is unanswerable from data (P9b-6);
**D18** — the only decision with a count-free Customer line
(P9b-15.7); **D22 rev** — the demotion backstop's breakage against
closed shapes is unnamed in the trade-off (P9b-10).

## 6. Examined, no finding

- **Registry rot vs facet registry (attack 2):** ch15 makes the
  Foundation's index/log SHOULD-tier and non-load-bearing ("the index
  can burn down tomorrow and not a single validation … changes its
  answer"); bundles self-carry pinned facet schemas. The project's own
  corpse is answered structurally. (The "Foundation" entity itself is
  undefined — worth one sentence in ch15.)
- **Modality lattice vs legal meaning (attack 11):** the D9 order,
  may-only incomparabilities, and axis-change rules survive
  adversarial pairing (DARF NUR → DARF NICHT lands incomparable —
  audited channel, correctly). Party re-targeting is unrepresentable
  in the documented vocabulary; the `set-field` hole is P9b-5, not a
  lattice defect.
- **Exclude-is-selection (D13):** defended with counts; holds.
- **Valid-and-meaningless via prose/modality contradiction:** not a
  kernel hole — the typed field is normative, prose is rendering; the
  grammar facet + source-QA pipeline is the catch path. Holds.
- **Coverage semantics:** `oscal_conv_lib.coverage()` implements
  extraction-accounting — every source leaf value must match a
  declared rule, UNMAPPED = 0 as the gate signal, L2 residues declared
  with named exits (F Q21). "100 %" claims exactly what the code
  measures; round-trip correctly deferred to gate 4.
- **Aggregate simplicity claims in the normative core:** IV.1 and
  ch12's evidence marker label "simpler/weekend" as unmeasured pending
  gate 4 — the honest tier. The inflation that existed (deep-research
  Dimensions 7–8) is refuted or flagged (P9b-13).
- **Sealed/air-gap design structure:** manifest exclusion of
  attestations is cycle-free; bi-modal states well-defined. The
  implementation-level digest defect is P9b-3; the design holds.

## 7. Pending online verification

- D18's "defense data diodes with XSD deep inspection are an installed
  base" (no in-repo count).
- CIS corpus repository status (R15; already a scope item).
- Availability of verified RFC 8785 implementations in the gate-4
  target languages (bears on P9b-3 fix cost).

---

## 8. Mission B — the north-star audit

**B1.** Audited against the four-test formulation (concurring with run
1's Finding-0 verdict that four is operative), with the register's
three axes read as a folding (complexity axis = no-props + no-bespoke)
that should be made explicit (P9b-14).

**B3 Verdict table.**

| Test | Verdict | Strongest support | Strongest opposition |
|---|---|---|---|
| **Simpler** | **Met (designed-for); not measured — and labeled so** | 9 closed shapes in one 358-line schema; 312-line reference validator; profile algebra → 4-step algorithm | Full-Portable concept inventory is large (digests, JCS, lattice, algebra, 8+3+8 vocabulary, pinning, composition); gate-4 measurement pending; RFC 8785 done right is harder than the shipped approximation (P9b-3) |
| **Closer to measured customer needs** | **Met (measured) for census + validation corpora; open for NIST — labeled so (IV.4)** | 8 corpora at 100 % declared coverage; emitted-object counts independently re-verified (all match); D9/D13/D20/D21 cite counted needs | NIST unconverted until gate 3 (#10 the live risk); lifecycle types exercised only by 13 hand-authored, digest-unverified examples; D18 count-free; `may-only` ×0 |
| **No more props** | **Met (measured) for the corpus; two carrier channels still open** | >70 % of prop instances structurally dead with no replacement construct; bundles ship 0 props; by-statement keying normative | Relations contradictions + unconstrained extension tokens (P9b-4); pinned stubs vs normative declarations (P9b-9); prop-bag corners inside a pinned stdlib schema (P9b-15.4); facet-payload validation vacuum (run 1 P9-1) |
| **Less bespoke JSON / meta-language** | **Met (measured) backward — CR26 absorbed 7,294/7,294; hypothesized forward — labeled so (F Q19/Q20)** | Bespoke CR26 and GS++ props land in one kernel; SCF/CSA path first-class (D20); no Metaschema/Schematron; one serialization | Forward claim untestable pre-adoption; 1.x export designed-for only, measurement folded to gate 4 (adjudicated) |

**B4 Gap list (claimed > demonstrated).** B.1.1 "all bundles close"
(P9b-1 — the one instance inside a normative appendix); README:133
(216→213); F Q20 (93,259); README:54 "machine-checked" facets (no
shipped tool validates payloads — run 1 P9-1); README:120 "model held
without kernel changes" (run 1 P9-3); IV.5.2 "both digests re-verified
per object" over-covers the example bundle (P9b-12);
DEEP_RESEARCH_REVIEW front-door numbers (P9b-13).

**B5 Falsification plan.**
1. *Simpler (gate 4):* pre-register the weekend-validator protocol —
   two implementers, two languages, LoC + hours + defect classes;
   **include RFC 8785 cross-implementation digest equality over an
   adversarial key/number corpus as an acceptance criterion** (settles
   P9b-3 in the same run).
2. *Core-tier completeness:* decide the P9b-1 reference taxonomy, then
   implement the missing primitive checks (references-resolve,
   unique-within, op-law, relation code-from) and re-run the nine
   bundles — expected green, now certifying what "green" is defined to
   mean.
3. *Spec sufficiency (P9b-5/P9b-6):* one independent second producer
   converts a C3A-sized corpus from the spec alone, no reference code
   — every question the spec cannot answer is a measured spec defect;
   the tier anchor surfaces at their first Tailoring.
4. *Customer test for NIST:* gate-3 conversion; #10 CTL/ODP is the
   pre-registered risk (concurs with run 1's B5.2).
5. *D22 demotion (P9b-10):* dry-run a synthetic anticipated promotion
   + demotion against a schema copy; write the migration rule from the
   wreckage.

**Aggregate verdict.** The north star is **met at the tiers the
project itself claims** — measured for customer-needs and
props-elimination on the converted corpus, designed-for on simplicity
and forward bespoke-prevention — and the honest labels are almost
everywhere they must be. What the two P9 runs jointly add: the
**executable layer currently proves less than the prose says it
proves** (P9b-1/2/3/7; run 1 P9-1/2/4), the extension surfaces have
drifted into three-way spec/handbook/schema contradictions exactly
where the props corpse teaches vigilance (P9b-4/5/8/9), and one
normative duty hangs on a tier no artifact can express (P9b-6). None
of this is architectural; all of it is closable in the v0.6 cycle;
every item has a named corpse and a countable fix.
