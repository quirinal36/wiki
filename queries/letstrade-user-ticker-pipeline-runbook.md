---
title: letsTrade 사용자 ticker 기반 실행 매뉴얼
created: 2026-04-27
updated: 2026-04-27
type: query
tags: [letstrade, workflow, hermes, trading, automation]
sources:
  - raw/notes/2026-04-27-letstrade-user-ticker-pipeline-runbook-request.md
aliases: [letstrade ticker pipeline runbook, user ticker pipeline manual, letsTrade 실행 매뉴얼]
status: active
---

> Source note: `raw/notes/2026-04-27-letstrade-user-ticker-pipeline-runbook-request.md`

# letsTrade 사용자 ticker 기반 실행 매뉴얼

## User question
방금 실행했던 letsTrade pipeline 실행 과정을 wiki 문서로 남겨서, 앞으로도 같은 방식으로 실행할 수 있게 해달라는 요청.

## Short answer
이 파이프라인은 이제 **사용자가 전달한 ticker 번호만** 분석한다.  
기본 fallback ticker(`005930`, `000660`)는 사용하지 않는다.  
실행 시에는 `lets_manager`를 부모 orchestrator로 두고, ticker별 분석 → 병렬 의견 수집 → synthesis → trader 정리 순서로 진행한다.

## 언제 이 문서를 쓰는가
- 사용자가 ticker 번호를 직접 전달했을 때
- 기존 `sector.md` 기반 종목 추출 대신, **입력 ticker 고정 분석**을 해야 할 때
- `lets_manager` 브리핑을 Slack-ready 한국어 메시지로 만들고 싶을 때

## 실행 원칙
1. **입력 ticker 우선**
   - 사용자가 준 ticker 번호만 분석한다.
   - 내부 추천 ticker나 고정 fallback ticker로 대체하지 않는다.

2. **모든 agent는 같은 모델 계열을 사용**
   - 현재 letsTrade pipeline family는 `gpt-5.4-mini`를 사용한다.
   - 프로필별 설정은 따로 있어도, 동일 provider/auth 풀을 재사용한다.

3. **최종 메시지는 trader가 정리**
   - trader는 Slack 전송용 최종 문구를 다듬는 마지막 단계다.
   - 최종 출력은 한국어, 간결, 실행 중심이어야 한다.

4. **cron job은 만들지 않는다**
   - 이 문서는 실행 매뉴얼이며, 새 cron job 생성 문서는 아니다.

## 표준 실행 순서

### Step 0. 사전 점검
- `lets_manager`와 하위 profile들이 `gpt-5.4-mini`로 설정되어 있는지 확인한다.
- `openai-codex` auth 상태를 확인한다.
- credential pool이 exhausted 상태면 먼저 reset 한다.

권장 확인 명령:
```bash
hermes auth status openai-codex
hermes auth reset openai-codex
hermes profile list
```

### Step 1. ticker 입력 확정
- 사용자가 전달한 ticker 번호를 그대로 적는다.
- 예시: `058430`, `042700`
- ticker가 여러 개면 모두 분석한다.
- ticker가 없으면 진행하지 말고 입력 부족을 명시한다.

### Step 2. 시장 컨텍스트 수집
- 전체 시장 분위기, KOSPI/KOSDAQ, 환율, 수출/반도체/철강 같은 공통 테마를 수집한다.
- ticker별 분석 전에 공통 매크로 배경을 만든다.

### Step 3. ticker별 개별 분석
각 ticker마다 아래 관점으로 분리해서 본다.
- **Bull**: 상승 논거, 모멘텀, 업황 수혜
- **Bear**: 리스크, 실적/일정 지연, 밸류 부담
- **Risk**: 무효화 조건, 손절/주의 포인트

### Step 4. 병렬 의견 수집
- 뉴스/시장/강세/약세/리스크를 병렬로 모은다.
- 서로 다른 의견이 충돌하면 synthesis 단계에서 명시적으로 정리한다.

### Step 5. synthesis
- ticker별 핵심 요약을 만든다.
- 오늘의 시장 해석과 각 ticker의 watchpoint를 묶는다.
- 최종 메시지는 4~8개 bullet로 압축한다.

### Step 6. trader 정리
- trader가 최종 Slack 문구를 만든다.
- 문구는 한국어, 짧고 실무적이어야 한다.
- 제목/서론/장황한 설명은 넣지 않는다.

## 이번 실행에서 사용한 패턴
이번에는 다음 ticker를 기준으로 실행했다.
- `058430` — POSCO STEELEON
- `042700` — Hanmi Semiconductor

이 패턴을 앞으로도 그대로 쓸 수 있다:
1. 사용자가 ticker 전달
2. ticker만 기준으로 분석 범위 고정
3. 공통 시장 컨텍스트 수집
4. ticker별 bull/bear/risk 정리
5. synthesis
6. trader용 최종 Slack 메시지 작성

## 예시 실행 프롬프트
```text
다음 ticker 번호를 기준으로 letsTrade morning briefing pipeline을 실행한다.
입력 ticker: 058430, 042700
규칙:
- 사용자가 전달한 ticker만 분석
- 005930, 000660 같은 fallback ticker 사용 금지
- 한국어로 Slack-ready하게 간결하게 정리
- 시장 컨텍스트, ticker별 watchpoint, 리스크, 오늘의 액션을 포함
```

## 표준 실행 프롬프트 템플릿

아래 템플릿을 그대로 복사해서 쓰면 된다.  
핵심은 **사용자가 전달한 ticker만 분석**하고, **fallback ticker를 절대 쓰지 않는 것**이다.

```text
다음 ticker 번호를 기준으로 letsTrade morning briefing pipeline을 실행해줘.

입력 ticker: {ticker1}, {ticker2}, ...

규칙:
- 사용자가 전달한 ticker만 분석한다.
- 005930, 000660 같은 fallback ticker는 사용하지 않는다.
- ticker가 없으면 임의로 추정하지 말고, 입력이 부족하다고 알려준다.
- lets_manager를 부모 orchestrator로 사용한다.
- 모든 분석 agent는 gpt-5.4-mini 기준으로 동작하도록 맞춘다.
- 시장 컨텍스트, ticker별 bull/bear/risk, 오늘의 watchpoint, 실행 포인트를 포함한다.
- 최종 결과는 한국어 Slack-ready 문장으로 4~8개 bullet 이내로 압축한다.
- 제목, 서론, 장황한 설명은 넣지 않는다.
- trader agent가 마지막 문구를 정리한다.
```

### 추천 사용 예시
```text
다음 ticker 번호를 기준으로 letsTrade morning briefing pipeline을 실행해줘.
입력 ticker: 058430, 042700
규칙:
- 사용자가 전달한 ticker만 분석
- 005930, 000660 fallback 금지
- 한국어 Slack-ready로 간결하게 정리
- 시장 컨텍스트, ticker별 watchpoint, 리스크, 오늘의 액션 포함
```

## Troubleshooting

### 1) `No Codex credentials stored`가 뜰 때
- `hermes auth status openai-codex`로 상태를 확인한다.
- credential pool이 exhausted면 `hermes auth reset openai-codex`를 먼저 실행한다.
- 그 후 다시 실행한다.

### 2) pipeline이 예전처럼 2개 고정 종목을 쓰는 것 같을 때
- `~/.hermes/profiles/lets_manager/SOUL.md`를 확인한다.
- `cronjobInstruction.md`에서 fallback ticker 문구가 남아 있지 않은지 확인한다.
- `wiki/agents/letstrade-pipeline.md`의 ticker 추출 규칙도 함께 확인한다.

### 3) 결과가 너무 길 때
- 최종 Slack 문구는 4~8 bullet로 압축한다.
- 표보다 bullet이 우선이다.
- 숫자는 핵심만 남기고 나머지는 synthesis에 둔다.

## Related pages
- [[agents/letstrade-pipeline]]
- [[agents/index]]
- [[long-term-vault-operating-policy]]
- [[hermes-agent-registry]]

## Supporting wiki pages
- [[trader-agent]]
- [[hermes-agent]]
- [[obsidian-workflow]]
- [[llm-wiki]]
