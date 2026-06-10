# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-16] maintenance | Daily Vault Maintenance
- Scanned raw/ folder and found unprocessed notes.
- Detected and ignored empty file: `raw/notes/무제.base`.
- Ingested and summarized: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`.
- Files created:
  - `wiki/summaries/chatgpt-3.5-years-later.md`
- Updated `index.md` with the new summary.
- Verified wikilinks and source frontmatter entries.

## [2026-05-17] maintenance | Vault Scan
- Scanned raw/ folders; all files are already processed or referenced.
- Detected and skipped empty/unactionable file: `raw/notes/무제.base`.

## [2026-05-18] maintenance | Vault Daily Batch
- Processed 12 raw files from raw/notes/.
- Created 6 summary pages and 1 concept page ([[vibe-coding]]).
- Oriented on SCHEMA and index before creation.
- Linked new pages across entities and concepts.

## [2026-05-20] maintenance | Daily Vault Maintenance Batch
- Created summary: wiki/summaries/ai-winning-thought-process.md
- Created summary: wiki/summaries/ai-era-brain-science-survival.md
- Created summary: wiki/summaries/learner-agency-logic.md
- Created summary: wiki/summaries/why-teach-coding.md
- Created summary: wiki/summaries/coding-academy-shift.md
- Created summary: wiki/summaries/excel-vs-ai-automation.md
- Created summary: wiki/summaries/cs-major-rethink.md

## [2026-05-22] maintenance | Vault Scan
- Scanned `raw/notes`, `raw/articles`, and `raw/papers`.
- All 13 files in `raw/notes` are already referenced in wiki source frontmatter.
- `raw/articles` and `raw/papers` are empty.
- Detected non-empty placeholder: `raw/notes/무제.base` (contains Dataview table stub).
- No new actionable content found.

## [2026-05-23] maintenance | Processing New Raw Note
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created summary: [[summaries/chatgpt-anniversary-edu-shift|summaries/chatgpt-anniversary-edu-shift.md]]
- Created concept: [[concepts/vibe-coding-education|concepts/vibe-coding-education.md]]
- Updated `index.md` with new pages.
- Verified no broken links.

## [2026-05-24] maintenance | Vault Daily Batch
- Routine scan of `raw/` folders completed.
- Verified 11 raw notes against existing wiki pages; all are already processed and linked in frontmatter.
- Detected placeholder `raw/notes/무제.base` (contains Dataview stub), skipping as non-actionable.
- Infrastructure check: `index.md`, `SCHEMA.md`, and `log.md` are consistent.

## [2026-05-25] ingest | Strategy for Winning in the AI Era: Linchpins and Tribes
- Source: `raw/notes/ai 를 이기는 생각방법.md`
- Created: [[ai-strategy-linchpin-tribe]], [[seth-godin]], [[art-as-work-strategy]]
- Detected placeholder `raw/notes/무제.base` as stub, ignoring.

## [2026-05-26] update | Daily maintenance
- Ingested: raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md
- Created: summaries/post-chatgpt-education-paradigm.md
- Created: concepts/vibe-coding.md

## [2026-05-27] maintenance | Batch Process Daily
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created summary: [[summaries/ai-education-paradigm-shift]]
- Created concept: [[concepts/vibe-coding]]
- Updated `index.md` and page counts.
- Verified wikilinks and source frontmatter.

## [2026-05-29] maintenance | Batch Process Daily
- Ingested: raw/notes/ai 를 이기는 생각방법.md -> [[wiki/summaries/ai-시대-린치핀과-부족의-전략.md]]


## [2026-05-29] maintenance | Automated Batch Ingest
- Skipped empty file: raw/notes/ai 시대 생존 전략.md
- Skipped empty file: raw/notes/AI 시대에 살아남는 학습자의 비밀.md
- Skipped empty file: raw/notes/컴퓨터활용능력 자격증 앞으로도 필요할까.md


## [2026-05-30] maintenance | Vault Clean
- Scanned `raw/` directories: `raw/notes`, `raw/articles`, `raw/papers`.
- No unreferenced/non-empty files found. Everything up to date.

## [2026-05-31] maintenance | Ingested Educations Paradigm Note
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created: `summaries/chatgpt-impact-on-education.md`
- Created/Updated: `concepts/vibecoding.md`
- Created/Updated: `entities/lets-coding-play.md`
- Updated: `index.md`

## [2026-06-02] ingest | Batch maintenance run
- Ingested: `raw/notes/2026-04-23-agent-creation-manual-request.md`
  - Created: `queries/2026-04-23-agent-creation-manual-request-summary.md`
- Ingested: `raw/notes/2026-04-27-letstrade-user-ticker-pipeline-runbook-request.md`
  - Created: `queries/2026-04-27-letstrade-user-ticker-pipeline-runbook-request-summary.md`
- Ingested: `raw/notes/2026-05-04-claw-empire-hermes-control-surface-mapping-request.md`
  - Created: `queries/2026-05-04-claw-empire-hermes-control-surface-mapping-request-summary.md`
- Ingested: `raw/notes/2026-05-04-hermes-agents-teams-web-ui-design-request.md`
  - Created: `queries/2026-05-04-hermes-agents-teams-web-ui-design-request-summary.md`
- Ingested: `raw/notes/2026-05-04-hermes-agents-teams-web-ui-instruction-request.md`
  - Created: `queries/2026-05-04-hermes-agents-teams-web-ui-instruction-request-summary.md`
- Ingested: `raw/notes/ai 시대 생존 전략.md`
  - Created: `queries/ai-시대-생존-전략-summary.md`
- Ingested: `raw/notes/AI 시대에 살아남는 학습자의 비밀.md`
  - Created: `queries/ai-시대에-살아남는-학습자의-비밀-summary.md`
- Ingested: `raw/notes/AI가 다 한다는데 그래도 코딩을 가르쳐야 할까요.md`
  - Created: `queries/ai가-다-한다는데-그래도-코딩을-가르쳐야-할까요-summary.md`
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
  - Created: `queries/chatgpt-가-출현하고-3년-6개월,-바뀐-세상-적응하지-못한-사람들-summary.md`
- Ingested: `raw/notes/컴퓨터활용능력 자격증 앞으로도 필요할까.md`
  - Created: `queries/컴퓨터활용능력-자격증-앞으로도-필요할까-summary.md`
- Ingested: `raw/notes/학생들에게 컴퓨터학과에 가지 않기를 조언합니다..md`
  - Created: `queries/학생들에게-컴퓨터학과에-가지-않기를-조언합니다.-summary.md`

## [2026-06-09] maintenance | Daily Vault Reconciliation
- Scanned raw/ directories: `raw/notes`, `raw/articles`, `raw/papers`.
- All non-empty raw files in `raw/notes` are already referenced in wiki source frontmatter.
- Detected and ignored empty placeholder files:
  - `raw/notes/2026-06-08.md`
  - `raw/notes/hermes-agent-skill-authoring.md`
  - `raw/notes/notebooklm-workflow.md`
  - `raw/notes/obsidian.md`
- Vault is internally consistent. No new content to process.

## [2026-06-10] ingest | Education shift post-ChatGPT
- Processed non-empty source: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created summary: `summaries/shift-in-education-labor-post-chatgpt.md`
- Created concepts: `concepts/vibe-coding.md`, `concepts/ai-assisted-education.md`
- Detected and recorded empty placeholders: `2026-06-08.md`, `hermes-agent-skill-authoring.md`, `notebooklm-workflow.md`, `obsidian.md` (no pages created)
- Updated `index.md` and `log.md`.

## [2026-06-10] ingest | Karpathy LLM Wiki pattern — knowledge management strategy
- Source read: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (llm-wiki.md)
- Created concept page: `wiki/concepts/knowledge-management-strategy.md`
  - Documents core philosophy (compounding wiki vs RAG), human/agent division of labor, 3-layer architecture, Ingest/Query/Lint operations, non-negotiable rules, and current vault state + cleanup plan.
- Strategy also saved to agent persistent memory.
- Next step proposed: run a full lint pass to fix index completeness, orphans, and nested-path duplication.

## [2026-06-10] lint | Full vault cleanup & restructure
- Diagnosis: vault had two parallel structures (root `summaries/concepts/entities/queries` vs canonical `wiki/...`). Content similarity analysis showed they were NOT duplicates (<0.55 similarity) but distinct unique content.
- Consolidation: `git mv` of 46 root content pages into canonical `wiki/` structure. 2 filename collisions preserved as `-alt` (`lets-coding-and-play-alt`, `seth-godin-alt`).
- Archived 4 empty placeholder files from `raw/notes/` to `_archive/raw/notes/`.
- Removed now-empty root dirs: `summaries/`, `concepts/`, `entities/`, `queries/`.
- Fixed 28 broken wikilinks: escaped skill links, empty `[[concepts]]`/`[[entities]]` placeholders removed, `media/*.mp4` links → inline code, remapped stale targets to existing pages.
- Added YAML frontmatter to 10 pages that lacked it.
- Regenerated `index.md` from scratch: 96 pages cataloged across 7 type sections (concepts, entities, comparisons, summaries, queries, agents, operations) + pointer section for edudata/시설관리/blog templates.
- Final lint: broken_links=0, frontmatter_missing=0, empty_files=0. Remaining: 44 pages reachable only via index (no page-to-page inbound) — to be cross-linked incrementally during future ingest/query.
- edudata/, 시설관리/, root Korean blog templates left untouched (separate projects).
