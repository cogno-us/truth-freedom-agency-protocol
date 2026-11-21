<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / /\__ \
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

**Status:** optional reasoning protocol (side group of the [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md)). Label: merged. In the hub lock as `tfa` with `optional: true`; the lock records no interface for it, and it is not selected for enforcement. A behavioral protocol, not an authority system. <!-- pin-round: lock revision statements in this file are refreshed with the hub lock -->

Identity, revision 2: **Say what is true, and how you know. Ask for nothing. Protect the next move of everyone affected.** Revision 1 read: Say what is true. Ask for nothing. Protect their next move. See [Protocol text and revisions](#protocol-text-and-revisions).

## What it is, who it is for, what it does not do

**What it is.** A lightweight optional behavioral protocol for AI interaction. Its identity remains three rules, which in revision 2 read: Say what is true, and how you know. Ask for nothing. Protect the next move of everyone affected. Implementation and evaluation guidance explain those rules without making them an authority system.

**Who it is for.** Reviewers and builders who want a small vocabulary for interaction failures. An assistant can burden or influence a user through unsupported certainty, unnecessary questioning, validation pressure or premature closure of alternatives; TFA names those failures while allowing questions that are materially necessary. Engineers can inspect the evaluation cases and validator; architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

**What it does not do.** TFA does not authenticate identities, issue or revoke grants, enforce tool permissions or prove an external effect. It does not enforce authorization or substitute for human oversight. See [Limits](#limitations-and-deployment-decisions).

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Protocol text and revisions

**Revision 2 (2026-11-21).** The protocol has three rules.

1. Say what is true, and how you know.
2. Ask for nothing.
3. Protect the next move of everyone affected.

Two rules sit beside the three. They are not part of the three-rule identity.

- **Correction rule.** If what you said proves false, withdraw it as visibly as you said it.
- **Companion rule for action.** Act only within what you were granted.

**The test.** Three questions a reviewer can put to any response:

- Is it true, and can you show the source?
- Does it demand anything?
- Is everyone affected at least as free as before?

**Scope of rule 3.** "Everyone affected" means the recipient and anyone the response is about or acts upon. A person who is not party to an exchange can still be affected by it.

**What changed from revision 1.**

| Rule | Revision 1 | Revision 2 | Reason |
| --- | --- | --- | --- |
| 1 | Say what is true. | Say what is true, and how you know. | A claim with no stated basis cannot be checked. The addition asks for the source of a claim and the confidence it deserves. |
| 2 | Ask for nothing. | Ask for nothing. | Unchanged. |
| 3 | Protect their next move. | Protect the next move of everyone affected. | Revision 1 addressed the other party to the exchange. An exchange can also narrow the options of someone it is about who is not present. |

**What did not change.** The protocol still has three rules, and rule 2 is untouched. "Ask for nothing" still allows materially necessary clarification and authorization checks. The companion rule restates the limit already given under Agency in [Key features](#key-features). It grants no permission and does not make TFA an authority system.

**Evidence for revision 2.** **known limit** The 19 committed evaluation cases were written against revision 1. None targets the revision 2 additions: the basis of a claim, people outside the exchange, or correction. **known limit** No case has been executed under either revision. The historical PDFs state revision 1 and are retained as written. [EVALUATION.md](EVALUATION.md) freezes a separate condition text for each revision; results under different revisions are not to be pooled.

## Where it fits

TFA sits in the "Optional reasoning protocols" side group, beside [Portable Reasoning Protocol (PRP)](https://github.com/cogno-us/portable-reasoning-protocol) and [Research Intelligence Protocol](https://github.com/cogno-us/research-intelligence-protocol). It can be used independently; adopting the wider stack is optional. See [Relationship to PRP and institutional governance](#relationship-to-prp-and-institutional-governance). The [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md) is the canonical map; the table below is a copy of it.

<!-- stack-map-block:start -->
### Cognous stack components

The Open Control Stack keeps five responsibility groups and two side groups. The groups organize responsibilities. They are not an execution sequence or a requirement to install every component. The canonical map, with one row per repository, is the hub [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md); names are defined in [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) and commands and profiles per repository are in [profiles and tools](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/profiles-and-tools.md). The map uses four labels: merged, selected, known limit and proposed. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 Knowledge & Provenance** | [Evidence Registry (The Index)](https://github.com/cogno-us/cognous-evidence-registry) · [Evidence Attestation (BitRep)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 Institutional Governance** | [Institutional Governance (Alvorada)](https://github.com/cogno-us/cognous-institutional-governance) |
| **03 Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 Constrained Execution** | [Execution Runtime](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **Cross-cutting exchange** | [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) |
| **Optional reasoning protocols** (side group) | [Portable Reasoning Protocol (PRP)](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence Protocol](https://github.com/cogno-us/research-intelligence-protocol) · [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol) |
| **Tooling and qualification** (side group) | [Ergonomics (`cognous-ocs`)](https://github.com/cogno-us/cognous-open-control-stack-ergonomics) · [Verifier](https://github.com/cogno-us/cognous-open-control-stack-verifier) · [Orchestrator](https://github.com/cogno-us/cognous-stack-orchestrator) · [Qualification](https://github.com/cogno-us/cognous-stack-qualification) |

The hub, [cognous-open-control-stack](https://github.com/cogno-us/cognous-open-control-stack), holds the component lock and the canonical documentation. Execution Runtime is the repository formerly named Moltbot Safe; see [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md). PRP, Research Intelligence Protocol and TFA Protocol are optional behavioral instructions; they do not enforce authorization or substitute for human oversight. A signature, registry entry, message receipt or evidence summary does not grant execution authority.

Last checked against `component-lock.json` at hub commit `dcc9bd7533ef`. <!-- pin-round: refresh this commit with the hub stack map -->
<!-- stack-map-block:end -->

## Quick start

Prerequisites: Python 3 and a clone of this repository (the validator uses only the standard library; verified with Python 3.13). No model, network or account is needed.

```bash
git clone https://github.com/cogno-us/truth-freedom-agency-protocol
cd truth-freedom-agency-protocol
python scripts/validate_evaluation.py
```

Run it from the repository root: with no argument the validator reads `evaluation/cases.json` relative to the current directory, and it accepts another path as its one argument (CI passes `evaluation/cases.json`). Expected: exit code 0 and the single line

```text
OK: 19 cases validated; all statuses are explicit.
```

It finishes in well under a second. A missing or malformed file prints an `ERROR:` line and exits 1. <!-- pin-round: the case count reflects the repository head at the time of writing -->

**What this does not prove.** The validator checks case structure, required category coverage, unique IDs and allowed status labels. It does not call a model, validate run metadata or raw outputs, or establish that any model follows TFA. All 19 cases are `unexecuted`.

To use the protocol, apply the three rules as prompt guidance or a review rubric. "Ask for nothing" does not prohibit necessary clarification or permission checks. Read [the evaluation protocol](EVALUATION.md) before reporting results.

## What ships

| Item | Kind | Purpose | Status label |
|---|---|---|---|
| [EVALUATION.md](EVALUATION.md) | evaluation protocol | Scoring dimensions (Truth, Freedom, Agency; 0 to 2 each), failure conditions, run controls, required run metadata, ablation design, minimal comparison procedure with condition texts for revisions 1 and 2, and status values. | merged |
| [evaluation/cases.json](evaluation/cases.json) | evaluation cases (19) | Seven required behavioral categories with one case each, plus the 12 original public scenarios kept as `legacy_ablation`. All `unexecuted`. | merged |
| [`scripts/validate_evaluation.py`](scripts/validate_evaluation.py) | command (standard library) | Structural validation of a case file; optional path argument. Verified above. | merged |
| [.github/workflows/validate-evaluation.yml](.github/workflows/validate-evaluation.yml) | CI | Runs the validator on pull requests that change the README, protocol, cases or validator. | merged |
| [TFA_Whitepaper.pdf](TFA_Whitepaper.pdf) | historical source (PDF, 4 pages) | The TFA Protocol (S43) paper, dated 2026-03-06. It reports an ablation battery of its own; this repository does not re-run or reproduce it. | merged |
| [S43_Cryptographic_Protocol.pdf](S43_Cryptographic_Protocol.pdf) | historical source (PDF, 9 pages) | A cryptographic interpretation of S43, dated 2026-03-06. It is a paper, not an implementation in this repository. | merged |
| [docs/security-cloud-remediation-20261016.md](docs/security-cloud-remediation-20261016.md) | historical note | Record of the 2026-10-16 workflow pin change, retained as written. | merged |
| [Business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md) | collateral | Nontechnical introduction to this component's role and evidence limits. | merged |

TFA ships no installable package, no commands other than the validator, no profile and no contract draft. The two PDFs have no text version in this repository; the table above describes them only at the level their title pages support.

## Documentation index

Every page in this repository is linked below.

| Page | Read it for |
|---|---|
| [EVALUATION.md](EVALUATION.md) | How to evaluate TFA reproducibly, and what a validated case file does not establish. |
| [evaluation/cases.json](evaluation/cases.json) | The machine-readable cases. |
| [TFA_Whitepaper.pdf](TFA_Whitepaper.pdf), [S43_Cryptographic_Protocol.pdf](S43_Cryptographic_Protocol.pdf) | Historical sources. |
| [docs/security-cloud-remediation-20261016.md](docs/security-cloud-remediation-20261016.md) | Historical note on a workflow pin change. |
| [Business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md) | Nontechnical introduction, not additional runtime features. |

Reading paths: **adopter** this README, then EVALUATION.md. **Reviewer** EVALUATION.md "Interpretation boundaries", then this README's limits. Shared names and labels are in the hub [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) page.

## How it works and design notes

### How it works

A reviewer evaluates an assistant response for factual calibration, unnecessary extraction and preservation of user choice. A clarification is appropriate when it resolves decision-critical uncertainty or an authorization boundary. Once sufficient permission and evidence exist, the assistant can proceed without repeatedly seeking reassurance. This behavior does not override institutional or runtime controls.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

### Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Truth** | Calibrate claims to evidence, state the basis for material claims, and avoid invented facts, sources, capabilities or authority. |
| **Freedom** | Avoid extracting unnecessary information, reassurance, labor or commitment as the price of help. |
| **Agency** | Keep meaningful alternatives open for the recipient and for anyone the response is about or acts upon, and act only within permission already granted. |
| **Correction** | Withdraw a statement that proves false as visibly as it was made. |
| **Proportionate questions** | Ask the minimum needed when accuracy, safety or authorization depends on missing information. |
| **Evaluation guidance** | Use explicit cases and review criteria rather than treating the three rules as a behavioral guarantee. |

## Relationship to PRP and institutional governance

TFA can be used independently. Its three rules remain the interaction-level target; adopting the wider stack is optional.

| Component | Role | Boundary |
| --- | --- | --- |
| TFA | Review truthfulness, unnecessary extraction, and preservation of meaningful choice in an interaction. | Behavioral guidance does not guarantee model behavior or grant permission. |
| [Portable Reasoning Protocol](https://github.com/cogno-us/portable-reasoning-protocol) | Add reasoning discipline, evidence distinctions, and proportionate scrutiny. | More reasoning or confidence does not establish authority. |
| [Cognous Institutional Governance (Alvorada)](https://github.com/cogno-us/cognous-institutional-governance) | Describe institutional decision rights, challenge, and correction. | A published framework is not institutional adoption; operative authority must be independently established. |

Necessary requests for authorization, decision-critical evidence, or safety-relevant facts are compatible with “Ask for nothing.” Ask only what materially affects the decision, explain why when useful, and proceed when sufficient evidence and permission already exist. The rule rejects manipulation and unnecessary burden; it does not waive an actual approval requirement.

When evaluating TFA alongside PRP or other instructions, record their exact text and revisions. Overlapping truthfulness or agency instructions can remain active in an ablation, so removing a TFA sentence does not remove the underlying capability or obligation. See the [comparison procedure](EVALUATION.md#minimal-comparison-procedure).

## Compatibility and selection

TFA is optional behavioral guidance; static artifact validity does not establish behavioral efficacy. [EVALUATION.md](EVALUATION.md) and the case validator distinguish proposed evaluations from executed observations. Do not infer effectiveness or cryptographic assurance from the protocol name, historical PDFs or a successfully parsed case file.

The protocol keeps three rules. Revision 2 reads: **Say what is true, and how you know. Ask for nothing. Protect the next move of everyone affected.** Revision 1 read: Say what is true. Ask for nothing. Protect their next move. The historical [TFA Whitepaper](TFA_Whitepaper.pdf) and [S43 Cryptographic Protocol](S43_Cryptographic_Protocol.pdf) state revision 1. They remain sources, not evidence of new implementation or execution.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

## Limitations and deployment decisions

TFA does not authenticate identities, issue or revoke grants, enforce tool permissions or prove an external effect. Truthfulness, non-coercion and agency preservation require evidence from actual behavior. The hub has not executed model-behavior qualification. Historical PDFs retain their original provenance and are not new cryptographic guarantees.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

Known limits, as labelled facts: **known limit** All 19 evaluation cases are `unexecuted`; behavioral efficacy is not established here. **known limit** No committed case targets the revision 2 additions (the basis of a claim, people outside the exchange, correction). **known limit** The hub has not executed model-behavior qualification. **known limit** The two PDFs are historical sources and are not new cryptographic guarantees. Shared stack-level limits are stated in the hub [guarantees and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/guarantees-and-limits.md).

## Contributing, licence, attribution and security

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation. Run the validator from the quick start before opening a pull request; CI runs it when the README, protocol, cases or validator change.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update. For reporting a concern, see the hub [security reporting and triage](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/security-reporting-and-triage.md) page; the historical [workflow note](docs/security-cloud-remediation-20261016.md) is retained as written.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.
- [OECD. *Agentic AI in organisations: Early insights from practitioner interviews*. OECD Artificial Intelligence Papers, No. 65 (2026)](https://doi.org/10.1787/1257a26f-en). Qualitative practitioner research on bounded autonomy, oversight and organizational deployment.
- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
