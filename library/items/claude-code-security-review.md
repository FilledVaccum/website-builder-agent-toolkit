---
name: claude-code-security-review (Anthropic)
url: https://github.com/anthropics/claude-code-security-review
local: -
summary: GitHub Action that uses Claude to review code changes for vulnerabilities. Closest repo found to the article's "Claude Security"; the plugin itself is unconfirmed.
type: [github-repo, plugin]
stage: [18-security, 16-vcs-ci]
task: [security-review]
content: [code]
content-format: []
agent: [claude-code, any-agent]
software: [github]
channel: []
cost: usage-based
license: mit
commercial-use: yes
requires: [api-key]
level: intermediate
source: official
maturity: active
verified: partial
stars: 6503
last_push: 2026-02-11
added: 2026-10-23
related: [claude-repos-playbook]
---

Stars and licence read from GitHub on 2026-10-23. Context and the author's opinion: [playbook/06](../../playbook/06-claude-repos-that-earn-their-place.md).
