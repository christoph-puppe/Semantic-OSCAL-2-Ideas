# OSCAL Semantic Core — Decision Rationale Register (v0.5)
## Every decision, justified against the three north-star criteria
### 2026-07-18

**The three tests (session directive).** Every decision below is justified
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
