# OSCAL Semantic Core — Decision Rationale Register (v0.5)
## Every decision, justified against the four north-star tests
### 2026-07-18

**The four tests (session directive; P9 Finding 0 erratum: this header
once said "three" — the scoring axes below FOLD tests 3 and 4 into one
complexity axis, which is a presentation choice, not a different north
star).** Every decision below is justified
against: **Customer** — a measured need of the authorities and users (ISM,
BSI, CR26 census; SCF/CIS/CSA/NIST-lifecycle evidence), never taste;
**Simplicity** — fewer concepts, fewer ambiguities, learnable and
implementable fast; **Reduced complexity** — total tool-and-ecosystem
complexity goes *down*: no props, no custom Metaschema extensions, no
bespoke JSON formats forced into existence. Where a decision *adds*
something, the register states what larger thing it removes. Trade-offs are
stated; a decision with no stated cost has not been examined.

Format per decision: **Decision · Customer · Simplicity · Complexity ↓ ·
Trade-off.**

---

## D1 — JSON only; CommonMark+GFM prose, no raw HTML
**Decision.** One conformance serialization; one prose dialect with tables.
**Customer.** CR26 (the newest authoritative content) is JSON-canonical;
ISM's XML/JSON/YAML triple-publication is a measured agency tax; compliance
prose is full of parameter matrices — tables are a customer need, not a
luxury.
**Simplicity.** One byte-form to parse, digest, and document; no
markup-mapping rules to learn.
**Complexity ↓.** Deletes the serialization-sync problem that consumed a
large share of Metaschema's existence; deletes the c14n dependency chain.
**Trade-off.** XML constituencies served only via the fenced transit
projection (D18); triple-publishers generate extras outside conformance.

## D2 — Global authority URIs; string comparison; label/aliases; alias≠lineage
**Decision.** Identity is a URI compared as an opaque string, never
resolved; `canonical-alias` (identity) is split from `replaces` (lineage).
**Customer.** BSI's twin-catalog ID collision is a measured composition
failure; all three authorities maintain parallel identifier schemes
(×1,219 / ×188 / ISM labels) — `aliases[]` is their typed home; revisions
must not silently substitute (auditor reality).
**Simplicity.** "Where does this control live?" has one answer; no
import-context namespacing to teach.
**Complexity ↓.** Deletes the entire profile merge/combine algebra and the
resolution spec — the single largest 1.x implementation cliff; kills
`alt-identifier` props before they return.
**Trade-off.** Authorities must govern stable URIs (Authority-tier duty) —
the alternative is the measured status quo: mutable `tree/main` CSV links.

## D3 — Content manifest, sealed mode, two digest domains, canonical forms
**Decision.** Manifest = local resolution table with package- and
semantic-digests per object; attestations excluded; JCS with
empty-omission; decimal as canonical string; semver-normative bundle
composition.
**Customer.** Air-gapped estates (defense) must validate offline; the
deleted FedRAMP registry is the measured cost of network-coupled trust;
CR26 references external submission schemas — signed structured bundles are
the operating reality.
**Simplicity.** One file answers "what is in this bundle and is it
intact"; verification states are enumerable; no fixed-point puzzles.
**Complexity ↓.** Replaces per-tool ad-hoc integrity conventions and 1.x's
non-answer to tamper evidence; deterministic composition replaces
dependency guesswork.
**Trade-off.** Two digests at Authority tier; JCS must be implemented
correctly (test vectors provided); one more file to ship.

## D4 — Nine shallow types; documents are renderings
**Decision.** A graph of nine shallow types; document shapes leave the
normative core.
**Customer.** #2118/#2112 are customers (CSA, BSI) being rejected by
another framework's document conventions; **CR26 already operates
documents-as-views in production**; every GRC tool normalizes documents
into a database on ingest anyway.
**Simplicity.** Nine flat records versus eight deep, positional document
trees; learnable in an afternoon.
**Complexity ↓.** Nine shallow types **replace eight deep document models**
(OSCAL 1.2.2, including its March-2026 Mapping Model); the layout-dispute
class becomes structurally impossible.
**Trade-off.** Legal document reality must be re-covered (D7); rendering
templates are real work; RMF readers relearn "System".

## D5 — Component absorbs System; identified authorizations; inductive boundary rule
**Decision.** One Component type; explicit `authorizations[]` with ids and
member scoping; inheritance across a declared authorization requires a
typed basis, checked edge-locally.
**Customer.** FedRAMP's leveraged authorizations and KRITIS supplier chains
*are* "your system is my component"; multiple concurrent ATOs per service
are the norm; the legal boundary is where liability attaches — auditors
need it addressable, and absence must never be a negative assertion.
**Simplicity.** One composition mechanism instead of two ontologies; each
boundary check is a one-hop rule.
**Complexity ↓.** Deletes the System/Component duality and multi-hop
traversal machinery (induction covers chains); the historical
interconnection-prop cluster dies into typed structure.
**Trade-off.** A component that hides its authorization evades the trigger
— policed by publication duties and assessment practice, stated as R12.

## D6 — One Implementation edge
**Decision.** comp-def linkage and SSP implemented-requirements collapse
into one typed relation with per-clause scoping.
**Customer.** A professional authoring team publicly abandoned component
definitions because complexity exceeded value (PR #8); FedRAMP's daily CRM
and inheritance are exactly this edge's fields; shared responsibility is
per-clause in reality.
**Simplicity.** One relation to learn; responsibility and inheritance are
fields, not conventions.
**Complexity ↓.** Deletes a whole duplication axis and its
synchronization problem.
**Trade-off.** Comp-def marketplaces republish as Component+capabilities —
mechanical migration.

## D7 — Attestation with bi-modal verification
**Decision.** Attestation binds the content-manifest digest; verification
yields Full Match or Semantic Match; DSSE profile contract; provenance map.
**Customer.** Authorizing officials sign documents; lawyers subpoena the
exact view; annotation stripping is a legitimate hygiene right — both
truths are customer facts and the state machine serves both.
**Simplicity.** Two named verification outcomes instead of undefined
"signature broke, nobody knows why".
**Complexity ↓.** Replaces per-vendor signing conventions with one
contract; the H1 forgery vector and the P7 hash cycle are unrepresentable.
**Trade-off.** DSSE-profile maintenance; provenance maps are renderer work.

## D8 — Deviation sub-object
**Decision.** One typed disposition record with a state machine, attachable
where deviations occur; the audited channel for every recognized weakening.
**Customer.** Four historical FedRAMP extensions encoded the identical
state machine four times; CR26 carries corrective actions; BSI audit
practice runs on documented Abweichungen — regulators want weakening
*auditable*, not forbidden.
**Simplicity.** One concept, one state machine, one place to look.
**Complexity ↓.** Replaces five prop-based workflow encodings and ad-hoc
exception fields.
**Trade-off.** State-machine governance lives in stdlib; richer workflows
extend via facets.

## D9 — Statements collection; modality lattice; parties array; honest durations; small parameter algebra
**Decision.** Identified clauses with per-clause modality/parties/
parameters; a normative modality partial order (incl. may-only/DARF NUR);
elapsed vs. calendar durations; a closed scalar algebra.
**Customer.** 3/3 authorities converge on modality (BSI ×1,006, CR26 force
×328 with exactly this code set, ISM style guide); BSI's **347 nested
pseudo-controls** are the measured cost of missing clause granularity;
CR26's `affects[]` is an array (shared responsibility is bedrock); CR26's
`bizdays` is a real deadline unit whose meaning depends on calendars —
pretending otherwise computes wrong deadlines for the customer; DARF NUR is
German normative language, now machine-checkable for the first time.
**Simplicity.** One statement shape for every framework; a printable
lattice instead of folklore about which modality changes are "weaker".
**Complexity ↓.** The single largest prop consumer (BSI grammar, 100 % of
statements) and the 216-defect class disappear; control-splitting
workarounds become unnecessary; no schemas-in-parameters ever.
**Trade-off.** Multi-statement rendering is slightly harder than one blob;
calendar-periods introduce an explicit calendar dependency — honest, and
fail-closed rather than silently divergent.

## D10 — Registered facets; capability declarations; fail-closed; private: harmless by definition
**Decision.** Extensions are schema-validated, federated, exact-pinned;
semantic effect is declared; undeclared registered facets are dangerous by
default; `private:` facets are compliance-invisible by definition.
**Customer.** BSI's 12,059 ns-qualified props with CSV "schemas" are the
measured cost of contractless extension; three tools treating one facet
three ways (preserve/interpret/refuse) is the interoperability failure GRC
buyers actually hit; internal tool bookkeeping needs a legal outlet.
**Simplicity.** "What does this extension mean to my tool" has a decidable
answer; smuggling semantics into the escape valves is self-defeating
rather than policed.
**Complexity ↓.** Kills the props mechanism *and* the incentive to fork
custom Metaschema extensions: the sanctioned path (publish a JSON Schema at
your own domain) is cheaper than either; no central approval queue to
route around.
**Trade-off.** Fail-closed produces hard stops where 1.x guessed (R9) —
deliberate; facet semver is real governance (softened by pinning).

## D11 — SP 800-53 as Canonical Reference Facet; oscal-stdlib
**Decision.** NIST's conventions become the shipped-by-default standard
library, registered under the same rules as everyone.
**Customer.** Every non-NIST authority (CSA in #2118, BSI in the census)
is a customer harmed by 800-53 conventions in core; NIST itself keeps
out-of-the-box primacy and visible leadership.
**Simplicity.** One rulebook for all frameworks — no privileged ontology to
special-case.
**Complexity ↓.** Core carries zero document conventions forever; #2050's
externalization direction completed rather than patched.
**Trade-off.** stdlib release engineering needs an owner; launch optics
(R5).

## D12 — The complete, bounded extension surface
**Decision.** Eight evidence-priced stdlib facets + an open framework-facet
category + annotations; one candidate parked pending verification; ISM
needs zero.
**Customer.** Every stdlib facet cites counted instances (terminology 75/
188, reporting ~40, effectivity 17×paths, security-objectives ×4,494 …);
nothing was invented for elegance.
**Simplicity.** The whole extension surface fits on one page; "where does
my data go" is a lookup, not a debate.
**Complexity ↓.** >70 % of all counted prop instances vanish into kernel
mechanics with **no** replacement facet — the largest single simplification
in the design; unverified reviewer deletions are parked, not executed
(complexity of churn also counts).
**Trade-off.** Medium-confidence facets carry an explicit verification
debt.

## D13 — Bounded selection; identity-addressed ops; per-operation weakening rules; deterministic resolution
**Decision.** Selection by set-ref or three predicates; a closed op
vocabulary addressed by ids; weakening rules per operation with Deviation
as the audited escape; ordered application, same-target conflict = error,
chaining as the only override, no auto-merge.
**Customer.** ISM's 5,557 membership props and CR26's class variants exist
*because* 1.x tailoring was too expensive to be the single source —
baselines are the customer's daily bread, which is exactly why "exclude ⇒
Deviation" was **rejected**: it would drown every ISM classification
baseline and FedRAMP class in pseudo-deviations. CR26's deadline
tightening is the measured case for declared tightening directions.
**Simplicity.** Eight operations you can list from memory; a resolution
algorithm that fits on half a page (Appendix B); failures explain
themselves.
**Complexity ↓.** Replaces the profile-resolution spec *and* general JSON
Patch (whose positional fragility both hostile passes condemned) —
upstream errata can no longer silently repoint downstream tailorings.
**Trade-off.** Less expressive than arbitrary patching by design (R10);
authoring UX must make clause-level edits fluid.

## D14 — Eight primitives, one bounded conditional, no general-purpose expression language
**Decision.** A closed rule set with mandatory rationale-on-failure; one
≤1-hop predicate vocabulary shared with selection.
**Customer.** #2118's defining pathology — a rule nobody can justify —
is a customer-facing failure; parameter-conditioned allowed values are
real interchange semantics in all three corpora.
**Simplicity.** A rule interpreter, not a language runtime; 2-a.m.
failures print their reason.
**Complexity ↓.** CEL (and every future DSL negotiation) stays out; the
complexity balloon has no dark corner to re-inflate into.
**Trade-off.** Genuinely complex framework logic lives in the framework's
own tooling — if it cannot be a primitive, it is not an interchange rule.

## D15 — Core passive; normative feature × tier matrix
**Decision.** Core validates and preserves, computes nothing semantic;
Portable computes with fail-closed; Authority publishes with duties; one
normative matrix.
**Customer.** The customer-facing disaster is a tool that half-understands
a bundle and proceeds — P7-B3's silent-ignore state; RFC-0024's
approved-format slot needs one checkable tier to point at (Portable).
**Simplicity.** "What may this tool do" is a table lookup; the two v0.4
tier contradictions are gone.
**Complexity ↓.** Prose-allocated conformance (the 1.x pattern of
implementation-defined behavior) is abolished.
**Trade-off.** Corpus maintenance is standing engineering.

## D16 — Three migration guarantee levels
**Decision.** Native / compatibility-facet / opaque-preservation, per
element; "information-preserving for the supported corpus."
**Customer.** Adopters must know exactly what survives conversion — a
false "lossless" costs them at audit time.
**Simplicity.** "What did I lose" becomes a query over declared levels.
**Complexity ↓.** Replaces an unprovable universal claim with three
checkable ones; route-around formats (CR26) get absorbed instead of
competed with.
**Trade-off.** Three levels are more documentation than one lie.

## D17 — Declared non-goals
**Decision.** Flows, template accreditation, narrative grammar, PCI
customized approach, ISO management-system clauses, and executable proof
are named as *not covered here*.
**Customer.** Customers are harmed more by silent gaps than by declared
ones; each named gap has a stated home or a stated owner.
**Simplicity.** The spec's edge is drawn, so nobody argues about fog.
**Complexity ↓.** Kernel growth toward BPMN/ISO-MSS territory is refused
explicitly.
**Trade-off.** Coverage tables must be re-earned as targets are taken on.

## D18 — Fenced XML transit projection
**Decision.** One-way JSON→XML with strict XSD guaranteed for
kernel+stdlib only (transit-safe schema subset); third-party facets opaque
unless publisher-mapped.
**Customer.** Defense data diodes with XSD deep inspection are an
installed base; a promise of universal strict XSD would be a lie (P4-H5's
math is right).
**Simplicity.** XML is an encoding, like Base64 — never authored, never
round-tripped.
**Complexity ↓.** JSON-only conformance survives intact; no second
authoring format re-enters.
**Trade-off.** Third-party facet transit is guard-policy-dependent (R11) —
stated, not hidden.

## D19 — Engine positioning; accurate on-ramps; sunset trigger
**Decision.** Ship as a semantic core compiling to 1.x during transition;
name avoids 2.0/profile/kernel; #58 and #2050 cited as live, #2115/#2116
as closed positions; RFC-0024's five-CSP clause recorded.
**Customer.** The RFC-0024 wave (deadlines 2026/2027) is customers'
sunk-cost reality — freezing it would harm the very adopters this design
serves.
**Simplicity.** One public story: an engine under your existing
obligations.
**Complexity ↓.** Avoids a fork of the ecosystem's attention; the
dual-model window is bounded by a declared trigger.
**Trade-off.** Dual-model maintenance until sunset (R8).

## D20 — Mapping as the ninth kernel type
**Decision.** A shallow first-class crosswalk object with IR 8477/OLIR
relationship codes, statement-level scope, provenance, confidence.
**Customer.** SCF's entire product is a 200+-framework mapping graph; CIS
and CSA ship mappings as core artifacts; CR26 itself carries 263
KSI→800-53 links; NIST just shipped a whole eighth model for this (March
2026) — demand could not be better attested.
**Simplicity.** Nine flat fields versus a full mapping document model with
uuid/metadata/revisions/props scaffolding.
**Complexity ↓.** Replaces the 1.2.2 Mapping Model; prevents the two exact
north-star violations that otherwise follow — mappings as relation-string
**props**, and SCF/CSA staying on **bespoke** Excel/JSON.
**Trade-off.** Ninth type (dogma retired with reasons); relationship
code-system governance (R13).

## D21 — Nested sets and normative sequence
**Decision.** Sets nest; `sequence` is a defined presentation-order field.
**Customer.** CSF's Functions→Categories→Subcategories, SCF's 34 domains,
ISO themes, CIS Controls→Safeguards, and ISM's `sort-id` ×1,150 are all
the same customer need: taxonomy and order.
**Simplicity.** One mechanism (sets-of-sets + integer order) for every
hierarchy in the corpus.
**Complexity ↓.** No return of group/part nesting on Requirements — the
#2118 attractor stays dead; order-as-prop stays dead.
**Trade-off.** Deep taxonomies mean set indirection instead of inline
nesting — deliberate.

---

## Rejected alternatives — same three tests, failed

| Rejected | Customer | Simplicity | Complexity |
|---|---|---|---|
| Normative XML / YAML conformance | serves toolchains, not content needs | two more byte-forms to teach | resurrects mapping + c14n |
| URN identity scheme | same DNS rot on rebrand | loses the documentation affordance | adds IANA friction for nothing |
| CEL / sandboxed CEL | no authority asked for a language | a runtime to embed and secure | the historical re-inflation site |
| General JSON Patch (RFC 6902) | breaks customers on upstream errata | positional paths are unreadable | recreates baseline-shatter — convergently condemned |
| Central approval registry | months-long queues drive flight to private: | one more gatekeeper to petition | the Rev4 registry died exactly this way |
| Grammar in the kernel | Procrustean for CSF/ISO/privacy customers | forces linguistics on everyone | replaces NIST's bias with BSI's |
| "exclude ⇒ Deviation" (P7-B2 part) | drowns every baseline customer in pseudo-deviations | thousands of records nobody reads | kills the mechanism absorbing 5,900+ membership props |
| Mapping as stdlib facet (P8) | third-party crosswalks own neither endpoint | facet-on-whose-object debates | regresses to relation-string props |
| Universal weakening detector | promises the customer what cannot be computed | undecidable "is this weaker" arguments | requires exactly the semantics engine we refuse to build |
| Separate System type · defaulted boundary boolean | overlapping ATOs unrepresentable · absence became a legal claim | two ontologies · silent negatives | duplication + negative-assertion hazard |
| Authority `variants` carrier on Requirement (v0.6 cycle) | authority-variance is 1-of-3 (CR26 only) and its mechanism — Tailoring — exists | a second way to say "per-class differs" | fails the D22 promotion bar on tests 1 and 2; new kernel structure taxing every validator |

## The structurally-dead category — the north star's largest win

Membership matrices (ISM ×5,557; CR26 subsets + per-class lists), inline
class variants (`varies_by_class`, 79 CTL overlays), sort-ids (×1,150),
per-object revision props (×2,202 + CR26 `updated[]` everywhere), UUID/
attachment/import plumbing, and 216 pseudo-placeholders — **over 70 % of
all counted prop instances across three authorities** — disappear with no
replacement construct at all, because the kernel mechanism they were
imitating (sets, tailorings, L0 versioning, manifests, typed parameters)
now exists and is cheap. That is the measurable meaning of "no more props,
less bespoke": most extension was never extension — it was a core deficit,
and the deficit is closed.

---

# Amendments — v0.6 cycle, review round 1 (2026-07-21)

Backlog items #1, #2, #4, #5, #7 decided; rows leave the backlog per its
standing rule. Spec changelog IV.7 carries the same table; normative text
in the specification's D9/D10/D13/D20/D21/D22.

## D22 — Kernel promotion rule *(new)*
**Decision.** Promotion from facet space into the kernel requires all
three: **≥ 2-of-3 independent authority encodings** · **one shared
computation** every generic tool must perform · **one vocabulary that fits
all corpora without flattening**; and a candidate whose kernel *mechanism*
already exists is absorbed by that mechanism, never by a new field
(assurance levels: 3-of-3 encoded, yet level-as-a-Set — level-as-a-field
is the 5,301-marker corpse).
**Customer.** Every kernel field is a permanent tax on every Core
validator; only the census may levy it. The rule was implicit until App. F
Q22 forced it into words — and "why isn't X kernel" disputes are customer-
facing friction (the #2118 class: rules nobody can justify).
**Simplicity.** The bar is three countable questions; a promotion PR that
cannot show its three passes is rejected without further argument.
**Complexity ↓.** Ends promotion-by-advocacy, the historical re-inflation
channel by which cores grow until they need a metaschema.
**Trade-off.** A genuinely novel semantic with one national encoding waits
in a facet for a second authority — the kernel lags evidence, never leads
taste.

### D22 (rev, same cycle) — The anticipated-convergence path
**Decision.** Promotion is also permitted at 1-of-3 when a major census
authority ships and depends on the semantic, general use is credibly
anticipated (argued here, in the register), and the absorption clause
holds. Such promotions carry evidence tier **anticipated**, are re-verified
at every corpus addition, and demote back to facet space after two gate
cycles without materialized convergence.
**Customer.** The census population is three; treating its consensus as a
ceiling would make the kernel hostage to the historical accident of which
three authorities published first. FedRAMP wanting a thing, plus a credible
argument everyone else will too, is customer evidence — one tier below
measured, and labeled as exactly that.
**Simplicity.** One extra clause, same three-question shape, plus a clock.
**Complexity ↓.** Without the path, anticipated-general semantics ship as
facets, harden in tooling, and cost a migration when convergence arrives.
**Trade-off.** The kernel can now be wrong in a new way — which is why the
tier label and the demotion clock are not optional.

### The anticipated-path re-audit of the facet space (2026-07-21)

Every stdlib facet re-checked under the amended rule:

| Facet | Today | Anticipation case | Verdict |
|---|---|---|---|
| `terminology@1` | 1-of-3 (CR26 FRD: 75 terms, 188 aliases; alias-resolution computation measured, 264/264) | every national framework publishes terminology | **Kernel candidate** — the strongest anticipated case; final shape (carrier object vs. root-Set hosting) decides with the gate-2 schemas → backlog #6 re-scoped |
| `reporting-obligation@1` | 1-of-3 (CR26 `notification[]`) | NIS2 / DORA / CRA are notification-duty regimes — the incoming EU wave is *made of* reporting deadlines | **Anticipated candidate** — revisit at gate 2 with the declaration promotion (backlog #8) in place; promote when an EU corpus lands |
| `effectivity@1` | 1-of-3 (CR26 `info.effective`) | every regulation has effective dates and transition periods | Absorption check first: lifecycle + L0 versioning cover part of it; what remains is a gate-2 question, not a promotion yet |
| `security-objectives@1` | 1-of-3 (BSI C/I/A/Auth) | C/I/A is universal in theory | Stays facet — fails test 3 measured: values ("1"/"0") share no scale with anyone; anticipation cannot cure a vocabulary that already flattens |
| `statement-grammar@1` | 1-of-3 encoded (BSI ×1,006) | grammar is universal in theory | Stays facet — the rejected-alternatives table already names the corpse: kernel grammar replaces NIST's bias with BSI's |
| `assessment-criteria@1` | 2-of-3 (BSI `documentation` ×959 + CR26 artifacts/key_tests) | — | Stays facet — passes test 1, fails test 3: free-text document names vs. per-class artifact lists vs. KSI tests are irreconcilable shapes |

## D22-applied — Terminology hosting: root-Set normative, carrier rejected *(backlog #6, gate 2)*
**Decision.** A glossary is hosted as `terminology@1` on a RequirementSet —
typically the corpus root — whose id, version, and lifecycle govern it; a
dedicated carrier object (or tenth kernel type) is rejected. Normative in
the stdlib descriptor: `uses-term` relations resolve against the nearest
hosting Set; an unresolvable term ref is a Portable-tier validation error.
**Customer.** The D22 anticipated path opened the kernel door; the
absorption clause walked through it first: the existing mechanism (facet
on a Set) measured 264/264 reference resolution with zero new structure.
**Simplicity.** No tenth type; the ledger claim "nine shallow types"
survives its strongest challenger.
**Complexity ↓.** Identity, versioning, lifecycle, and digests come free
from the host Set — a carrier would reimplement all four.
**Trade-off.** A glossary shared by several corpora needs its own hosting
Set (a one-member Set is legal and cheap) — accepted; re-opens only if a
measured multi-corpus glossary corpus arrives (D22 clock discipline).

## P9-applied — Reference taxonomy: closure vs. landmark *(backlog #16, closed 2026-07-21)*
**Decision.** Two reference classes, normative: **closure-required**
references MUST resolve in-bundle (Set `members[].ref`; Tailoring
`selects[].set-ref`, `excludes[].ref`, operation `requirement-ref` +
statement existence; Implementation `component-ref`/`requirement-ref` +
the D5 `basis-ref` against the component's authorizations; Finding
`assessment-ref`/`requirement-ref`; Mapping `source/target-scope`
statement ids WHEN the endpoint is in-bundle). **Landmark** references
resolve outside the bundle by design (Mapping endpoints, party/authority
URIs, evidence refs, external schema/reference URLs, attestation
subjects — self-verifying via their digests). Parties get no kernel
type: the D22 test scores 0-of-3 (no census corpus publishes party
objects; CR26 `affects[]` are strings).
**Customer.** P9b-1 measured the contradiction: 1,008 Mapping endpoints
+ every party URI in the shipped corpus resolve to nothing, under a
primitive whose text said "a bundle that doesn't close doesn't
validate." Crosswalks own neither endpoint — external endpoints are the
normal case, not a defect.
**Simplicity.** One question per reference: does the bundle promise it?
**Complexity ↓.** No party plumbing; no forced vendoring of foreign
catalogs into every bundle that maps to them.
**Trade-off.** A consumer resolving a landmark ref needs the other
bundle — exactly what Mapping provenance and pinning are for.

## P9-applied — Facet enforcement executable *(backlog #17, closed 2026-07-21)*
**Decision.** The Portable-tier rule runs: stdlib facet payloads
validate against the normative descriptors; non-stdlib facets validate
against the bundle-pinned schemas (the manifest pin is the registry);
`private:` is ignored by definition; anything else is unregistered ⇒
error. Pinned facet-schema files are themselves existence- and
digest-verified.
**Customer.** P9-1's probe: a corrupt payload plus
`unregistered-dangerous-facet@99` validated green — the 1.x
valid-and-meaningless pathology reborn. Now both are vectors, both fail.
**Simplicity.** The manifest already carried the registry; enforcement
is a lookup plus a schema check.
**Complexity ↓.** No warning tier, no guessing tool: the three legal
states (validated, pinned-validated, ignored-private) are exhaustive.
**Trade-off.** Publishing a facet now genuinely requires publishing its
schema — which was always the contract.

## D10 (rev 2) — Declaration-audit promotions *(backlog #8)*
**Decision.** The three under-declared stdlib facets promote their
`modifies-semantics` declarations: `security-objectives@1` → `[selection]`,
`effectivity@1` → `[selection]`, `reporting-obligation@1` → `[assessment]`.
`cr26/scope@1` remains the exemplar that already declares `[selection]`.
The normative schemas at gate 2 ship these declarations; bundle stubs
update at the next converter run.
**Customer.** The user directive states the principle plainly: **a tool
that cannot handle a facet must stop working on that data.** Fail-closed
only engages when the declaration is honest — a facet declaring `[]` while
actually carrying selection or assessment semantics is the silent-ignore
corpse (P7-B3) wearing a conformance badge.
**Simplicity.** The declaration says what the payload does; no consumer
guesses.
**Complexity ↓.** Under-declaration is the cheap lie that reintroduces
props semantics (meaning invisible to the contract); this closes it for
the shipped stdlib.
**Trade-off.** Real fail-closed stops in tools that ignored these facets —
deliberate, and exactly the stops the user directive demands.

## D9 (closure note) — No duration union; unit-class boundary stays strict *(backlog #3)*
**Decision.** Closed without change. The elapsed-duration vs.
calendar-period split keeps its strict unit-class boundary; no union type
enters the algebra.
**Customer.** Zero measured crossings — the 51 first-pass flags were
base-absent authority variants, a ceremony question resolved under the
D13 rev (backlog #2), not a typing question.
**Simplicity.** A union type would exist to serve zero counted cases.
**Complexity ↓.** The fail-closed calendar rule stays the only rule;
nothing new to implement.
**Trade-off.** If a future corpus ships a genuine crossing, the item
re-enters the backlog with its count — the standing rule works in both
directions.

## D9 (rev) — Parameter `label` + `default` *(backlog #1)*
**Decision.** Optional `label` (display handle, never an identifier) and
`default` (advisory, type-valid) on parameter declarations. Resolution
never substitutes a default silently; binding remains `set-parameter`-only.
**Customer.** BSI labels ("regelmäßig") + `values[]` on 179 requirements,
exiled to L2 `param-extras` for want of two optional fields.
**Simplicity.** Two scalars; no resolution semantics touched.
**Complexity ↓.** Empties a whole L2 residue class (drains at the next
converter run).
**Trade-off.** A default that consumers *expect* to auto-apply will
surprise them once — the silent-substitution corpse says surprise them.

## D10 (rev) — `by-statement` payload keying *(backlog #7)*
**Decision.** Facet payloads addressing individual statements MUST key
them `by-statement: {sid: payload}`; a key naming no statement of the host
is a validation error.
**Customer.** 1,015 statements' payloads across six facets already ride
this converter convention; a second producer inventing divergent keying
would fracture per-clause alignment for every consumer.
**Simplicity.** One shape to learn; checkable without facet knowledge.
**Complexity ↓.** Pre-empts a per-facet addressing zoo.
**Trade-off.** Facets with exotic addressing needs (ranges, pairs) must
model them inside the payload — deliberate.

## D13 (rev) — Deviation duties bind at consumption tier *(backlog #2)*
**Decision.** Authority-tier Tailorings are normative source: the
per-operation Deviation requirements do not apply to them; weakening
classification is still computed and reportable. Consumer-tier Tailorings
keep the full table.
**Customer.** 29 variant-only CR26 rules + 5 KSI variants forced the
converter to synthesize base prose to have something to "deviate" from —
ceremony without a wronged party; the authority publishing variance *is*
the norm being varied.
**Simplicity.** One question decides the duty: who published the
Tailoring?
**Complexity ↓.** No `variants` carrier enters the kernel (rejected — see
table above; fails D22 on tests 1 and 2); synthesized-prose flags and
converter pseudo-Deviations disappear.
**Trade-off.** "Which class eases the base" becomes a report a tool runs,
not a record the authority writes — acceptable because the measured easing
count across 111 CR26 class-variant moves is zero.

## D20/D21 (rev) — Supplement pattern named; `supplements` registered *(backlog #5)*
**Decision.** D21 names the supplement pattern normatively (own-prefix
authorship + shadow set with interleaved sequence + attachment by
reference); D20 registers `supplements` as a stdlib relationship extension
code beyond IR 8477 — non-chaining, OLIR exports MAY down-translate to
`supports`.
**Customer.** Q23's asker ("where did profile add/alter go?") speaks for
every 1.x profile author; multi-authority membership is proven in the
bundles.
**Simplicity.** The verb split is teachable in one line: modifying is
Tailoring, adding is authorship.
**Complexity ↓.** No injection mechanism, no merge provenance, no resolved
artifacts with tool-run lineage.
**Trade-off.** One code added to an adopted external vocabulary — fenced
by the extension marking and the down-translation rule.
