---
title: agentree-home 개발 히스토리
created: 2026-07-18
updated: 2026-07-18
type: project
tags: [ai-business, product, git, history]
sources:
  - ~/Documents/workspace/agentree-home (git log 176 commits, 2026-04-27 ~ 2026-07-18)
---

# agentree-home 개발 히스토리

[[projects/agentree-home/overview|agentree-home]] 저장소의 커밋 히스토리 분석 (2026-07-18 기준 176 커밋).

## 저장소 상태
- 기간: 2026-04-27 (create-next-app) ~ 2026-07-18 (진행 중)
- 기여자: foresightvalue-create(102) · quirinal36(47) · 성영태(29) · leehg(1)
- 브랜치: `main` + 원격 `redesign/claude-code`, `redesign/codex` — Claude Code와 Codex로 각각 리디자인을 시도한 흔적

## 전개 5단계
1. **4월 말 — 초기 구축**: B2B 신뢰형 톤으로 홈페이지 카피·레이아웃 집중 다듬기
2. **5월 — 커뮤니티 축 추가**: 커뮤니티 중심 리디자인, Supabase 신청 페이지, `/agents` 역할 카탈로그, GEO 섹션 도입
3. **6월 — 대규모 리디자인 + 오픈강의 인프라**: 6/9 하루 20여 커밋으로 "Agent Operations Console" 9섹션 개편, AI 도입 성숙도(L1~L4) 위젯, 탭형 워크플로우 애니메이션. 이어 `/open` 랜딩, `/admin` 대시보드, Paperclip 페이지
4. **7월 초 — SEO/GEO 총력전**: sitemap·robots·JSON-LD·llms.txt·RSS, 전주·전북 지역 페이지, 구글·네이버 인증, IndexNow → [[concepts/geo-generative-engine-optimization|GEO]]
5. **7월 중순~ — 오픈강의 D-day 운영 모드**: Hermes 강의 슬라이드(세션 1 v7.2, 세션 2 AX 덱)와 출석·현황·문자 알림 기능 집중 → [[projects/agentree-home/open-lecture-ops|오픈강의 운영 시스템]]

## 관찰 포인트
- 오픈강의 날짜가 6/15 → 7/13 → **7/20**으로 두 번 연기된 이력이 커밋에 남아 있음
- 주간 커밋: W28 21개 → W29 37개 — 강의일이 다가올수록 급증
- 최근 커밋의 압도적 다수가 `feat(slides)` — 코드보다 강의 콘텐츠가 주 작업물

## 관련 페이지
- [[entities/agentree|Agentree (에이전트리)]]
- [[projects/agentree-home/overview|저장소 개요]]
- [[projects/agentree-home/open-lecture-ops|오픈강의 운영 시스템]]
