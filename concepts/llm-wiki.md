---
title: LLM Wiki
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [llm, research, workflow, memory]
sources: []
---

# LLM Wiki

## Definition
LLM Wiki is a persistent markdown knowledge-base pattern where sources are stored once, synthesized into reusable notes, and continuously refined over time.

## Why it matters
- It compounds knowledge instead of redoing the same analysis.
- It makes cross-links and contradictions visible.
- It turns ad hoc conversations into reusable documentation.

## Core structure
- `raw/` stores immutable source material.
- `wiki/` stores maintained knowledge pages.
- `index.md` provides navigation.
- `log.md` records meaningful changes.

## Related pages
- [[hermes-agent]] is the operator that maintains this pattern.
- [[obsidian-workflow]] describes how the vault is used day to day.
- [[trader-agent]] is a domain-specific workflow that can be documented inside the same system.

## Practical rule
A good LLM Wiki grows through consistent updates, strong linking, and disciplined indexing rather than page count alone.
