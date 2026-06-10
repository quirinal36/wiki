# Hermes Agent + Obsidian: Second Brain with Agent Team - 분석 노트

> 🎬 **원본 영상**: [Hermes Agents + Obsidian: My Second Brain Has a Team of Agents in Discord](https://www.youtube.com/watch?v=L0hs3-xBjJE)
> ⏱️ **길이**: 17:19
> 📅 **분석일**: 2026-06-07
> 🤖 **분석 도구**: NotebookLM (notebook: `hermes with notebooklm`)

---

## 🎯 핵심 인사이트

### 1. 자기개선 루프 (Self-Improvement Loop) — 가장 혁신적인 기능

Hermes Agent의 가장 차별화된 특징은 **사용할수록 똑똑해지는 자기학습 루프**:

| 트리거 | 액션 | 결과물 |
|--------|------|--------|
| 10턴마다 | Memory Review Agent 실행 | `user.md` 업데이트 (사용자 선호도/페르소나 기록) |
| 15턴마다 | Skill Review Agent 실행 | 관찰된 워크플로우 기반 새 스킬 자동 생성 |
| 새벽 4시 | Stale Session Review | 만료 예정 세션에서 최종 인사이트 추출 |

> 💡 **인상적인 실제 사례**: 사용자가 YouTube → NotebookLM 워크플로우를 반복하자, Hermes가 이를 감지하고 **자동으로 `notebooklm-workflow` 스킬을 생성**함. 사용자가 아무 지시도 하지 않았는데!

### 2. Discord 멀티에이전트 아키텍처

각 Discord 채널을 **독립된 에이전트 컨텍스트**로 구성:

- **Vault 채널**: Obsidian과 연동, 데일리 노트/위키 링크 위주
- **Content 채널**: YouTube/Substack 콘텐츠 제작용
- **Build 채널**: 코딩 작업용 (스킬 셋 제한)

각 채널마다 다른 페르소나와 스킬 셋을 설정할 수 있어서, 마치 여러 명의 전문 비서를 둔 것과 같은 경험을 제공.

### 3. 모바일 퍼스트 리서치 파이프라인

핵심 사용 사례: **폰으로 Discord에서 연구 지시 → Hermes가 NotebookLM으로 처리**

```
📱 Discord 메시지 → 🔍 YouTube 검색 → 📥 NotebookLM 소스 추가 → 🎙️ 팟캐스트 생성
```

이동 중에도 아이디어 캡처, 리서치, 콘텐츠 제작 가능.

### 4. 스킬 블롯(Skill Bloat) 문제와 해결책

- Hermes는 기본 200개 이상의 스킬을 번들로 제공
- **문제**: 스킬 설명이 전부 컨텍스트에 로드되어 모델이 혼란 → 잘못된 도구 선택
- **해결책**: 신뢰하는 스킬만 화이트리스트, 채널별 스킬 셋 제한

### 5. 오픈소스 + 모델 독립성

- Claude Code는 클로즈드 소스 (소스 코드 접근 불가, 시스템 프롬프트 수정 불가)
- Hermes는 모든 코드 공개, 모든 모델 지원 (OpenAI/Anthropic/로컬 모델)
- 시스템 프롬프트 완전 투명, 커스터마이징 가능

### 6. 딥워크 vs 모바일 캡처 전략

| 모드 | 도구 | 용도 |
|------|------|------|
| **딥워크** | Claude Code + Obsidian 나란히 | 진지한 분석, 계획 수립, AI slop 방지 |
| **모바일 캡처** | Hermes via Discord | 아이디어 브레인덤프, 빠른 리서치, 이동 중 작업 |

Hermes = **Capture Inbox + Research Fuel**

---

## 📊 NotebookLM 분석 요약

NotebookLM이 생성한 AI 요약:
> Hermes agent는 Obsidian 볼트를 Discord와 연결하는 오픈소스 프레임워크로, 자율 서브에이전트가 대화를 검토하여 사용자 선호도를 업데이트하고 **관찰된 워크플로우를 기반으로 새 스킬을 자동 생성**하는 자기개선 루프가 핵심 특징.

**주요 키워드**: Hermes AI Agent, Obsidian Vault Integration, Self-improvement Loop, Discord Multi-agent Channels, Personal Memory Management

---

## 🗂️ 생성된 아티팩트

| 아티팩트 | 상태 | 위치 |
|----------|------|------|
| 📝 보고서 (Blog Post) | ✅ 완료 | `summaries/2026-06-07-hermes-agent-video-review.md` |
| 🎙️ 오디오 개요 (Podcast) | ✅ 완료 | [[media/2026-06-07-hermes-agent-podcast.mp4]] (43MB, 영어 "Building a self-improving local second brain") |
| 🎙️ 오디오 개요 (한국어) | ✅ 완료 | [[media/2026-06-07-hermes-agent-podcast-ko.mp4]] (36MB, 한글 "밤새 스스로 도구를 깎는 AI 세컨드 브레인") |

---

## 🔗 관련 노트

- [[notebooklm-workflow]] - NotebookLM 통합 워크플로우
- [[hermes-agent-skill-authoring]] - Hermes 스킬 작성법
- [[obsidian]] - Obsidian 세컨드 브레인

---

## 💭 나의 생각 (Actionable Takeaways)

1. **자기학습 루프는 진짜 게임체인저** — 에이전트가 사용 패턴을 학습해 스킬을 자동 생성하는 기능은 다른 어떤 에이전트에서도 본 적 없는 혁신
2. **스킬 관리가 핵심** — 200개 번들 스킬은 오히려 독. 필요한 것만 활성화하는 전략 필수
3. **Discord 채널 분리가 현명한 아키텍처** — 컨텍스트 격리로 에이전트 정확도 향상
4. **Obsidian 심볼릭 링크는 필수** — Hermes 데이터를 Obsidian 볼트와 동기화하면 모든 메모리/세션/스킬을 위키에서 검색/조회 가능
