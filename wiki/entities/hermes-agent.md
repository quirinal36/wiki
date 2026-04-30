---
title: Hermes Agent
created: 2026-04-19
updated: 2026-04-19
type: entity
tags: [ai-agents, llm, tooling, workflow]
sources: []
---

# Hermes Agent

## Overview
Hermes Agent is the primary AI operator that manages this vault, performs tool-using workflows, and maintains persistent context across sessions.

## Why it matters
- It can ingest sources, write notes, update indexes, and maintain logs.
- It provides a repeatable operating interface across terminal, gateway, and profile-based workflows.
- It is the execution layer that connects the wiki process to day-to-day work.

## Key responsibilities in this vault
- Maintain wiki discipline described in [[llm-wiki]].
- Work smoothly with the note structure described in [[obsidian-workflow]].
- Support domain-specific workflows such as [[trader-agent]].

## Relationships
- [[llm-wiki]] defines the knowledge-base pattern Hermes maintains.
- [[obsidian-workflow]] defines how humans browse and extend the same vault.
- [[trader-agent]] is one example of a focused operating profile inside the broader Hermes setup.

## Notes
Hermes should prefer updating existing linked pages instead of scattering similar information across duplicates.
