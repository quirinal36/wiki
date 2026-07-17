---
title: "자동 Wiki 지식 수집기 (Auto Wiki Collector)"
created: 2026-07-17
updated: 2026-07-17
type: concept
tags: [knowledge-management, automation, wiki, hermes-agent]
sources:
  - yellow-auto-collect: 2026-07-17
---

# 자동 Wiki 지식 수집기 (Auto Wiki Collector)

## 정의
Auto Wiki Collector는 Yellow(Hermes Agent 지휘자)가 대화 중 가치 있는 지식을 **사용자 승인 없이 자동으로** `~/wiki` 지식 베이스에 기록하는 시스템이다.

## 왜 중요한가
- **지식 누수 방지**: 대화 중 오가는 귀중한 인사이트가 휘발되지 않는다
- **승인 마찰 제거**: "이거 wiki에 넣어도 될까요?" 확인 과정 없이 자동 축적
- **지식 베이스 성장**: wiki가 자연스럽게 살아있는 지식 저장소로 진화한다
- **재발견 비용 절감**: 과거에 논의했던 내용을 다시 검색해서 찾을 수 있다

## 작동 방식

### 3가지 자동 수집 트리거
1. **대화 인사이트**: 새로운 개념 정의, 중요한 결정, 교훈, 설정 정보
2. **대규모 Input**: 문서·URL·영상요약·NotebookLM 출력 등 외부 자료
3. **프로젝트 중요 정보**: 아키텍처 결정, 기술 선택 이유, 배운 점

### 판단 로직
- ✅ 기록: 여러 번 참조될 정보, 중요한 결정, 환경 정보, 방법론
- ❌ 무시: 일회성 질문답변, 중복 정보, 사소한 잡담
- 애매하면 기록하는 쪽 선택 (저장 비용 < 재발견 비용)

### 구현
Yellow의 AGENTS.md §6에 통합되어 있으며, `auto-wiki-collector` skill에 상세 규칙이 정의되어 있다. 별도의 cronjob 없이 Yellow의 대화 처리 흐름에서 즉시 실행된다.

## 관련 개념
- [[concepts/llm-wiki|LLM Wiki]] — 이 시스템의 기반이 되는 지식 관리 패턴
- [[concepts/knowledge-management-strategy|지식관리 전략]] — wiki 운영의 상위 전략
- [[concepts/obsidian-workflow|Obsidian Workflow]] — wiki 탐색 및 네비게이션 계층

## 기술 구현
상세 스펙은 [[agents/auto-wiki-collector|Auto Wiki Collector 스킬 스펙]] 참조.