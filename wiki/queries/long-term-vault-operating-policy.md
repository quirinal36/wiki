---
title: Long-Term Vault Operating Policy
created: 2026-04-19
updated: 2026-04-19
type: query
tags: [workflow, research, memory, evaluation]
sources: []
aliases: [장기 운영 정책, vault 장기 운영 정책]
---

# Long-Term Vault Operating Policy

## User question
우리 Vault에 맞는 장기 운영 정책 문서

## Short answer
This document defines the long-term operating policy for the current Obsidian/LLM Wiki vault so that Hermes and related agents can work for a long time without the repository becoming chaotic.

## Policy goals
- Keep `raw/` immutable and trustworthy.
- Keep `wiki/` reusable, searchable, and cross-linked.
- Let multiple agents contribute without fragmenting structure.
- Make long-running work easier to resume across sessions.
- Prevent the vault from growing into a pile of duplicated notes.

## Policy 1. Separate raw sources from maintained knowledge
### Rule
- `raw/` is for original inputs only.
- `wiki/` is for interpreted, structured, reusable knowledge.
- Do not rewrite or overwrite source files in `raw/`.

### Why this matters
- Source integrity remains intact.
- Future re-interpretation is always possible.
- Errors in summaries do not corrupt original material.

### Practical application in this vault
- `raw/notes/`, `raw/articles/`, and `raw/papers/` are inboxes and archives of source material.
- All summaries, concepts, entities, comparisons, and queries belong in `wiki/`.
- If a source changes, store the updated version as a new raw file rather than silently replacing earlier evidence.

## Policy 2. Every meaningful page must be discoverable
### Rule
- Every new wiki page must have YAML frontmatter.
- Every new wiki page must be added to `index.md`.
- Every meaningful operation must be appended to `log.md`.

### Why this matters
- A page that cannot be rediscovered is operationally close to lost.
- `index.md` is the map; `log.md` is the memory of change.
- Frontmatter allows structured maintenance, search, and automation.

### Minimum frontmatter standard
- `title`
- `created`
- `updated`
- `type`
- `tags`
- `sources`

### Practical application in this vault
- `index.md` should remain the first navigation layer for humans and agents.
- `log.md` should capture creation, ingest, query, scan, and lint activity.
- If a page exists but is not indexed, it is considered incomplete.

## Policy 3. Prefer updating existing pages over creating duplicates
### Rule
- Search before creating.
- If a concept already exists, update it unless the new material clearly deserves a separate page.
- Create new pages only when they add durable retrieval value.

### Why this matters
- Duplicate pages are one of the fastest ways to degrade a long-lived vault.
- Fewer, denser, better-linked pages are more useful than many thin pages.
- Repeatedly updating strong pages compounds knowledge instead of scattering it.

### Practical application in this vault
- Before creating new concepts or entities, search `wiki/` and inspect `index.md`.
- New pages are justified when:
  - the idea is central to a source,
  - it will likely be reused,
  - or folding it into an existing page would make that page blurry or oversized.

## Policy 4. Multi-agent work must follow one shared structure
### Rule
- Multiple agents may contribute, but they must all obey the same storage conventions.
- Naming, frontmatter, tags, indexing, and logging rules must remain shared.

### Why this matters
- Multi-agent productivity is only valuable if the resulting repository still feels coherent.
- Without shared rules, one vault quickly turns into many incompatible mini-systems.

### Shared structure for this vault
- Use the existing folder layout:
  - `raw/`
  - `wiki/summaries/`
  - `wiki/entities/`
  - `wiki/concepts/`
  - `wiki/comparisons/`
  - `wiki/queries/`
- Use tags from `schema/tag-taxonomy.md`.
- Use stable lowercase hyphenated filenames when possible.
- Preserve the same summary/entity/concept/query writing style used by current pages such as [[ai-era-survival-strategy]], [[learner-agency]], and [[parent-notice-ai-use-guide]].

## Policy 5. Use automation mainly for reconciliation and hygiene
### Rule
- Automate discovery, reconciliation, indexing, and validation before automating aggressive page generation.
- Human or high-level review should still shape large structural decisions.

### Why this matters
- Automation is strongest at catching drift and handling repetition.
- Poorly constrained automation can flood a vault with low-value pages.
- Long-term quality depends more on disciplined cleanup than on raw creation speed.

### Practical application in this vault
- Daily scheduled maintenance should:
  - scan `raw/` inboxes,
  - detect unreferenced raw files,
  - skip empty placeholders,
  - generate justified summary/concept/entity pages,
  - update `index.md` and `log.md`,
  - verify broken links.
- Large structural refactors should remain explicit rather than automatic.

## Operating checklist
- Is the source stored in `raw/` and left unchanged?
- Did the new or updated page include full frontmatter?
- Was an existing page checked before creating a new one?
- Was the new page added to `index.md`?
- Was the operation recorded in `log.md`?
- Are there at least 2 outbound wikilinks where practical?
- Are all tags inside `schema/tag-taxonomy.md`?

## Interpretation for long-term use
This vault should behave less like a pile of notes and more like a maintained operating knowledge base. The objective is not maximum page count. The objective is durable clarity: trusted raw evidence, reusable synthesized pages, strong navigation, and consistent upkeep across time and agents.

## Supporting wiki pages
- [[llm-wiki]]
- [[obsidian-workflow]]
- [[critical-ai-literacy]]
- [[learner-agency]]
- [[ai-era-survival-strategy]]
- [[ai-era-learning-survival-secret]]
