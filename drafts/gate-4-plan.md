# Gate 4 — Engines + Measurement Plan
### v0.6 gate item 4 (spec IV.5.4 + backlog #18/#24 residuals) · prepared 2026-07-22

**Purpose.** Gate 4 measures the two economic claims that justify the
architecture: **cheap to implement** (the weekend-validator acceptance
test) and **safe to leave** (bidirectional 1.x export). On the way it
builds the three engines the conformance corpus has named gaps for:
DSSE verification (#24), bundle-composition semver (D3.5), and
`conditional-apply` instantiation (B.1.8) — closing backlog #18.

## 1. Work items, in dependency order

1. **DSSE verification engine (#24).** `dsse-envelope@1` fixes payload
   (canonical Attestation, annotations excluded) and PAE per DSSE v1
   but deliberately does not pin an algorithm — the reference engine
   pins **Ed25519 (RFC 8032)**, implemented dependency-free in the
   validator (key distribution stays authority-local, like template
   accreditation R6; the engine takes trusted keys as input). Tier
   integration: `authority-proven` now additionally requires a
   verifying signature when trusted keys are supplied; without keys the
   validator reports `envelope present — signature UNVERIFIED`.
   Vectors: signed→proven · tampered payload→attestation-binds FAIL ·
   wrong key→claimed · payload≠attestation canonical→FAIL (fixture
   keypair committed; deterministic envelopes).
2. **Bundle-composition engine (D3.5).** `--compose A B`: facet pins in
   the same major line resolve to the highest pinned minor with BOTH
   payload sets re-validated under the winner; major clash / digest
   mismatch / re-validation failure / same-id-and-version objects with
   differing semantic digests = reported errors, never silent picks.
   New vector family `composition-vectors.json`.
3. **`conditional-apply` engine (B.1.8).** Instances = {id, trigger:
   one B.2 predicate (≤1 hop, no nesting), enforcement: one
   instantiated primitive, rationale}; verdict where the trigger holds,
   no-op elsewhere; FAIL format per B.1.8. New vector family
   `conditional-vectors.json`.
4. **Bidirectional export suite (IV.5.4).** `export_oscal.py`: every
   catalog-shaped bundle → syntactically valid OSCAL 1.2.2 catalog JSON
   (validated against the official NIST catalog schema, fetched to
   `sources/nist/`); facets/annotations ride namespaced props (JSON
   string values) so `import_oscal.py` (a generic importer, not the
   corpus converters) can reconstruct the objects; round-trip verified
   by **semantic-digest equality per object**. Supported corpus =
   catalog-shaped bundles (declared; the lifecycle bundle's five types
   export at gate 5 / OSCAL SSP-family scope).
5. **Second-language validator (the weekend test).**
   `validate_core.ps1` — PowerShell 5.1, ZERO installs, the stock
   auditor's Windows box. Authored from the specification + appendices
   + conformance corpus; every place the spec text under-determines the
   implementation is a FINDING. Target: all 129+new vectors + full
   corpus digests; wall-clock reported.
6. **Measurement report** (`drafts/gate-4-measurement.md`): LoC per
   implementation (counted, same counter), vector pass rates,
   wall-clocks, and the comparison baseline — an OSCAL 1.2.2
   validator+resolver (compliance-trestle, LoC counted from a fetched
   sdist). Authorship recorded honestly (AI-assisted, spec-driven);
   the measured claims are spec-sufficiency and implementation SIZE,
   which do not depend on who types.

## 2. Acquisitions (public domain, to `sources/`)

NIST OSCAL 1.2.2 catalog JSON Schema (usnistgov/OSCAL release asset) ·
compliance-trestle sdist (PyPI, for LoC counting only, not a runtime
dependency).

## 3. Definition of done

- #24 closed: signature verification live behind trusted-key input;
  vectors prove proven/claimed/FAIL paths; bundles report the unverified
  state distinctly.
- #18 closed: both named vector families exist and pass; the engines
  that run them are in the reference validator.
- Export: 100 % of catalog-shaped bundles export schema-valid OSCAL
  1.2.2 and round-trip to semantic-digest equality; failures are
  reported per object, never summarized away.
- The PS validator passes the full conformance corpus; divergences =
  findings; LoC + hours + baseline in the measurement report.
- Register entries for every decision the engines forced; backlog,
  spec IV.10, README, zip updated; all green throughout.
