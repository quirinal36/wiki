---
title: Hermes Agents/Teams Web UI Design
created: 2026-05-04
updated: 2026-05-04
type: query
tags: [ai-agents, workflow, product, automation]
sources:
  - raw/notes/2026-05-04-hermes-agents-teams-web-ui-design-request.md
aliases:
  - Hermes용 agents/teams 웹 UI 설계안
  - Hermes Control Plane
---

# Hermes Agents/Teams Web UI Design

## Short answer

Open WebUI is not enough for this use case. The right design is a separate **control plane** for managing agents, teams, tasks, runs, and handoffs, while Open WebUI remains the chat surface and Hermes Gateway remains the messaging integration layer.

## Why this matters

The user needs:
- agent creation and editing
- team composition and role assignment
- task routing and status tracking
- run/session history
- handoff tracking
- cron and skills integration

That requires an **operations UI**, not just a chat UI.

## Recommended architecture

### Layer 1: Chat surface
- Open WebUI for direct human chat
- Used for prompt testing and ad-hoc conversations
- Not responsible for organizing agents or teams

### Layer 2: Control plane
- A dedicated Hermes dashboard
- Manages agents, teams, tasks, runs, profiles, skills, and cron jobs
- Shows operational state and allows orchestration actions

### Layer 3: Hermes runtime
- Hermes API server
- Hermes Gateway
- Hermes Cron
- Hermes sessions/profiles
- Actual tool use and model execution

## Core data model

### Agent
A reusable execution unit with:
- name
- role
- model/provider
- toolsets
- profile binding
- default prompt
- enabled state

### Team
A group of agents with:
- leader
- members
- workflow
- default routing rules

### Task
A work item with:
- title
- description
- assigned agent or team
- status
- priority
- source channel
- output

### Run
A concrete execution trace with:
- task link
- session link
- logs
- tool calls
- status
- timestamps

### Session
Hermes conversation or job history with:
- source
- profile
- model
- transcript reference

## UI pages

### 1. Dashboard
- active agents
- active teams
- running tasks
- failed runs
- recent handoffs

### 2. Agents
- list / filter / search
- create / edit / clone / disable
- detail tabs for model, tools, profile, runs, skills

### 3. Teams
- create / edit team
- add or remove members
- select leader
- view workflow and handoffs

### 4. Tasks
- inbox and kanban view
- assign to agent or team
- change priority
- rerun / cancel / review

### 5. Runs / Sessions
- execution history
- logs
- tool calls
- replay and debug

### 6. Cron
- scheduled jobs
- next run time
- recent results
- failures

### 7. Skills
- browse skills
- attach skills to agents
- inspect skill docs

### 8. Settings
- Hermes API endpoint
- gateway connection state
- auth and permissions
- Slack / Telegram / Discord links

## Recommended stack

- **Frontend:** Next.js, React, TypeScript, Tailwind, shadcn/ui
- **Backend:** Next.js API routes or FastAPI
- **DB:** Postgres / Supabase
- **Realtime:** SSE or WebSocket
- **Runtime integration:** Hermes CLI / API server / gateway adapter

## MVP scope

Build first:
1. Agent CRUD
2. Team CRUD
3. Task board
4. Run history
5. Hermes connection status
6. Basic auth

Defer for later:
- advanced workflow editor
- complex permissions UI
- full realtime collaboration
- simulation / replay tooling

## Related pages

- [[hermes-agent]]
- [[llm-wiki]]
- [[obsidian-workflow]]
- [[agents/index]]

## Next step

Turn this into a concrete implementation plan:
1. DB schema
2. page-by-page wireframe
3. API contract
4. MVP task breakdown
