---
title: Hermes Agents/Teams Web UI Instruction
created: 2026-05-04
updated: 2026-05-04
type: query
tags: [ai-agents, workflow, product, automation, documentation]
sources:
  - raw/notes/2026-05-04-hermes-agents-teams-web-ui-instruction-request.md
aliases:
  - instruction.md
  - Hermes control plane instruction
---

# Hermes Agents/Teams Web UI Instruction

## Purpose

Use this page as the working instruction for the Hermes agents/teams web UI effort. The goal is to build a control plane, not a chat wrapper.

This project now treats **Claw-Empire** as the main control surface for Hermes orchestration. In other words:
- **Claw-Empire** handles CEO/directive input, office-style task routing, and team/agent operations.
- **Hermes** remains the execution/runtime layer behind those operations.
- The UI should expose Hermes agents, teams, tasks, runs, and handoffs through Claw-Empire's workflow model rather than inventing a second competing operator UI.

## What to do first

1. Read the existing Hermes operating docs.
2. Keep Open WebUI separate from the control plane.
3. Treat agents, teams, tasks, runs, and handoffs as first-class objects.
4. Update the wiki as the design evolves.

## Existing documents already in place

### 1. [[hermes-agent]]
The core operator page. It explains Hermes as the agent that maintains this vault, runs workflows, and connects the wiki process to day-to-day work.

### 2. [[llm-wiki]]
The knowledge-base pattern page. It explains the raw/wiki/index/log structure and the discipline used to keep the vault reusable.

### 3. [[obsidian-workflow]]
The vault navigation page. It explains how the same vault is used in Windows Obsidian and WSL tooling.

### 4. [[agents/index]]
The agents operations index. It is the current home for Hermes-based letsTrade orchestration notes, skills, and operating records.

### 5. [[hermes-agents-teams-web-ui-design]]
The control-plane design page. It describes the architecture, data model, and UI sections for the agents/teams dashboard.

### 6. [[claw-empire-hermes-control-surface-mapping]]
The integration map between Claw-Empire and Hermes. It defines which office-style concepts belong to the control surface and which runtime actions belong to Hermes.

## Working instruction

When continuing this project:
- Prefer a separate control plane over embedding management features into Open WebUI.
- Make agent and team definitions explicit and editable.
- Track tasks and runs separately.
- Preserve session history and handoffs.
- Connect the UI to Hermes runtime features through an adapter layer.

## Recommended order of implementation

1. DB schema
2. API contract
3. Agent CRUD
4. Team CRUD
5. Task board
6. Run history
7. Hermes connection status
8. Basic auth

## Relationship to the rest of the vault

This page is an instruction layer that sits above the design page.
- [[hermes-agents-teams-web-ui-design]] explains what to build.
- This page explains how to proceed.
- [[hermes-agent]] and [[llm-wiki]] provide the maintenance rules.

## Notes

Keep this page short and operational. If the design changes materially, update this instruction page so it remains the stable entry point for the work.
