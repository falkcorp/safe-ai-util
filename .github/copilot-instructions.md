<!-- file: .github/copilot-instructions.md -->
<!-- version: 2.4.0 -->
<!-- guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a -->
<!-- last-edited: 2026-06-13 -->

# safe-ai-util — Additional Context

Org-wide coding standards (file headers, language rules, commit format) are at
**https://github.com/falkcorp/.github** and apply automatically to this repo.

For full project context: **CLAUDE.md** at the repo root.

## Project overview

Safe centralized utility for AI agent command execution with comprehensive logging. Language: Rust/Python.

## Key directories

| Directory | Purpose |
|-----------|---------|
| `src/` | Rust source code |
| `scripts/` | Python automation scripts |
| `tests/` | Integration tests |
| `docs/` | Documentation |

## Critical constraints

- Use `copilot-agent-util` (this binary) for git operations in agent workflows — not raw git
- All commits MUST use conventional commit format: `type(scope): description`
- Logs are written to `logs/` after running VS Code tasks
