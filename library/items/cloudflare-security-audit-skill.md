---
name: Cloudflare security-audit-skill
url: https://github.com/cloudflare/security-audit-skill
local: -
summary: Official Cloudflare skill that makes a coding agent run a six-phase security audit (recon, coverage-led hunting, validation, structured findings, independent verification, report) with schema-validated, machine-readable results.
type: [skill, github-repo]
stage: [18-security, 19-maintenance]
task: [security-review, automation]
content: [code]
content-format: [report]
agent: [claude-code, cursor, codex, any-agent]
software: [nodejs]
channel: []
cost: free
license: mit
commercial-use: yes
requires: [node, local-install]
level: advanced
source: official
maturity: established
verified: yes
stars: 40380
last_push: 2026-09-14
added: 2026-10-23
related: [claude-code-security-review]
---

## What it is

Seeded Cloudflare's internal vulnerability-discovery harness (see their blog post "Build your own vulnerability harness"). It orchestrates isolated sub-agents through six phases and keeps work in `coverage-ledger.json` and `findings.json`, checked by zero-dependency Node validators (`validate-findings.cjs`, `validate-coverage-ledger.cjs`) against `report-schema.json`.

1. **Reconnaissance** - architecture, trust boundaries, input surfaces, coverage ledger.
2. **Coverage-led hunting** - isolated hunters per ledger unit; critics find gaps.
3. **Candidate validation** - a fresh verifier tries to *disprove* each candidate.
4. **Structured output** - `confirmed`, `needs_validation`, `rejected` records.
5. **Independent verification** - fresh agents re-check final source claims.
6. **Reporting** - `REPORT.md`, `FINDINGS-DETAIL.md`, `NEEDS-VALIDATION.md`.

Hunting playbooks cover core attack classes plus memory safety, AI/LLM, web protocol and auth, client-side, supply chain, cloud and deployment, RPC/messaging, resource exhaustion, data isolation and desktop/mobile targets.

## Install and use

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit   # add --global for user-level
```

Then ask the agent: `security audit this codebase`, `find security vulnerabilities in ./src`, or `do a security review, output to ~/audits/my-project`. A direct audit request runs full audit mode; focused security questions use lighter guidance mode. Default output: `~/security-audit-skill/<repo>/run-<N>` (it writes inside the repo only if you pick a version-control-ignored directory). Repeat runs are additive.

## Requirements and cautions

- Agent with tool use and **parallel sub-agents**, plus Node.js for the validators.
- **Sandbox:** target-controlled builds, tests, fuzzers or browsers must run in an OS-enforced sandbox (no external network, sanitized environment, resource limits, writes only to scratch paths). Without one, the skill leaves the lead as `needs_validation` instead of executing target code.
- A full audit uses many sub-agents, so expect substantial model usage.
- Created 2026-06-18; MIT. It reduces, not replaces, a human or professional review before launch.

Fits website projects at the pre-launch review step in [catalog stage 18](../../catalog/stages/18-security.md), alongside Gitleaks and Semgrep.
