# Semantic OSCAL — Ideas

A design study for **OSCAL Semantic Core**: compliance data as a graph of nine
shallow, globally identified objects instead of eight nested document models.
This repository holds the handbook, the draft specification, eight converted
corpora (the three-authority census base plus five validation frameworks),
and a ready-to-install Claude skill that applies the standard.

Status: **pre-1.0, evidence-gated.** The specification is at v0.5 with a v0.6
feedback backlog open. Nothing here is endorsed by NIST, BSI, ACSC, or FedRAMP.

---

## Why

OSCAL 1.x is *rigid where frameworks legitimately differ* and *contractless
where meaning actually lives* — and every measured pathology flows from one
side of that paradox:

- **Nobody used it.** FedRAMP's RFC-0024 (Jan 2026) records that of 100+ Rev5
  authorizations processed in 2025, **zero** submissions used OSCAL — the
  program the standard was co-designed with, in the year machine-readability
  became its central theme.
- **Valid and meaningless are compatible states.** The German Grundschutz++
  catalogs carry **12,059 namespace-qualified props** whose "schema" is a set
  of CSV files behind mutable links. Inside them sit **216 pseudo-placeholders**
  (`{{einem anerkannten Standard}}`) that imitate parameter syntax where it has
  no meaning — several contradicting the adjacent prose. Every OSCAL validator
  on earth certifies these documents as flawless.
- **The same model keeps getting rediscovered.** FedRAMP built CR26 on a green
  field in 2026 with no props mechanism, and its typed fields correspond almost
  one-to-one to the German prop names: `modal_verb` ↔ `force`,
  `target_object_categories` ↔ `affects`. Two teams, no coordination, one
  target model — convergent evidence about what the domain demands.
- **Membership gets hand-maintained twice.** 59 % of all ISM props are a
  5,301-entry applicability matrix duplicating information ACSC *also* ships as
  eight profile documents, because consuming the profile mechanism costs more
  than inlining.

Full argument with sources: [Chapter 1 — Why This Exists](semantic-oscal/references/ch01-why-this-exists.md).

## What it is

Nine kernel objects — Requirement, RequirementSet, Tailoring, Mapping,
Component, Implementation, Assessment, Finding, Attestation — plus two
sub-objects (Deviation, Authorization). Documents become renderings of the
graph rather than the unit of exchange.

Three layers, strictly separated:

| Layer | Holds | Contract |
|---|---|---|
| **Kernel** | What all three corpora were measured to need: binding force, clauses, typed parameters and deadlines, membership, aliases, history | Normative, fixed |
| **Facets** | Framework-specific vocabulary | Registered, schema-pinned, machine-checked; fail-closed on unknown semantics |
| **Annotations** | Rendering hints and chrome | Invisible to compliance |

Design rules that follow: failures are made *unrepresentable* rather than
forbidden (bound `{param:}` tokens, identity-addressed tailoring); integrity
uses two digests — package (bytes sent) and semantic (meaning approved) — so
signatures survive repackaging; and tools that don't understand something must
carry it or stop with a reason, never guess.

Every design decision is scored against four tests — *simpler · closer to
measured customer needs · no more props · less need for bespoke JSON* — in the
[Decision Rationale Register](drafts/oscal-semantic-core-decision-rationale-register.md).

Start here: [Chapter 2 — The Core in One Hour](semantic-oscal/references/ch02-the-core-in-one-hour.md),
or the [one-file explainer](semantic-core-explainer-concept-files-workflow.md)
if you prefer diagrams.

## How to use this repo

### As a Claude skill

[`semantic-oscal/`](semantic-oscal/) is an installable skill that guides an
agent through authoring, validating, and migrating Semantic Core content. Its
[SKILL.md](semantic-oscal/SKILL.md) turns the 15 handbook chapters into 14
numbered requirements, each with reference chapters and companion examples.

Install by copying the directory into your skills folder, or unpack
`SKILL_semantic-oscal.zip`:

```
~/.claude/skills/semantic-oscal/     # user-level
.claude/skills/semantic-oscal/       # project-level
```

It carries 18 worked examples plus an index in [`examples/`](semantic-oscal/examples/) — a
self-consistent bundle from a zero-facet minimum requirement through
attestations with semantic digests — the converters in
[`scripts/`](semantic-oscal/scripts/), and, since gate 2 (2026-07-21), the
**normative kernel JSON Schema**, six stdlib facet descriptors, a
54-vector conformance corpus, and the reference validator
([`validate_core.py`](semantic-oscal/scripts/validate_core.py)) — which
validates the eight corpus bundles plus the example bundle green:
5,470 manifest-listed objects with both digests re-verified each (plus 8
manifest checks and 13 example objects shape-checked without digests),
every object matching exactly one kernel shape.

### As a human

[`one-page-apps/semantic-core-reader.html`](one-page-apps/semantic-core-reader.html)
is a zero-dependency, single-file bundle reader: open it in a browser, drop
in any bundle folder from `converted_examples/`, and it renders the objects
for humans — statements with their modality lattice, facets and annotations
visually separated, and one-click re-verification of both SHA-256 digests
per object, entirely client-side (nothing is uploaded anywhere). The five
stages of the compliance graph are working views, not just explanations:
a navigable catalog tree with baselines, a live Tailoring resolver
(selection expansion, same-target conflict detection, before→after lattice
verdicts), a filterable crosswalk table, an implementation inspector that
checks inheritance basis-refs, and an assessment board with bi-modal
attestation verification (Full/Semantic Match/Tamper). Since v1.2 the
stages also *author*: build your own Tailoring (with the weakening rules
enforced live — easings demand a Deviation, unit-class crossings are
blocked, same-target conflicts refused), assemble a system of assets that
carry controls, and run a checklist assessment that mints real Assessment
and Finding objects back into the graph — all exportable as
schema-conformant JSON.

### As a specification

- [`drafts/oscal-semantic-core-v0.5-specification.md`](drafts/oscal-semantic-core-v0.5-specification.md) — the normative draft
- [`drafts/oscal-semantic-core-decision-rationale-register.md`](drafts/oscal-semantic-core-decision-rationale-register.md) — 22 decisions, each scored against the north star, with rejected alternatives
- [`drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md`](drafts/oscal-semantic-core-v0.6-spec-feedback-backlog.md) — the living input queue for v0.6: items enter with counts, leave via register entries

### As evidence

[`converted_examples/`](converted_examples/) holds the three census corpora
(the evidence base the architecture was derived from) plus five further
frameworks converted as validation targets — each with a computed coverage
report: a bundle of objects, pinned facet schemas, and a manifest carrying
both digests per object.

The census corpora (gate 1):

| Corpus | Source | Emitted | Coverage |
|---|---|---|---|
| [AU.ISM](converted_examples/AU.ISM/ism-coverage-report.md) | ACSC ISM, OSCAL 1.1.2 catalog, 1,150 controls | 1,150 Requirements · 322 Sets | 36,161 / 36,161 leaf values |
| [geman.bsi](converted_examples/geman.bsi/bsi-coverage-report.md) | Grundschutz++ v2026-07-16, OSCAL 1.1.3 (MS-TLS dropped by decision — defects reported to BSI) | 651 Requirements carrying 999 statements · 221 params with label/default · 162 Sets | 49,431 / 49,431 |
| [FedRAMP-CR26](converted_examples/FedRAMP-CR26/cr26-coverage-report.md) | CR26 bespoke JSON, v2026.07.14.01 | 292 Requirements · 373 Mappings · 91 Sets · 4 Tailorings | 7,294 / 7,294 |

Validation corpora (converted 2026-07-21; the model held without kernel
changes beyond the same morning's already-decided D9-rev parameter
`label`/`default` — evidenced by the census corpus (BSI ×179), decided
before these conversions ran, and first exercised by DE.C3A):

| Corpus | Source | Emitted | Coverage |
|---|---|---|---|
| [BE.CyFun](converted_examples/BE.CyFun/cyfun-coverage-report.md) | CCB CyberFundamentals 2025, BASIC + ESSENTIAL resolved catalogs (one corpus) | 218 Requirements · 124 Sets (3 cumulative baselines) | 4,312 / 4,312 |
| [CIS.Controls](converted_examples/CIS.Controls/cisc-coverage-report.md) | CIS Controls v8.1, OSCAL 1.1.3 | 171 Requirements · 34 Sets (IG1–3 baselines, asset/function categories) | 5,493 / 5,493 |
| [CIS.Ubuntu2404](converted_examples/CIS.Ubuntu2404/cisb-coverage-report.md) | CIS Ubuntu 24.04 LTS Benchmark v1.0.0 | 312 Requirements · 635 Mappings (v7+v8) · 79 Sets (4 recovered profile baselines) | 20,698 / 20,698 |
| [DE.C5](converted_examples/DE.C5/c5-coverage-report.md) | BSI C5:2026, OSCAL 1.2.2 | 623 Requirements · 190 Sets (basic baseline + additional criteria) | 5,868 / 5,868 |
| [DE.C3A](converted_examples/DE.C3A/c3a-coverage-report.md) | BSI C3A v1.0, OSCAL 1.2.2 (GS++ grammar family) | 30 Requirements · 30 typed parameters (first `label`/`default` use) · 9 Sets | 1,093 / 1,093 |

The reports declare every conversion rule with counts, and report source
defects rather than repairing them — the BSI run surfaces all 213
pseudo-placeholders in the current GS++ catalog for the authors' queue
(the census figure of 216 included MS-TLS's 3, dropped from the corpus
2026-07-21).

### Orientation

[`oscal-models-overview-1x-vs-semantic-core.md`](oscal-models-overview-1x-vs-semantic-core.md)
maps the eight OSCAL 1.x document models onto the nine objects, with reusable
Mermaid sources.

## House rules

Three rules govern the handbook, and you should hold it to them:

1. **Evidence tiers, always labeled** — every claim is *measured*,
   *designed-for*, or *hypothesized*. Corrections ship with the same
   prominence as the original claim.
2. **Concepts enter through the corpus** — no mechanism is introduced
   abstractly. If a concept can't be motivated by something an authority
   actually shipped, it isn't in the spec.
3. **Every "don't" names its corpse** — prohibitions cite the measured failure
   they prevent, with the number attached. A rule that can't name what it
   prevents is a rule to delete.

## Contributing

Objections are the point — [Appendix F](semantic-oscal/references/appendix-f-objections.md)
is an adversarial FAQ, and review findings land in the v0.6 backlog with their
diffs on the record. Items enter the backlog with counts and leave via a
decision recorded in the register; an item that can neither be evidenced nor
closed after two gate cycles gets deleted.
