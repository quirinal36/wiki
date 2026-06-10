---
title: Claw-Empire Hermes Control Surface Mapping
created: 2026-05-04
updated: 2026-05-04
type: query
tags: [ai-agents, workflow, control-plane, orchestration, claw-empire, hermes]
sources:
  - raw/notes/2026-05-04-claw-empire-hermes-control-surface-mapping-request.md
aliases:
  - Claw-Empire ↔ Hermes mapping
  - Hermes control surface mapping
---

# Claw-Empire Hermes Control Surface Mapping

## Purpose

This page defines how **Claw-Empire** should control **Hermes**.

The design goal is simple:
- **Claw-Empire** is the operator-facing control surface.
- **Hermes** is the execution/runtime layer.
- The web UI should make that separation explicit so the user does not have to think about two competing systems.

## Why Claw-Empire should be the control surface

Claw-Empire already provides an office-style orchestration model:
- CEO directive input
- project selection
- team leader meetings
- task routing
- report and log visibility
- local-first state management

That makes it a better fit for managing Hermes than a chat-only surface.

## Concept mapping

| Claw-Empire concept | Hermes concept | Notes |
|---|---|---|
| CEO directive | top-level task / goal | Entry point for work |
| Project | task container / workspace | Uses `project_id`, `project_path`, `project_context` |
| Team | agent group | Maps to an operational team with leader and members |
| Team leader | orchestrator agent | Responsible for coordination and handoff |
| Employee / agent | Hermes agent instance | May bind to a profile, model, and toolset |
| Meeting | planning / alignment step | Optional gating step before execution |
| Task | unit of work | Assigned to agent or team |
| Report | execution summary | Includes status, output, and follow-up |
| Log / history | session + run history | Used for traceability and replay |
| Stuck worker / active agent | running Hermes process | Should expose kill / retry / inspect actions |
| Worktree / isolated work area | Hermes workdir / session context | Keeps agent runs separated |

## Operational flow

### 1. Directive intake
1. User sends a CEO-style directive to Claw-Empire.
2. Claw-Empire resolves whether this is an existing project or a new project.
3. Claw-Empire records the mapping payload needed for Hermes execution.

### 2. Team routing
1. Claw-Empire decides whether a team leader meeting is needed.
2. If needed, the team leader aligns on scope and output format.
3. The directive is routed to the right Hermes agent or team.

### 3. Execution
1. Claw-Empire launches or resumes the relevant Hermes session.
2. Hermes performs tool use, code changes, web actions, or document work.
3. Hermes returns status, outputs, and artifacts.

### 4. Review and handoff
1. Claw-Empire records the result as a report or completed task.
2. If the work needs follow-up, Claw-Empire creates a new task or handoff.
3. The cycle repeats until the project is complete.

## Suggested data fields

The control surface should preserve these fields whenever possible:
- `project_id`
- `project_path`
- `project_context`
- `team_id`
- `team_name`
- `leader_agent_id`
- `agent_id`
- `agent_profile`
- `task_id`
- `run_id`
- `session_id`
- `status`
- `source_channel`
- `created_at`
- `updated_at`

## UI responsibilities

### Claw-Empire should own
- directive intake
- project selection / creation
- team composition
- meeting choice
- routing to agent or team
- run status display
- task and report history
- kill / retry / inspect actions

### Hermes should own
- actual tool execution
- session transcripts
- file operations
- model/provider selection
- memory / skills / cron execution
- low-level runtime health

## Adapter principle

Do not couple the UI directly to low-level Hermes internals.

Instead, build an adapter layer that translates:
- office concepts -> Hermes runtime actions
- project/team/task state -> Hermes session/run operations
- user-facing directives -> executable job payloads

This keeps the UI stable even if Hermes internals change.

## Relationship to existing docs

- [[instruction]] explains how to continue the work.
- [[hermes-agents-teams-web-ui-design]] explains the target control-plane shape.
- [[hermes-agent]] explains the runtime operator role.
- [[llm-wiki]] explains how to maintain the vault itself.

## Next step

Use this mapping as the reference for implementing API contracts, DB tables, and UI actions in the Claw-Empire-driven control plane.
