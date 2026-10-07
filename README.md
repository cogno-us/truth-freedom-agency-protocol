<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / / /\__ \
/ /___/ /_/ / /_/ / /|  / /_/ / /_/ /___/ /
\____/\____/\____/_/ |_/\____/\____//____/
               TRUTH FREEDOM AGENCY
       g o v e r n e d   b y   d e s i g n
  github.com/cogno-us/cognous-open-control-stack
──────────────────────────────────────────────────
```
<!-- cognous-banner:end -->

# TFA Protocol (S43)

**Truth · Freedom · Agency.**

## Overview

A lightweight optional behavioral protocol for AI interaction. Its identity remains three rules: Say what is true. Ask for nothing. Protect their next move. Implementation and evaluation guidance explain those rules without making them an authority system.

**Implementation status:** this README describes merged public reference work. Component acceptance, selection in the hub and execution of a qualification are separate facts. The selected revision for this component is `442d07b4891870abb1756fcb11c24ccf187706f4`; the [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/component-lock.json) is the source of that integration choice.

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

## Getting started

Apply the three rules as prompt guidance or a review rubric. “Ask for nothing” does not prohibit necessary clarification or permission checks. Read [the evaluation protocol](EVALUATION.md) before reporting results. The Python standard-library validator below checks case structure and explicit status; it does not call a model.

```bash
python scripts/validate_evaluation.py
```

## Evidence and supported scope

The hub selects TFA as optional behavioral guidance, with static artifact checks only. [EVALUATION.md](EVALUATION.md) and the case validator distinguish proposed evaluations from executed observations. Do not infer effectiveness or cryptographic assurance from the protocol name, historical PDFs or a successfully parsed case file.

The accepted [hub persistence-generation evidence](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/examples/control-plane-store-adoption/qualification-summary.json) records 915 Python tests in each of two repetitions, 35 matrix entries satisfying their gates and 120 separate mocked OpenShell tests. Those are aggregate hub results, not a per-component test count or a claim of production readiness. Optional behavioral layers receive static checks only. The [support ledger](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) separates implementation, execution and adoption.


The three-rule identity is unchanged: **Say what is true. Ask for nothing. Protect their next move.** The historical [TFA Whitepaper](TFA_Whitepaper.pdf) and [S43 Cryptographic Protocol](S43_Cryptographic_Protocol.pdf) remain sources, not evidence of new implementation or execution.

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

## Cognous stack components

[Stack hub](https://github.com/cogno-us/cognous-open-control-stack) · [Selected pins](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) · [Evidence and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)

Component links are navigation, not a requirement to install every component. The hub lock determines its supported integration.

| Component | Responsibility |
|---|---|
| [Agent Action Manifest](https://github.com/cogno-us/cognous-agent-action-manifest) | Declare the action before evaluating permission |
| [Agent Control Plane](https://github.com/cogno-us/cognous-agent-control-plane) | Evaluate proposals against authority and preserve the decision record |
| [Agent Replay Bundle](https://github.com/cogno-us/cognous-agent-replay-bundle) | Reconstruct what the retained records support |
| [Agent Governance Evidence Pack](https://github.com/cogno-us/cognous-agent-governance-evidence-pack) | Turn traceable runtime records into reviewable governance evidence |
| [Open Decision Evidence Standard](https://github.com/cogno-us/open-decision-evidence-standard) | Portable decision evidence across system and organizational boundaries |
| [Alvorada Experimental Workbench](https://github.com/cogno-us/alvorada) | Governed exchange and continuity for a bounded synthetic workflow |
| [Moltbot Safe](https://github.com/cogno-us/moltbot-safe) | Constrained execution beneath independent current authorization |
| [BitRep](https://github.com/cogno-us/bitrep) | Verify issuer signatures under explicit trust assumptions |
| [The Index](https://github.com/cogno-us/the-index) | A local blockchain reference for claims, evidence commitments and lifecycle history |
| [Portable Reasoning Protocol v1.0](https://github.com/cogno-us/portable-reasoning-protocol) | Portable instructions for evidence-bounded reasoning |
| [Research Intelligence Protocol v1.0](https://github.com/cogno-us/research-intelligence-protocol) | Disciplined discovery and cross-domain abstraction, kept separate |
| [Constitutional Governance for Institutions](https://github.com/cogno-us/constitutional-governance-for-institutions) | Alvorada: authority, challenge and correction for institutions |
