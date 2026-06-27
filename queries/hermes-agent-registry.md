---
title: Hermes Agent Registry
created: 2026-04-23
updated: 2026-04-23
type: query
tags: [ai-agents, inventory, workflow, ops]
sources: []
aliases: [agent registry, Hermes profile registry, agent list, 현재 agent 목록]
status: active
---

> Living note: this registry reflects the current Hermes snapshot and should be updated whenever profiles, aliases, or gateway states change.

# Hermes Agent Registry

## Purpose
This page keeps a concise, durable overview of the currently created Hermes agents/profiles.
Because the list may change over time, treat this as a living registry rather than a fixed inventory.

## Registry

| Profile      | Alias        | Gateway | One-line purpose                                                                           |
| ------------ | ------------ | ------- | ------------------------------------------------------------------------------------------ |
| default      | -            | running | Main general-purpose Hermes profile for everyday tasks and fallback work.                  |
| aggressive   | -            | stopped | High-assertiveness market-analysis variant for faster, more decisive outputs.              |
| bear         | -            | stopped | Downside-leaning market analysis profile for risk-off and bearish scenarios.               |
| bull         | -            | stopped | Upside-leaning market analysis profile for optimistic and growth scenarios.                |
| collector    | collector    | stopped | Feed and inbox collection helper that gathers external data for later processing.          |
| conservative | -            | stopped | Cautious market-analysis variant that prefers safer, lower-risk conclusions.               |
| facilitator  | -            | stopped | Coordination profile for organizing multi-step work and keeping people/agents aligned.     |
| fundamental  | -            | stopped | Fundamentals-focused analysis profile for business, value, and long-horizon reasoning.     |
| gaia         | gaia         | running | Slack-only operations profile used for chat-based coordination and assistant work.         |
| lets_manager | lets_manager | stopped | Academy operations manager profile for student, class, and daily school workflows.         |
| neutral      | -            | stopped | Balanced baseline analysis profile used when no strong market tilt is needed.              |
| news         | -            | stopped | News monitoring and summarization profile for current-events scanning.                     |
| sector       | -            | stopped | Sector-level market analysis profile for industry grouping and rotation views.             |
| sentiment    | -            | stopped | Sentiment-analysis profile for tone, crowd mood, and market sentiment reading.             |
| technical    | -            | stopped | Technical-analysis profile for charts, patterns, indicators, and price structure.          |
| trader       | trader       | running | Primary trading analysis profile for active market workflows and trade-oriented decisions. |

## Operational notes
- Current running profiles are `default`, `gaia`, and `trader`.
- The registry should be revised whenever a profile is added, removed, renamed, repurposed, or restarted.
- If gateway/service behavior changes, update this page alongside the relevant runtime notes.

## Related pages
- [[hermes-agent]]
- [[trader-agent]]
- [[new-agent-creation-manual]]
- [[long-term-vault-operating-policy]]
