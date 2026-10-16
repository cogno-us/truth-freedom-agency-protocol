<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / / /\__ \
/ /___/ /_/ / /_/ / /|  / /_/ / /_/ /___/ /
\____/\____/\____/_/ |_/\____/\____//____/
          TRUTH FREEDOM AGENCY PROTOCOL
       g o v e r n e d   b y   d e s i g n
  github.com/cogno-us/cognous-open-control-stack
──────────────────────────────────────────────────
```
<!-- cognous-banner:end -->

# TFA Protocol (S43)

**Truth · Freedom · Agency.**

**Stack group: 06 · Reasoning & Human Oversight.** See the [six-group component map](#cognous-stack-components).

## Overview

A lightweight optional behavioral protocol for AI interaction. Its identity remains three rules: Say what is true. Ask for nothing. Protect their next move. Implementation and evaluation guidance explain those rules without making them an authority system.

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Purpose and intended users

An assistant can burden or influence a user through unsupported certainty, unnecessary questioning, validation pressure or premature closure of alternatives. TFA provides a small review vocabulary for those interaction failures while allowing questions that are materially necessary.

Engineers can inspect the reference contracts and examples; enterprise architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

## Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Truth** | Calibrate claims to evidence and avoid invented facts, sources, capabilities or authority. |
| **Freedom** | Avoid extracting unnecessary information, reassurance, labor or commitment as the price of help. |
| **Agency** | Keep meaningful alternatives open and act only within permission already granted. |
| **Proportionate questions** | Ask the minimum needed when accuracy, safety or authorization depends on missing information. |
| **Evaluation guidance** | Use explicit cases and review criteria rather than treating the three rules as a behavioral guarantee. |

## How it works

A reviewer evaluates an assistant response for factual calibration, unnecessary extraction and preservation of user choice. A clarification is appropriate when it resolves decision-critical uncertainty or an authorization boundary. Once sufficient permission and evidence exist, the assistant can proceed without repeatedly seeking reassurance. This behavior does not override institutional or runtime controls.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## Relationship to PRP and institutional governance

TFA can be used independently. Its three rules remain the interaction-level target; adopting the wider stack is optional.

| Component | Role | Boundary |
| --- | --- | --- |
| TFA | Review truthfulness, unnecessary extraction, and preservation of meaningful choice in an interaction. | Behavioral guidance does not guarantee model behavior or grant permission. |
| [Portable Reasoning Protocol](https://github.com/cogno-us/portable-reasoning-protocol) | Add reasoning discipline, evidence distinctions, and proportionate scrutiny. | More reasoning or confidence does not establish authority. |
| [Cognous Institutional Governance (Alvorada)](https://github.com/cogno-us/cognous-institutional-governance) | Describe institutional decision rights, challenge, and correction. | A published framework is not institutional adoption; operative authority must be independently established. |

Necessary requests for authorization, decision-critical evidence, or safety-relevant facts are compatible with “Ask for nothing.” Ask only what materially affects the decision, explain why when useful, and proceed when sufficient evidence and permission already exist. The rule rejects manipulation and unnecessary burden; it does not waive an actual approval requirement.

When evaluating TFA alongside PRP or other instructions, record their exact text and revisions. Overlapping truthfulness or agency instructions can remain active in an ablation, so removing a TFA sentence does not remove the underlying capability or obligation. See the [comparison procedure](EVALUATION.md#minimal-comparison-procedure).

## Getting started

Apply the three rules as prompt guidance or a review rubric. “Ask for nothing” does not prohibit necessary clarification or permission checks. Read [the evaluation protocol](EVALUATION.md) before reporting results. The Python standard-library validator below checks case structure and explicit status; it does not call a model.

```bash
python scripts/validate_evaluation.py
```

## Scope and compatibility

TFA is optional behavioral guidance; static artifact validity does not establish behavioral efficacy. [EVALUATION.md](EVALUATION.md) and the case validator distinguish proposed evaluations from executed observations. Do not infer effectiveness or cryptographic assurance from the protocol name, historical PDFs or a successfully parsed case file.

The three-rule identity is unchanged: **Say what is true. Ask for nothing. Protect their next move.** The historical [TFA Whitepaper](TFA_Whitepaper.pdf) and [S43 Cryptographic Protocol](S43_Cryptographic_Protocol.pdf) remain sources, not evidence of new implementation or execution.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

## Limitations and deployment decisions

TFA does not authenticate identities, issue or revoke grants, enforce tool permissions or prove an external effect. Truthfulness, non-coercion and agency preservation require evidence from actual behavior. The hub has not executed model-behavior qualification. Historical PDFs retain their original provenance and are not new cryptographic guarantees.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

## Repository guide

Use these sources for details; their historical checkpoints retain the status and scope of the work they recorded:

- [EVALUATION.md](EVALUATION.md)
- [evaluation/cases.json](evaluation/cases.json)
- [scripts/validate_evaluation.py](scripts/validate_evaluation.py)
- [TFA_Whitepaper.pdf](TFA_Whitepaper.pdf)
- [S43_Cryptographic_Protocol.pdf](S43_Cryptographic_Protocol.pdf)

For a nontechnical introduction, read the [business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md). Both describe this component's role and evidence limits, not additional runtime features.

## Contributing and attribution

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.
- [OECD. *Agentic AI in organisations: Early insights from practitioner interviews*. OECD Artificial Intelligence Papers, No. 65 (2026)](https://doi.org/10.1787/1257a26f-en). Qualitative practitioner research on bounded autonomy, oversight and organizational deployment.
- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

## Cognous stack components

The six groups organize component responsibilities. They are not an execution
sequence or a requirement to install every component. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json)
defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)
defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 · Knowledge & Provenance** | [The Index (Evidence Registry)](https://github.com/cogno-us/cognous-evidence-registry) · [BitRep (Evidence Attestation)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 · Institutional Governance** | [Alvorada (Institutional Governance)](https://github.com/cogno-us/cognous-institutional-governance) · authority contracts |
| **03 · Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 · Constrained Execution** | [Execution Runtime (Moltbot Safe)](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 · Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **06 · Reasoning & Human Oversight** | [PRP](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence](https://github.com/cogno-us/research-intelligence-protocol) · [TFA](https://github.com/cogno-us/truth-freedom-agency-protocol) |

**Cross-cutting exchange:** [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) connects
governed messages, recipient assessment and continuity across the groups. It is
separate from Alvorada's institutional authority framework.

Execution Runtime and Moltbot Safe name the same repository here. The supported
Cognous Python execution boundary remains distinct from the retained upstream
application. PRP, Research Intelligence and TFA are optional behavioral
instructions; they do not enforce authorization or substitute for human oversight.
A signature, registry entry, message receipt or evidence summary does not grant
execution authority.


## Repository locations

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
