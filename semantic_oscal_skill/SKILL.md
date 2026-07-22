---
name: semantic_oscal
description: Guidelines and requirements for authoring, validating, and migrating to Semantic OSCAL (OSCAL Semantic Core).
---

# Semantic OSCAL Skill Requirements

When triggered, this skill guides the agent in applying the OSCAL Semantic Core standard correctly. The chapters of the OSCAL Semantic Core Handbook serve as the normative requirements for this skill.

## Core Directives (Chapters as Requirements)

You must strictly adhere to the guidelines detailed in the handbook chapters linked below:

### Requirement 1: Paradigm Alignment & Motivation
- **Description:** Align all compliance data into a graph of nine shallow, globally identified objects (Requirement, RequirementSet, Tailoring, Mapping, Component, Implementation, Assessment, Finding, Attestation) and 2 sub-objects (Deviation, Authorization). Ensure strict separation of concerns between kernel semantics, registered facets, and rendering annotations.
- **Reference Document:** [Chapter 1 — Why This Exists](references/oscal-semantic-core-handbook-ch01-why-this-exists.md) and [Chapter 2 — The Core in One Hour](references/oscal-semantic-core-handbook-ch02-the-core-in-one-hour.md)

### Requirement 2: Identity, Versioning, and Lifecycle Management
- **Description:** Govern namespaces strictly. Use canonical-alias vs. replaces rules correctly to ensure revision and rebranding integrity. Every reference to an object must use its unique identifier.
- **Reference Document:** [Chapter 3 — Identity, Versions, and Lifecycle](references/oscal-semantic-core-handbook-ch03-identity-versions-lifecycle.md)

### Requirement 3: Writing Requirements, Statements, and Parameters
- **Description:** Requirement clauses must have statement-level granularity to allow precise tailoring, mappings, and responsibility assignment. Adhere strictly to the modality lattice (obligations vs. permissions). Deadlines must be structured using explicit, typed parameters or duration systems instead of free-text placeholders.
- **Reference Document:** [Chapter 4 — Writing Requirements: Statements, Modality, Parameters](references/oscal-semantic-core-handbook-ch04-writing-requirements.md)

### Requirement 4: Sets, Hierarchy, and Baselines
- **Description:** Use nested `RequirementSets` as the singular taxonomy mechanism. Define baselines using membership sets rather than inline properties.
- **Reference Document:** [Chapter 5 — Sets, Hierarchy, and Baselines](references/oscal-semantic-core-handbook-ch05-sets-hierarchy-baselines.md)

### Requirement 5: Tailoring Semantic Core
- **Description:** Define changes via selection rules and identity-addressed operations. Apply per-operation weakening rules and require a `Deviation` object where needed. Follow the deterministic tailoring resolution algorithm.
- **Reference Document:** Detailed chapter reference is pending (Chapter 6). Refer to tailoring resolution logic in Chapter 12 and Appendix B.

### Requirement 6: Facet Extensions
- **Description:** Extend the kernel only via registered, schema-pinned facets (`modifies-semantics`, fail-closed rules) or annotations (purely styling/chrome). Never add custom top-level fields to kernel objects.
- **Reference Document:** [Chapter 7 — Facets: Extending Without Fracturing](references/oscal-semantic-core-handbook-ch07-facets-extending-without-fracturing.md)

### Requirement 7: Mappings and Crosswalks
- **Description:** Map relationships using `Mapping` objects with IR 8477/OLIR relationship semantics. Always map at the statement-level scope for high precision.
- **Reference Document:** [Chapter 8 — Mappings and Crosswalks](references/oscal-semantic-core-handbook-ch08-mappings-and-crosswalks.md)

### Requirement 8: Systems, Components, and Inheritance
- **Description:** Structure system components, composition boundaries, and responsibility matrices. Implement CRM inheritance and the edge-local boundary rule for multi-tenant chains.
- **Reference Document:** [Chapter 9 — Systems, Components, and Inheritance](references/oscal-semantic-core-handbook-ch09-systems-components-inheritance.md)

### Requirement 9: Assessment, Findings, and Deviations
- **Description:** Define assessment methods, track finding statuses and action deadlines, and manage the lifecycle of deviations as an audited weakening channel.
- **Reference Document:** [Chapter 10 — Assessment, Findings, Deviations](references/oscal-semantic-core-handbook-ch10-assessment-findings-deviations.md)

### Requirement 10: Integrity, Attestation, and Air-Gaps
- **Description:** Apply both package digests (for byte transport) and semantic digests (for meaning preservation). Follow the DSSE profile checklist and attestation structures for air-gapped security assurance.
- **Reference Document:** [Chapter 11 — Integrity, Attestation, and Air-Gaps](references/oscal-semantic-core-handbook-ch11-integrity-attestation-airgaps.md)

### Requirement 11: Validator Implementation
- **Description:** Ensure structural validation, facet schema checking, and resolution conformance. Adhere to JCS (JSON Canonicalization Schema) and tailoring resolution logic.
- **Reference Document:** [Chapter 12 — Building a Validator (The Weekend Chapter)](references/oscal-semantic-core-handbook-ch12-building-a-validator.md)

### Requirement 12: Safe Consumption
- **Description:** Handle unknown facets and annotations with standard fail-closed / warnings. Manage rendering, templates, and actionable error UX gracefully.
- **Reference Document:** [Chapter 13 — Consuming Content Safely](references/oscal-semantic-core-handbook-ch13-consuming-content-safely.md)

### Requirement 13: Migration Playbooks
- **Description:** Translate OSCAL 1.x structures (catalogs, profiles, SSPs, etc.) or legacy formats to Semantic Core objects preserving semantic equivalence.
- **Reference Document:** [Chapter 14 — Migration Playbooks](references/oscal-semantic-core-handbook-ch14-migration-playbooks.md)

### Requirement 14: Governance and Ecosystem
- **Description:** Adhere to conformance tiers, deprecation policies, registry usage, and the anti-#2118 change proposal workflow.
- **Reference Document:** [Chapter 15 — Governance, Conformance, and the Ecosystem](references/oscal-semantic-core-handbook-ch15-governance-conformance-ecosystem.md)

## Appendices Reference

- [Appendix A: Shapes reference](references/oscal-semantic-core-handbook-appendix-a-shapes.md) — The nine types + sub-objects, field by field.
- [Appendix B: Primitives, operations, predicates](references/oscal-semantic-core-handbook-appendix-b-primitives-ops-predicates.md) — One page each, with rationale and failure messages.
- [Appendix C: Code systems](references/oscal-semantic-core-handbook-appendix-c-code-systems.md) — Modality (with the lattice diagram), lifecycle, deviation states, responsibility, mapping relationships, duration units, confidence.
- [Appendix D: stdlib facet catalog](references/oscal-semantic-core-handbook-appendix-d-stdlib-catalog.md) — The eight standard facets with schemas, examples, and candidates.
- [Appendix E: Worked corpora](references/oscal-semantic-core-handbook-appendix-e-worked-corpora.md) — KONF.14.1, IEC-CSO-IIR + class tailoring, ISM control, SCF mapping.
- [Appendix F: Objections and answers](references/oscal-semantic-core-handbook-appendix-f-objections.md) — Adversarial FAQ (why not CEL / XML / JSON Patch, etc.).
- [Appendix G: Glossary](references/oscal-semantic-core-handbook-appendix-g-glossary.md).
