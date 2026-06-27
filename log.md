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
<<<<<<< HEAD
- Created summary: [[summaries/chatgpt-and-the-new-reality-for-coding-academies|summaries/chatgpt-and-the-new-reality-for-coding-academies.md]]
=======
- Created summary: [[chatgpt-3.5-years-later|summaries/chatgpt-anniversary-edu-shift.md]]
>>>>>>> 5678dc7f96a253d9b93937b99c43e1388b434147
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
- Created: [[linchpin-and-tribe-strategy]], [[seth-godin]], [[art-as-work-strategy]]
- Detected placeholder `raw/notes/무제.base` as stub, ignoring.

## [2026-05-26] update | Daily maintenance
- Ingested: raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md
- Created: summaries/post-chatgpt-education-paradigm.md
- Created: concepts/vibe-coding.md

## [2026-05-27] maintenance | Batch Process Daily
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
<<<<<<< HEAD
- Created summary: [[summaries/chatgpt-and-the-new-reality-for-coding-academies]]
=======
- Created summary: [[chatgpt-3.5-years-later]]
>>>>>>> 5678dc7f96a253d9b93937b99c43e1388b434147
- Created concept: [[concepts/vibe-coding]]
- Updated `index.md` and page counts.
- Verified wikilinks and source frontmatter.

## [2026-05-29] maintenance | Batch Process Daily
<<<<<<< HEAD
- Ingested: raw/notes/ai 를 이기는 생각방법.md -> [[summaries/linchpin-and-tribe-strategy]]
=======
- Ingested: raw/notes/ai 를 이기는 생각방법.md -> [[linchpin-and-tribe-strategy]]
>>>>>>> 5678dc7f96a253d9b93937b99c43e1388b434147


## [2026-05-29] maintenance | Automated Batch Ingest
- Skipped empty file: raw/notes/ai 시대 생존 전략.md
- Skipped empty file: raw/notes/AI 시대에 살아남는 학습자의 비밀.md
- Skipped empty file: raw/notes/컴퓨터활용능력 자격증 앞으로도 필요할까.md


## [2026-05-30] maintenance | Vault Clean
- Scanned `raw/` directories: `raw/notes`, `raw/articles`, `raw/papers`.
- No unreferenced/non-empty files found. Everything up to date.

## [2026-05-31] maintenance | Ingested Educations Paradigm Note
- Ingested: `raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md`
- Created: `summaries/chatgpt-and-the-new-reality-for-coding-academies.md`
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
- Created summary: `summaries/chatgpt-and-the-new-reality-for-coding-academies.md`
- Created concepts: `concepts/vibe-coding.md`, `concepts/ai-assisted-education.md`
- Detected and recorded empty placeholders: `2026-06-08.md`, `hermes-agent-skill-authoring.md`, `notebooklm-workflow.md`, `obsidian.md` (no pages created)
- Updated `index.md` and `log.md`.

<<<<<<< HEAD
## [2026-06-24] maintenance | Daily vault reconciliation
- raw/notes/2026-06-08.md: Detected but empty/blank. Skipped.
- ingested | ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들 (from raw/notes/ChatGPT 가 출현하고 3년 6개월, 바뀐 세상 적응하지 못한 사람들.md)
- raw/notes/hermes-agent-skill-authoring.md: Detected but empty/blank. Skipped.
- raw/notes/notebooklm-workflow.md: Detected but empty/blank. Skipped.
- raw/notes/obsidian.md: Detected but empty/blank. Skipped.
                    
## [2026-06-24] restructure | 폴더 구조 SOUL 기준 통일 + 중복 정리
- 안전 백업: `_backup/vault-snapshot-*.tgz` 생성 (rm 불가 마운트라 삭제 대신 _archive 사용).
- Phase 1 — 폴더 통일: `wiki/` 하위를 루트로 승격.
  - wiki/concepts→concepts, wiki/comparisons→comparisons, wiki/queries→queries
  - wiki/agents→agents, wiki/operations→operations(+hermes-control-interface 파일)
  - wiki/entities→entities, wiki/summaries→summaries
  - edudata·시설관리→projects/, 루트 템플릿 md 3종→templates/
  - 빈 wiki/ 트리는 _archive/wiki-empty로 이동.
- Phase 2 — basename 충돌 5건 해결:
  - entities/seth-godin: 2개 병합 → 1개(canonical, 풍부한 버전 기준).
  - entities/lets-coding-and-play: 3개(and-play/play/wiki) 병합 → 1개. 끊긴 링크 lets-coding-play→lets-coding-and-play 수정.
  - instruction.md 충돌: 상세본→queries/hermes-web-ui-instruction-guide.md, 빈약본 보관. 기존 instruction 링크 수정.
  - letstrade runbook 충돌: 상세 query→queries/, 짧은 summary→summaries/letstrade-ticker-run-record.md.
  - agents/operations 서브 index.md→<folder>-index.md로 개명.
- Phase 3 — summaries 중복 통합: 7개 원본 기사에 흩어진 31개 요약을 원본별 1개 canonical로 통합. 23개를 _archive/summaries-dupes로 보관. inbound 링크 전부 canonical로 재연결. (coding-syntax-drills-vs-vibe-coding는 comparison 성격이라 별도 유지)
  - canonical: chatgpt-and-the-new-reality-for-coding-academies, linchpin-and-tribe-strategy, advice-against-computer-science-majors, computer-utilization-certification-and-ai-spreadsheets, ai-era-survival-strategy, ai-era-learning-survival-secret, should-we-still-teach-coding
- 마무리: index.md 전체 재생성(폴더/타입별), 깨진 링크 스캔·수정(ai-assisted-learning→ai-assisted-education, letstrade→letstrade-pipeline).
- 남은 알려진 이슈: hermes-empire 미해결 링크(기존부터), concepts에 vibe-coding 3종 중복(vibe-coding/vibecoding/vibe-coding-education) — 차기 정리 후보.
=======
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

## [2026-06-25] lint | Vault 헬스체크 및 중복 통합
- 전체 lint 실행: 깨진 링크, 고립 노트, 중복, frontmatter, index 정합성 점검.
- 중복 통합: 같은 원본을 요약한 중복 노트 33개 삭제(원본당 1개 canonical 유지).
  - summaries/ 22개 삭제: ChatGPT 교육(9→1), 린치핀·부족(5→1), 생존전략·학습자비밀·컴활·컴퓨터학과·코딩교육(각 3→1).
  - concepts/ 1개 삭제: vibecoding → vibe-coding 통합.
  - entities/ 3개 삭제: lets-coding-and-play(3→1, 수어번역 프로젝트 병합), seth-godin(2→1).
  - queries/ 7개 삭제: 한글 article-summary 중복 → summaries canonical로 통합.
- 링크 재연결: 17개 파일의 wikilink를 canonical 노트로 갱신.
- index.md 재생성: 총 페이지 96(표기)/100 → 67로 정정, 한 줄 요약 갱신.
- frontmatter 추가: hermes-control-interface-external-access.md.
- 참고: agent/letstrade/hermes-web-ui/claw-empire 등 운영 request 요약 중복은 보존(추가 검토 권장).
- wiki md: 100 → 67. (git 추적, 복구 가능)

## [2026-06-25] ingest | AI 시대의 대전환 브리핑
- raw/articles/2026-06-25-ai-transformation-industry-labor-talent.md 저장 (원문 보존).
- summaries/ai-era-transformation-industry-labor-talent.md 생성 (산업·노동·인재·교육 4축 요약).
- 신규 개념 3개 생성:
  - concepts/frontier-ecosystem.md (프런티어 생태계, 나델라)
  - concepts/four-muscles-generalist.md (4대 근육·제너럴리스트, 최태원)
  - concepts/end-of-work-uhi.md (노동의 종말·UHI, 머스크)
- 기존 노트 연결: linchpin-strategy, critical-ai-literacy, art-as-work-strategy, learner-agency, ai-assisted-education, llm-wiki, AI_전쟁은_모델을_넘어섰다_요약.
- index.md 갱신.
>>>>>>> 5678dc7f96a253d9b93937b99c43e1388b434147
