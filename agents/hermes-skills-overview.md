---
title: Hermes Skills Overview
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [hermes, skills, agent, orchestration, python]
sources: []
aliases: [hermes skill system, custom skill, external skill]
status: active
---

# Hermes Skills Overview

## Skills란 무엇인가

Hermes의 **skill**은 agent가 특정 데이터 소스나 외부 시스템에 접근하는 방법을 표준화한 문서다.
`SKILL.md` 파일 하나로 정의되며, agent는 이 문서를 컨텍스트로 읽고 코드 패턴을 그대로 실행한다.

> Skill은 코드 라이브러리가 아니라 **실행 가능한 레시피 문서**다.
> 어떤 모델이 agent를 구동하든 동일한 코드를 실행할 수 있도록 작성해야 한다.

---

## 파일 구조

```
/home/leehg/github/Agents/skills/
├── feed-collector/
│   └── SKILL.md        ← FeedCollector Supabase 쿼리
└── ls-broker/
    └── SKILL.md        ← LS증권 계좌/시세 조회
```

각 `SKILL.md`는 YAML frontmatter + Markdown 본문으로 구성된다:

```markdown
---
name: skill-name
description: 한 줄 설명 (agent가 이 skill을 쓸지 말지 판단하는 근거)
version: 1.0.0
metadata:
  hermes:
    tags: [tag1, tag2]
    related_skills: [other-skill]
---

# 본문: 쿼리 패턴들 (복사-붙여넣기 가능한 코드 포함)
```

---

## Profiles에 등록하는 방법

각 Hermes profile의 `config.yaml`에서 `skills.external_dirs`에 경로를 추가한다:

```yaml
skills:
  external_dirs:
  - /home/leehg/github/Agents/skills
```

**등록된 profiles (2026-04-27 기준):**
`lets_manager`, `news`, `sector`, `fundamental`, `sentiment`,
`technical`, `bull`, `bear`, `facilitator`, `trader`,
`aggressive`, `neutral`, `conservative`

---

## 좋은 Skill 문서의 요건

모델이 바뀌어도 흔들리지 않으려면 다음 조건을 갖춰야 한다:

| 요건 | 이유 |
|------|------|
| `sys.path.insert` 등 경로 설정이 코드 안에 포함 | 모델이 환경을 모르므로 self-contained여야 함 |
| 환경 변수 목록과 기본값 명시 | 실패 시 원인을 즉시 알 수 있어야 함 |
| 반환값 예시 (JSON) 포함 | 모델이 후속 처리 코드를 올바르게 작성할 수 있도록 |
| "언제 이 skill을 사용하는가" 섹션 | 어느 agent가 어떤 목적으로 쓰는지 명확히 |
| 주의사항 (read-only 여부 등) | 모델이 사이드이펙트를 발생시키지 않도록 |

---

## 현재 등록된 Skills

| Skill | 파일 | 핵심 기능 |
|-------|------|---------|
| [[skill-feed-collector\|feed-collector]] | `skills/feed-collector/SKILL.md` | Supabase에서 뉴스·트렌딩·종목 매칭 조회 |
| [[skill-ls-broker\|ls-broker]] | `skills/ls-broker/SKILL.md` | LS증권 계좌 잔고·실시간 현재가·주문 내역 조회 |

---

## Skill 추가 시 체크리스트

```
[ ] /home/leehg/github/Agents/skills/<name>/SKILL.md 작성
[ ] frontmatter: name, description, version, tags 채우기
[ ] 코드 패턴마다 반환값 예시 포함
[ ] "언제 이 skill을 사용하는가" 섹션 작성
[ ] 주의사항 (read-only / 환경변수 / 장외시간 등) 명시
[ ] 관련 profiles의 config.yaml external_dirs 등록 확인
[ ] 이 index 문서 업데이트
```
