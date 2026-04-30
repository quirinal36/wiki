# Wiki Log

> Append-only record of wiki operations.

## [2026-04-18] create | wiki initialized
- Created AGENTS.md, index.md, log.md
- Created raw/, wiki/, schema/ structure

## [2026-04-19] setup | obsidian vault connected
- Installed obsidian-headless CLI (`ob`)
- Created working vault at `/mnt/c/Users/turbo/Documents/llm-wiki-vault`
- Added `.obsidian/app.json` with attachments routed to `raw/images`
- Created WSL shortcut path `/home/leehg/wiki`
- Configured Hermes wiki path and `OBSIDIAN_VAULT_PATH`

## [2026-04-19] create | start page and core pages
- Created `start-here.md`
- Created `wiki/entities/hermes-agent.md`
- Created `wiki/entities/trader-agent.md`
- Created `wiki/concepts/llm-wiki.md`
- Created `wiki/concepts/obsidian-workflow.md`
- Updated `index.md` with first navigation links

## [2026-04-19] ingest | ai 시대 생존 전략
- Source found at `raw/notes/ai 시대 생존 전략.md`
- Created `wiki/summaries/ai-era-survival-strategy.md`
- Created `wiki/entities/jang-dong-seon.md`
- Created `wiki/concepts/critical-ai-literacy.md`
- Created `wiki/concepts/ai-off-workflow.md`
- Updated `schema/tag-taxonomy.md` to include `evaluation`
- Updated `index.md`

## [2026-04-19] query | parent notice draft for ai use guide
- Created `wiki/queries/parent-notice-ai-use-guide.md`
- Updated `index.md`

## [2026-04-19] ingest | ai 시대에 살아남는 학습자의 비밀
- New unreferenced source detected at `raw/notes/AI 시대에 살아남는 학습자의 비밀.md`
- Created `wiki/summaries/ai-era-learning-survival-secret.md`
- Created `wiki/concepts/learner-agency.md`
- Created `wiki/concepts/school-as-learning-hub.md`
- Updated `schema/tag-taxonomy.md` to include `education` and `agency`
- Updated `index.md`

## [2026-04-19] scan | raw notes cleanup check
- Found `raw/notes/0419 발행 블로그 글.md` but it is currently empty, so no wiki page was created
- Verified newly added pages have no broken wikilinks

## [2026-04-19] ingest | 성실함이 무기가 되지 않는 시대, AI를 이기는 '린치핀'과 '부족'의 전략
- New unreferenced source detected at `raw/notes/ai 를 이기는 생각방법.md`
- Created `wiki/summaries/linchpin-and-tribe-strategy.md`
- Created `wiki/entities/seth-godin.md`
- Created `wiki/concepts/linchpin-strategy.md`
- Created `wiki/concepts/tribe-based-leadership.md`
- Updated `index.md`

## [2026-04-19] query | long-term vault operating policy
- Created `wiki/queries/long-term-vault-operating-policy.md`
- Updated `index.md`

## [2026-04-20] scan | daily raw inbox maintenance
- Compared raw files in `raw/notes`, `raw/articles`, and `raw/papers` against wiki page `sources:` entries
- Detected `raw/notes/2026-04-20.md` but it is empty, so no wiki page was created
- No new actionable non-empty raw files were found

## [2026-04-21] ingest | ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들
- Source found at `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created `wiki/summaries/chatgpt-and-the-new-reality-for-coding-academies.md`
- Created `wiki/entities/lets-coding-and-play.md`
- Created `wiki/concepts/ai-service-building-curriculum.md`
- Created `wiki/comparisons/certification-track-vs-project-track.md`
- Updated `index.md`
- Verified `raw/notes/2026-04-20.md` is empty; no wiki page was created

## [2026-04-22] scan | daily maintenance check
- Compared raw files in `raw/notes`, `raw/articles`, and `raw/papers` against wiki `sources:` entries
- Detected `raw/notes/2026-04-20.md` as empty; left it untouched
- Detected `raw/cardnews/0419 발행 블로그 글.md` as empty; left it untouched
- No actionable unprocessed raw files were found

## [2026-04-23] create | new agent creation manual
- Saved the user request into `raw/notes/2026-04-23-agent-creation-manual-request.md`
- Created `wiki/queries/new-agent-creation-manual.md`
- Created `wiki/queries/new-agent-creation-manual-source-link.md`
- Updated `index.md`

## [2026-04-23] update | link manual and source note
- Added cross-links between the raw request note and reusable manual via a helper wiki page
- Preserved raw immutability by leaving the source note unchanged

## [2026-04-23] create | Hermes agent registry
- Created a living registry page for current Hermes profiles and gateway states
- Added one-line purpose descriptions for each existing agent/profile
- Updated `index.md` so the registry is discoverable from the main catalog

## [2026-04-23] create | operations records folder
- Created `wiki/operations/` as a living folder for setup and development records
- Added `nas-teacher-bind-persistence.md` for the Synology teacher path persistence setup
- Added `operations/index.md` and linked the folder from the main catalog

## [2026-04-26] scan | daily maintenance check
- Vault path: /mnt/c/Users/turbo/Documents/llm-wiki-vault
- Raw file audit: All 5 raw files in raw/notes/ are referenced in wiki sources
- Unprocessed files: 0 (all raw materials have been ingested)
- Vault health: HEALTHY
  - 26 wiki pages, all with valid YAML frontmatter
  - All required frontmatter fields present (title, created, updated, type, tags, sources)
  - No broken wikilinks found
  - No orphan pages (all pages linked by index or other pages)
  - No stale pages (all updated within last 90 days)
  - No contradictions flagged
  - Page sizes reasonable (all under 300 lines)
- Raw directory structure: raw/notes (5 files), raw/articles (0 files), raw/papers (0 files)
- No action required; vault is up-to-date and well-maintained

## [2026-04-27] create | letsTrade user ticker pipeline runbook
- Saved the request context into `raw/notes/2026-04-27-letstrade-user-ticker-pipeline-runbook-request.md`
- Created `wiki/queries/letstrade-user-ticker-pipeline-runbook.md`
- Updated `wiki/agents/letstrade-pipeline.md` to use user-provided ticker numbers and remove fallback ticker behavior
- Added the new runbook to `index.md`
- Documented the gpt-5.4-mini / openai-codex execution pattern and auth reset troubleshooting
- Added a reusable standard execution prompt template for user-provided ticker runs

