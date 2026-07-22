# The OSCAL Semantic Core Handbook
# Appendix F — Objections and Answers

**Purpose:** the adversarial FAQ. Every question below is phrased the
way an opponent would phrase it — several *were* phrased this way, by
the eight hostile review passes whose verdicts shaped v0.5 — and the
answers cite counts, corpses, and, where the objection landed, the
correction it forced. §F.5 is the section most FAQs don't have: the
punches that connected.

---

## F.1 "Why not X" — the technology objections

**Q1. Why not CEL, Rego, or any real expression language for
constraints? Eight primitives is a toy.**
Because the toy is the point, and the language is the trap — twice
over. First, complexity: a weekend validator cannot embed a policy
engine, and the validator ecology (many cheap implementations, no
monoculture veto) is a governance control, not a nicety. Second,
rationale-rot: the defining pathology of the flagship's constraint
dispute was a rule *nobody could explain*; expression languages make
inexplicable rules cheap to write. The design's own history seals it:
an early draft casually allowed "selection by facet query" and was
caught smuggling an undefined language one decision after banning
languages. Eight primitives, versioned — the ninth ships with counts
and two implementations, never with a grammar.

**Q2. Why not JSON Patch for tailoring? It exists, it's standard.**
Because Patch addresses *positions* and compliance addresses
*identities*. Two independent tailorings of one catalog, one
legitimate re-issue that reorders an array — and every positional
path silently points at the wrong clause. Version-pinning doesn't fix
it (pinned positional patches still rot on re-issue; the register
records this rejected alternative verbatim). Identity addressing
(`requirement-ref` + `statement-id`) survives reordering by
construction, and the same-target-twice error makes conflicts loud
instead of last-wins quiet.

**Q3. Why abandon XML and Metaschema? Half of government runs on
XML.**
Abandon is the wrong verb; *fence* is the right one. The census
answer first: the authorities themselves author in JSON and bespoke
JSON — the American program's current rules are not OSCAL XML, they
are a custom JSON file. The kernel therefore has one authoring
serialization, and XML becomes a **one-way transit projection** with
a guaranteed strict XSD for the kernel+stdlib subset (D18) — XML
consumers keep validation, XML pipelines keep working, and nobody
maintains dual authoring truth (the corpse: every dual-format
ecosystem's drift). Metaschema dies for the complexity-budget reason:
a meta-language that generates three bindings is infrastructure spend
the census showed nobody's *semantics* ever needed.

**Q4. Why exactly one serialization? YAML is friendlier.**
Because digests. Semantic integrity rests on canonical bytes (JCS),
and every additional authoring format is another canonicalization
seam — the empty-omission and float rules were hard enough to pin
for *one* format (the conformance vectors exist because reviewers
found real fragmentation cases). YAML remains fine as a local
authoring convenience that *compiles* to the JSON — what it can't be
is a second truth.

**Q5. Why not fix 1.x profiles instead of replacing merge?**
Merge strategies exist to arbitrate identity collisions; global
identity makes the collisions unconstructible; a fix for an
impossible problem is dead code with a specification. The measured
history: merge/keep/combine semantics generated a dispute class and
implementation divergence for a decade. Legacy profiles that
genuinely depended on merge get §14.2's honest instruction — resolve
in the old world, migrate the result.

**Q6. Why not RDF/OWL — this is obviously a knowledge graph?**
It is a graph; it is not a *Semantic Web deliverable*, and the
difference is the complexity budget's whole thesis. The failure mode
this architecture answers is not "insufficient ontological
expressiveness" — it is 22,000 annotation props and three national
authorities routing around a standard that spent its budget on
infrastructure. Nine shallow types with typed edges give the graph;
JSON Schema gives the weekend validator; a triple store gives
neither. Anyone who wants RDF can project it — losslessly, from a
model this simple.

## F.2 "You went too far" — the architecture objections

**Q7. Nine types is arbitrary. Why not one generic node with typed
properties?**
Because "one generic node with typed properties" is the 1.x prop
system with better marketing — the exact architecture whose measured
cost opened the book. The nine types are not invented; they are the
convergence table's output: the shapes three governments
independently built. Fewer types pushes semantics back into
string-keyed soup; more types failed the census test (no third
authority needed them).

**Q8. A Core tier that computes *nothing* is useless.**
It is the most load-bearing tier in the design, and it exists because
a reviewer proved the alternative broken: a Core allowed to "partially
understand" semantics has a silent-ignore state — the tool that
validates a bundle while skipping the facet that changes its meaning.
v0.5's answer (P7-B3, accepted): Core is *passive* — validate,
digest, resolve, **preserve** — and every semantic computation begins
at Portable, behind the capability gate. Useless is what the old
world's "conformant" was; passive is honest.

**Q9. Two digests is crypto-overengineering.**
One digest forces a choice between two lies: bind bytes (and every
legitimate re-serialization or annotation-strip breaks signatures) or
bind some ad-hoc "meaning" (and tampering hides in the gap). The
Rev4-era answer was hash-plumbing props nobody could verify across
tools. Two digests, two jobs: the package digest answers "are these
the bytes," the semantic digest answers "is this the approved
meaning" — and bi-modal verification (Full/Semantic Match) is the
verdict shape auditors actually need. The cost is one extra SHA-256
per object; the converters paid it 3,066 times without noticing.

**Q10. Fail-closed will drive users to fork or lie.**
It would — if it fired at the noun. It fires at the *verb*: a bundle
full of unknown selection facets opens, validates, forwards, and
displays; it halts at the moment someone selects, with a three-part
message naming the blocker and the doors. The alternative is on the
record: three real tools, one preserving, one guessing, one
refusing, all "conformant." A warning-then-proceed is the guessing
tool with a seatbelt sticker. Forks come from *unpredictable* stops;
gate-at-the-verb plus printed rationale is the anti-fork design.

**Q11. Global URIs — so you've centralized naming. And URIs rot.**
Neither. Nothing resolves: identifiers are compared as strings,
never dereferenced (D2), so sealed environments and dead domains
change no verdict. Nobody grants prefixes: authorities mint under
names they already control, and the transparency log remembers
without gatekeeping. Rot is handled where it actually occurs — as an
identity *event*, with `canonical-alias` carrying the forwarding
address the old world never had. The corpse on this grave is the
registry that vanished with its repository.

**Q12. `may-only` is a Germanism the world doesn't need.**
The gate measured it: DARF NUR ×0 in the current German corpus — the
lattice anticipates it, nobody has used it yet, and this appendix
says so out loud. It stays because it is lattice-clean, costs one
code, and encodes a real regulatory move (exclusive permission) that
prose otherwise smuggles. If the corpus never votes for it, the
versioned code system has a removal path — that is what "closed but
versioned" is *for*.

## F.3 "You didn't go far enough" — the scope objections

**Q13. Where's the process/workflow model? Compliance is workflows.**
Declared non-goal (D17), with a corpse: the one process-flow
structure in the census (`flows[]`, ×1) is a *diagram*, and diagrams
are linked resources, not requirement data. The state machines the
model does own — Deviation, Finding — are the ones three authorities
encode as data. BPM engines exist; this is their input, not their
competitor.

**Q14. Where's risk modeling — likelihood, impact, scoring?**
In facets, where legitimate methodological diversity belongs.
`security-objectives@1` carries the ratings authorities actually
ship (measured: C/I/A/Auth ×4,494); scoring *methodologies* differ
by framework and by fashion, which is the exact profile of a facet
and the exact anti-profile of a kernel field. `privacy-assessment@1`
is parked for the same discipline: no facet designed from memory.

**Q15. Statements without mandatory grammar are just prose with
extra steps.**
The German corpus answers in both directions. With grammar: 1,006
machine-decomposed clauses, QA-checkable, defect-findable (the 216
and the 9 were found *because* grammar is data). Without: ISM's
1,149 declarative statements convert at Core tier with zero facets
and zero loss. Mandatory grammar would have made the second corpus a
second-class citizen — R2 accepts the bifurcation because the
alternative excludes half the world's authoring cultures.

**Q16. One reference hop can't express real inheritance chains.**
The objection (H4, on the record) was answered by *moving the rule*,
not denying the need: the boundary rule is edge-local and inductive —
each inheritance edge names its basis, each link verifies its link —
so chains of any depth check with one hop per step. Multi-hop
*expressions* stay banned; multi-hop *chains* work fine. The SaaS→
PaaS→IaaS walk in Chapter 9 is the constructive proof.

## F.4 The political objections

**Q17. NIST will never bless its own demotion.**
The arrangement demotes nothing NIST earned and everything the
structure imposed. 800-53's content keeps default primacy — shipped
in every stdlib bundle, first among equals — as the **Canonical
Reference Facet NIST owns**. What ends is one framework's document
conventions constraining every other framework's documents, whose
measured cost was a national catalog flattened into props. "Standard
library, not constitution" is a *promotion* to the role the content
actually plays; the optics risk is in the register (R5), not denied.

**Q18. Publishing this Osbornes the 1.x adoption wave.**
Which is why the name avoids "2.0," the posture is *engine*
(kernel-authoritative, valid 1.x generated for every regulator that
asks), and the dual window ends at a declared, measurable sunset
trigger rather than an announcement. The deadline wave is real and
useful; freezing it would be strategic self-harm, and D19 exists to
not commit it.

**Q19. The five-provider clause is a cute loophole, not a strategy.**
It is recorded without endorsement because it needs none: it is the
incumbent policy's *own* mechanism, and it swings both ways — the
door through which a format like this becomes approved without
permission, and equally the door through which something worse
replaces the incumbent if its second act disappoints. Quoting a
published rule is not a gimmick; it is reading the terrain.

**Q20. You have zero users and a hypothesis.**
Correct, and the specification says so on its cover — "well-supported
architecture hypothesis," claims narrowed to evidence tier, with the
v0.6 gate defining exactly what execution must prove. What exists is
not users but *user-shaped data*: three governments' complete corpora
at 100 % declared coverage, 93,259 values, and every design decision
traceable to something an authority shipped. That is more empirical
grounding than most 1.0s carry; it is still a hypothesis, and the
gate is where hypotheses go to become claims or die.

**Q21. The compat facet is just props with a registration number.**
It is exactly that *if the clock stops* — which is why the clock is
the contract: intended deprecation in the descriptor, residue as a
per-release KPI, and every current row with a named exit (ISM 539 →
narrative decision; BSI 179 → the D9 default question; CR26 29+5 →
the D13 ceremony question; CTL 79 → gate-3 catalog resolution). A
waiting room with a clock and exits is a migration tool; the same
room without them is the smell §14.6 names.

## F.5 The punches that landed — objections that changed the text

The credibility section. **"Your weakening rule is a slogan"**
(P7-B2): correct — "weakening ⇒ Deviation" was only enforced for
modality; v0.5 replaced it with per-operation laws. **"Core can't do
JCS and be minimal"** (P8-E1): correct — `attestation-binds` moved
to Portable; Core went fully passive. **"Lossless is unprovable and
your export claim is false"** (P6): correct — three guarantee levels
and a published equivalence relation replaced both adjectives.
**"Your canonicalization fragments on empty arrays"**: correct —
empty-omission became a normative rule with test vectors.
**"651 controls"**: wrong by 347 — the nested-control recount and
the public erratum. And this very week, our own converter's **"51
unit-class crossings"** dissolved under a refined counter into 0
true crossings and 51 base-absent variants — Appendices A and C
corrected on the record. The pattern is the point: this project's
answer to a good objection is a diff, and its answer to a bad one is
a count. To file yours: Chapter 15's door — bring corpus cases,
bring numbers, expect both in return.
