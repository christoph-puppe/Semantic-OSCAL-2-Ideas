# OSCAL Semantic Core — v0.6 Spec-Feedback Backlog
### Consolidated open design questions from gate item 1 and the first review round · 2026-07-19

Every item carries its evidence (measured where possible), its
proposed disposition, and its source. This file is the input queue
for the v0.6 specification revision; items leave it only via a
decision recorded in the register.

| # | Item | Evidence | Proposed disposition | Source |
|---|---|---|---|---|
| 6 | **Terminology hosting shape — RE-SCOPED (v0.6 cycle).** Kernel home now permitted under the D22 anticipated-convergence path (terminology audited as the strongest anticipated candidate); remaining question is shape only: dedicated carrier object vs. root-Set hosting. | 75 terms / 188 aliases / 264 refs, all resolving; anticipated: every framework publishes terminology | Decide the shape with the gate-2 schemas; either way, document | CR26 converter; D22 rev audit |
| 10 | **CTL/ODP addressing.** External-catalog ODP assignments (79 CTL overlays) need statement-level addresses in the NIST catalog. | 79 entries parked L2 | Resolves with the NIST catalog conversion (gate 3); then decide control-level parameters vs. statement map | CR26 converter |
| 12 | **Localized-text type for human-readable fields.** Only `statement.prose` and choice labels are `{lang: string}`; `title` (×3,041), Mapping `rationale` (×373), and most facet-payload free text are bare strings — converter payloads were internally inconsistent (BSI guidance tagged ×1,004 vs CR26 description bare ×180; ISM compat carried 300 bare `prose` beside 1,150 tagged). | Field inventory 2026-07-20 (user review) | Introduce a `text` primitive `{BCP-47: string}` for kernel human-text fields; normative facet-authoring rule: payload free text MUST be text-typed, identifiers stay strings. Payload harmonization **shipped for ISM + CR26** (2026-07-21: T(v) per converter; zero bare fields in authored payloads — remaining bare are verbatim L2 quotations, term headwords per the label rule, and stub annotations, all declared in the coverage reports; BSI rerun pending source access). Kernel `text` primitive decides at v0.6 | Review round 1, finding 3 |

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
(companion to the 216/issue #58; never a spec change). Numbering stays
stable — closed numbers are not reused.

**Standing rule for this file:** items enter with counts, leave with
register entries. An item that can neither be evidenced nor closed
after two gate cycles is deleted — backlogs rot like registries do.
