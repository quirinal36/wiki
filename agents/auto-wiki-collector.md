---
title: "Auto Wiki Collector — Skill Spec"
created: 2026-07-17
updated: 2026-07-17
type: query
tags: [hermes-agent, skill, automation, wiki, knowledge-management]
sources:
  - yellow-auto-collect: 2026-07-17
---

# Auto Wiki Collector — Skill Spec

## 개요
Yellow의 Hermes skill로 구현된 자동 wiki 지식 수집 시스템. 
Skill 위치: `~/.hermes/profiles/yellow/skills/productivity/auto-wiki-collector/SKILL.md`

## 트리거 유형별 액션

### Type 1: 대화 인사이트
- **감지**: 새로운 개념, 결정, 교훈, 설정 정보
- **액션**: concepts/entities/operations에 생성 또는 업데이트 → index.md, log.md 갱신

### Type 2: 대규모 Input
- **감지**: 문서, URL, 영상요약, NotebookLM 출력
- **액션**: raw/ 저장 → summaries/ 요약 → entities/concepts 추출 및 생성/업데이트 → index.md, log.md 갱신

### Type 3: 프로젝트 정보
- **감지**: 아키텍처 결정, 기술 선택, 배운 점
- **액션**: projects/<name>/에 페이지 생성/업데이트 → 연관 concepts와 연결 → index.md, log.md 갱신

## 판단 기준

| 기록 ✅ | 무시 ❌ |
|---------|---------|
| 여러 번 참조될 정보 | 일회성 질문답변 |
| 중요한 분기점 결정 | 이미 wiki에 있는 중복 정보 |
| 사용자 환경/설정 정보 | 사소한 잡담 |
| 새로운 방법론/프레임워크 | 작업 진행 상황 |
| 에이전트 운영 함정/해결책 | 불확실한 추측 |

## 통합 포인트
- **Yellow AGENTS.md §6**: 기본 행동 지침
- **~/wiki/AGENTS.md**: 모든 wiki 작업의 규칙 준수 (Non-Negotiable Rules, Ingest Workflow, Frontmatter)

## 관련 페이지
- [[concepts/auto-wiki-collector|자동 Wiki 지식 수집기 개념]]
- [[agents/hermes-skills-overview|Hermes Skills Overview]]
- [[concepts/llm-wiki|LLM Wiki]]