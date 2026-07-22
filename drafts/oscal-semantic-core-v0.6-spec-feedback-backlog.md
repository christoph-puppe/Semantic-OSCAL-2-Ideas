# OSCAL Semantic Core — v0.6 Spec-Feedback Backlog
### Consolidated open design questions from gate item 1 and the first review round · 2026-07-19

Every item carries its evidence (measured where possible), its
proposed disposition, and its source. This file is the input queue
for the v0.6 specification revision; items leave it only via a
decision recorded in the register.

| # | Item | Evidence | Proposed disposition | Source |
|---|---|---|---|---|
| 6 | **Terminology hosting shape.** Converter hosts the glossary on the corpus root Set (`glossary-info` block); alternative: a dedicated carrier object. | 75 terms / 188 aliases / 264 refs, all resolving | Decide root-hosting vs. carrier at schema time (gate 2); either way, document | CR26 converter |
| 8 | **Declaration audit promotions.** Shipped stubs declare `[]` conservatively; corpora argue for: security-objectives → `[selection]`?, effectivity → `[selection]`?, reporting-obligation → `[assessment]`? (`cr26/scope@1` is the exemplar that already earns `[selection]`.) | App. D.12 table | Decide per facet with the normative schemas (gate 2) | App. D audit |
| 9 | **Seed code-set confirmation.** Finding states and assessment results are deliberately small seed sets. | Lifecycle corpus pending | Confirm/extend with gate-3 evidence; resist state-zoo growth | App. C.3/C.10 |
| 10 | **CTL/ODP addressing.** External-catalog ODP assignments (79 CTL overlays) need statement-level addresses in the NIST catalog. | 79 entries parked L2 | Resolves with the NIST catalog conversion (gate 3); then decide control-level parameters vs. statement map | CR26 converter |
| 11 | **Grammar-prop completeness as source QA.** 9 clauses carry MUSS in prose without `modal_verb` (grammar coverage 99.1 %). | Measured; queued with the 216 | Not a spec change — feeds the authors' queue (BSI#58 companion) | App. E.1 |
| 12 | **Localized-text type for human-readable fields.** Only `statement.prose` and choice labels are `{lang: string}`; `title` (×3,041), Mapping `rationale` (×373), and most facet-payload free text are bare strings — converter payloads were internally inconsistent (BSI guidance tagged ×1,004 vs CR26 description bare ×180; ISM compat carried 300 bare `prose` beside 1,150 tagged). | Field inventory 2026-07-20 (user review) | Introduce a `text` primitive `{BCP-47: string}` for kernel human-text fields; normative facet-authoring rule: payload free text MUST be text-typed, identifiers stay strings. Payload harmonization pending (converter T(v) pass, blocked on source corpora); kernel change decides at v0.6 | Review round 1, finding 3 |

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
rev; the elapsed/calendar unit-class boundary stays strict). Numbering
stays stable — closed numbers are not reused.

**Standing rule for this file:** items enter with counts, leave with
register entries. An item that can neither be evidenced nor closed
after two gate cycles is deleted — backlogs rot like registries do.
