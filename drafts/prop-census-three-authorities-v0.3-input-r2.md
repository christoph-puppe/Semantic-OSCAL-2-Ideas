# Prop-/Feld-Zensus dreier Autoritäten → First-Class Citizens für OSCAL 2.0
## r2 — ERSETZT r1 (Stand 2026-07-16)

**Änderung gegenüber r1 (Direktive):** Die FedRAMP-Analyse basiert jetzt
ausschließlich auf der **aktuellen autoritativen Ausgabe** — dem CR26-JSON
(`fedramp-consolidated-rules.json`, Titel „FedRAMP Consolidated Rules for
2026", **Version 2026.07.14.01**, last_updated 2026-07-14, Repo
`FedRAMP/rules`, samt offiziellem JSON Schema). Das Rev4-OSCAL-Extension-
Registry von 2021 ist nur noch **historischer Anhang A** und fließt nicht mehr
in die Ableitung ein. CR26 ist kein OSCAL und hat keine `props`; die
Zensusfrage lautet für FedRAMP daher: *Welche Felder trägt das aktuelle
Format, und absorbiert der Kernel sie zu 100 %?* (Absorptionstest gem.
Strawman v0.2 §9.)

### Provenienz

| Quelle | Artefakt | Version | Status |
|---|---|---|---|
| **FedRAMP** | `FedRAMP/rules` → fedramp-consolidated-rules.json + Schema | **2026.07.14.01** | autoritativ („source of truth"), Public Preview 2026 |
| ACSC/ASD | ISM-Katalog (offizieller GitHub-Mirror) | v2026.06.18 | autoritativ |
| BSI | Grundschutz++-Katalog / Mindeststandard TLS | 2026-07-03 / 2026-04-23 | autoritativ (Entwurfsphase) |
| FedRAMP (historisch) | FRMR-Repo `FedRAMP/docs` | — | von FedRAMP selbst als **Legacy** markiert |
| FedRAMP (historisch) | Rev4-Extension-Registry (18F-Repo) | fedramp1.2.1 (2021) | nur Anhang A |

### ⚠ Erratum zu usnistgov/OSCAL#2118 (aus r1, weiterhin gültig)

Frühere Scans übersahen verschachtelte Controls. Korrekt: GS++ **998**
Controls (651 Top-Level), **996** exakt [statement, guidance]; **11.985 von
13.204** Props ns-qualifiziert; **216** Pseudo-Platzhalter. Fußnotentext für
den Thread siehe r1/Chat — alle qualitativen Aussagen halten.

---

## 1. ACSC ISM — 1.150 Controls, 8.958 Props (unverändert aus r1)

Namespace `https://cyber.gov.au/ns/ism/oscal/3.0` (sauber versioniert).
Props: `applicability` ×5.301 (NC/OS/P/S/TS), `sort-id` ×1.150, `revision`
×1.101, `updated` ×1.101 („Jun-26"-Strings), `essential-eight-applicability`
×256, `label` ×49. Alle Controls exakt `[statement]`.

**2.0-Abbildung:** Mitgliedschaft → RequirementSets; revision/updated → L0;
sort-id → sequence; label → aliases. **Facet-Bedarf: null.**

## 2. BSI — GS++ 998 + TLS 17 Controls, 13.315 Props (unverändert aus r1)

Grammatik-Cluster (modal_verb/action_word/result/… auf 100 % der Statements)
→ Kernel-Envelope + `statement-grammar@1`; Schutzziele (C/I/A/Auth ×~3,6k +
threats) → `security-objectives@1`; Taxonomie (sec_level/effort/tags/
documentation/practice) → `gspp-taxonomy@1`; alt-identifier ×1.219 + label →
`aliases[]`; 216 `{{…}}`-Werte → unrepräsentierbar.

---

## 3. FedRAMP CR26 — das autoritative Feldmodell (NEU)

Bestand: **246 Rules** in 17 Familien (AFC 16, AGU 20, CCM 19, CDS 21, CMU 3,
CPO 5, FRC 29, IEC 8, IVV 20, MAS 5, MKT 12, REC 16, SCG 9, SCN 17, SDR 5,
VDR 18, VER 23), **46 KSIs** in 10 Familien, **75 Definitionen** (FRD) mit
**188 Alias-Einträgen**, **79 CTL-Overlays** (800-53-Parameter/Guidance) in
14 Kontrollfamilien.

### 3.1 Feldzensus (normalisiert)

| Feld | Vorkommen / Enum | Semantik |
|---|---|---|
| `force` | 328 gesamt: **MUST 189, SHOULD 84, MAY 39, MUST NOT 11, SHOULD NOT 5** | Modalität als eigenes Feld |
| `statement`, `name` | je Rule/KSI | normativer Satz + Titel |
| `affects[]` | {Providers, Agencies, Assessors, Advisors, FedRAMP} | **Verpflichteter** (Adressat) als Feld |
| `terms[]` | 500+ Bindungen | Verweise ins kontrollierte Glossar (FRD) |
| `related[]` | ~80 | typisierte Querverweise |
| `timeframe_num` + `timeframe_type` | {hours, days, bizdays, months, years} | **typisierte Fristen** |
| `pain_timeframes.<sev>.{fir,iir,oir}` | je Klasse | Frist-Matrizen nach Schweregrad (N1–N4) × Berichtstyp |
| `varies_by_class.{a,b,c,d}` | überschreibt force/statement/timeframe/artifacts/parameters | **Inline-Tailoring** nach Zertifizierungsklasse |
| `notification[]{method,party,name,target}` | method ∈ {email, form, update, varies} | Meldepflichten als Daten |
| `artifacts.all[]`, `default_artifacts.{FRR,KSI}[]` | ~60 | **geforderte Nachweise** (Soll-Evidenz) |
| `following_information[]`(+`_bullets`) | 150+ | strukturierte Pflichtangaben-Listen |
| `examples[]{id, examples[], key_tests[]}` | Rules + KSIs | Beispiele und Schlüsseltests |
| `schema.{name,url}` | 20+ | Verweis auf Submission-Schemas (SDR, Incident Report, SCN…) |
| `corrective_actions[]`, `danger`, `note(s)`, `reference(+_url)` | verstreut | Eskalation, Warnungen, Rechtsquellen |
| `updated[]{date, comment}` | je Objekt (Daten bis 2026-07-14) | **Änderungshistorie pro Objekt** |
| KSI: `controls[]` | 263 Mappings (ac-2, cm-3, …) | KSI ↔ 800-53-Zuordnung |
| FRD: `term, definition, alts[], tag, reference, do_not_link` | 75 / 188 alts | Glossar mit Synonymen |
| `info.effective.{is, date.obtain/maintain/optional_adoption, grace…}` | je Familie × Pfad (20x/Rev5) | **Inkrafttretens-/Übergangsmetadaten** |
| `info.subsets.<G>.applicability.{affects, classes, paths, types}` | classes {A–D}, paths {Program, Agency}, types {20x, Rev5} | Anwendbarkeits-Matrix |
| `rev5_controls_list.{FAM}[]` | Baselines je Klasse B/C/D | Mitgliedschafts-Listen |
| `info.flows[]{nodes, steps{from,to,description}}` | IEC-Incident-Flow | **Prozessgraph als Daten** |
| `CTL.<FAM>.<id>.{parameters[], guidance[], varies_by_class}` | 79 | ODP-Festlegungen + Guidance-Overlays auf 800-53 |
| `web_name`, `short_name`, `status {stable, placeholder}`, `tag` | je Familie | Anzeige-/Lebenszyklus-Metadaten |

### 3.2 Der Befund: konvergente Evolution

Von OSCAL befreit hat FedRAMP auf der grünen Wiese **den Statement-Envelope
des Strawman nachgebaut**: `force` ist exakt das v0.2-Modalitäts-Codesystem
(inkl. MUST NOT / SHOULD NOT); Fristen sind typisierte Parameter;
`varies_by_class` ist Tailoring; `alts[]` sind Aliases; `updated[]` ist
Revisionshistorie; `subsets`/`rev5_controls_list` sind Set-Mitgliedschaft.
Wo 1.x-gebundene Autoren (BSI) dieselbe Semantik in flache Props pressen,
wählt Green-Field-FedRAMP typisierte Felder. **Zwei unabhängige Autoritäten,
zwei Wege, ein Zielmodell — das ist der stärkste empirische Beleg für die
Kernel-Architektur.**

### 3.3 Absorptionstest CR26 → Kernel v0.2/v0.3

| CR26-Feld | Zuhause | Status |
|---|---|---|
| force | `statement.modality` | ✔ deckungsgleich |
| statement / name | `statement.prose` / `title` | ✔ |
| related[] | `relations[]` | ✔ |
| id / web_name / short_name | L0-`id` / `label` / `aliases[]` | ✔ (aliases: 3. Autoritäts-Beleg) |
| status {stable, placeholder} | `lifecycle` | ✔ |
| timeframe_num/type | **Envelope-Delta v0.3:** Parametertyp `duration` {num, unit-Codesystem} | neu, klein |
| affects[] | **Envelope-Delta v0.3:** `statement.obligated-party` (Code/Ref) | neu, klein — 3/3 Autoritäten haben Subjekt-Semantik (BSI: target_object_categories im Grammar-Facet; CR26: Adressat) |
| pain_timeframes, varies_by_class | 4 Klassen-**Tailorings** (amends: modality/params/artifacts) | strukturell tot; Publikations-Ergonomie („alle Klassen in einem Objekt") = L4-View über resolved Tailorings |
| subsets.applicability, rev5_controls_list | **RequirementSets** | strukturell tot (3. Beleg des Mitgliedschafts-Musters) |
| CTL-Overlays (ODP-Werte, Guidance) | **Tailoring** auf das 800-53-Facet (set-params + amend/annotate) | strukturell tot |
| updated[] | L0 (version, supersedes, Manifest-Changelog) | strukturell tot (2. Beleg nach ISM) |
| schema.url, reference_url | typisierte L0-Links (rel = submission-schema / legal-source) | ✔ |
| do_not_link, web_name-Feinheiten | `annotations` | ✔ — erster legitimer Praxis-Anwendungsfall des Annotations-Ventils (reine Rendering-Hints) |
| terms[] + FRD (term/definition/alts/tag/reference) | **stdlib `terminology@1`** (neu): Definitions-Objekte mit Synonymen, Tags, Rechtsquellen; Statements binden Begriffe per Ref | neues Facet |
| notification[] + following_information | **stdlib `reporting-obligation@1`** (neu): {trigger, party, method, target, required-information[]} | neues Facet |
| artifacts / default_artifacts / examples / key_tests + KSI-Gestalt (statement + controls[]-Mapping) | **stdlib `assessment-criteria@1`** (ersetzt/erweitert r1-„automated-assessment"): Soll-Evidenz, Schlüsseltests, Beispiele, Mappings | Facet, erweitert |
| info.effective (obtain/maintain/grace/optional_adoption) | **stdlib `effectivity@1`** (neu): Inkrafttretens-/Übergangsfenster je Requirement/Set | neues Facet |
| corrective_actions, danger, note(s) | Deviation-`actions` / Prosa-Callouts (GFM) | ✔ |
| info.flows[] | **bewusst nicht absorbiert**: Prozessdiagramme sind kein Anforderungsmodell; Zuhause = referenzierte Diagramm-Ressource (L0-Link, z. B. Mermaid-Quelle) | out of scope, deklariert |

**Ergebnis: ~30 semantische Felder → 9 Kernel/Envelope, 12 stdlib-Facet,
8 strukturell tot, 1 deklariert out-of-scope, Rest 0.** Props: weiterhin
nirgends nötig.

---

## 4. Muster über alle drei Autoritäten (r2)

1. **Mitgliedschaft als Daten** — jetzt 3/3 (ISM applicability 5.557×,
   CR26 subsets + rev5_controls_list, BSI implizit via Doppelkatalog):
   RequirementSets müssen die *billige, einzige* Quelle sein.
2. **Modalität ist universell** — 3/3 (BSI modal_verb ×1.006, CR26 force
   ×328, ISM in Prosa): Kernel-Envelope bestätigt.
3. **Aliases sind universell** — 3/3 (BSI alt-identifier ×1.219, CR26 alts
   ×188 + web/short_names, ISM label + Alt-Nummern).
4. **Revisionshistorie je Objekt** — 2/3 explizit (ISM ×2.202, CR26
   updated[] überall): L0-Versionierung ist gemessener Bedarf, keine Kür.
5. **Typisierte Fristen & Adressaten** — CR26 liefert die Evidenz für zwei
   kleine Envelope-Erweiterungen (duration-Parameter, obligated-party).
6. **Workflow- und Evidenz-Semantik** sucht ein Datenmodell — CR26 baute es
   sich (notification, artifacts, key_tests); v0.3 gibt ihm registrierte
   Facets statt N proprietärer Formate.

## 5. Abgeleitete First-Class Citizens (r2, konsolidiert)

**Kernel/Envelope (v0.3):** `label` + `aliases[]{scheme, value}` ·
`Deviation`-Subobjekt · Parametertyp **`duration`** ·
**`statement.obligated-party`** · (`authorization-boundary`-Defaultfeld und
GFM-Tabellen aus dem Gemini-Pass unverändert)

**stdlib-Facets:** `statement-grammar@1` · `security-objectives@1` ·
`assurance-levels@1` · **`assessment-criteria@1`** (absorbiert KSI-Gestalt) ·
`privacy-assessment@1` · `system-context@1` · **`terminology@1`** ·
**`reporting-obligation@1`** · **`effectivity@1`**

**Strukturell tot (größte Kategorie):** Mitgliedschaft, Inline-Tailoring
(varies_by_class, CTL-Overlays), sort-id, Revisions-Props/-Felder,
UUID-/Schema-/Referenz-Plumbing, Platzhalterwerte.

**Annotations (legitim):** reine Rendering-Hints (do_not_link u. ä.).

**Deklariert out-of-scope:** Prozessfluss-Graphen (flows) — via Link auf
Diagramm-Ressourcen.

## 6. Abdeckungsnachweis (r2)

| Autorität | Einheiten | Kernel/Envelope | stdlib | Framework-Facet | strukturell tot | out-of-scope | Rest |
|---|---:|---:|---:|---:|---:|---:|---:|
| ACSC ISM (6 Prop-Namen) | 8.958 Props | 1 | 0 | 0 | 5 | 0 | **0** |
| BSI (16 Prop-Namen) | 13.315 Props | 4 | 6 | 5 | 1 | 0 | **0** |
| FedRAMP CR26 (~30 Felder) | 246 Rules + 46 KSIs + 75 FRD + 79 CTL | 9 | 12 | 0 | 8 | 1 | **0** |

Invariante erfüllt: **Props verboten, Abdeckung 100 %** — und die
FedRAMP-Zeile beruht jetzt auf dem Format, das seit dem 4. Juli 2026 in Kraft
ist, nicht auf einem Registry von 2021.

---

## Anhang A — Historisch: FedRAMP-OSCAL-Extension-Registry (Rev4, 2021)

*Nur zur Dokumentation der 1.x-Ära; fließt nicht in die Ableitung ein.*
60 registrierte Extensions (fedramp1.2.1): Implementierungs-Cluster
(implementation-status, control-origination…), Abweichungs-Workflows
(false-positive / operational-requirement / risk-adjustment /
vendor-dependency mit identischer State-Machine → historische Mitevidenz für
`Deviation`), Assessment-/System-/Privacy-/Plumbing-Cluster. Vollständige
Liste: `fr_props.json` (r1). Bemerkenswert: Das Registry selbst ist von
seiner kanonischen URL verschwunden (GSA-Repo gelöscht) — Link-Rot der
autoritativen Quelle als unfreiwilliger Beleg für L0 (stabile IDs, Manifeste,
Digests).
