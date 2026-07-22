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
