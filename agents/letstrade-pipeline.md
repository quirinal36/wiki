---
title: letsTrade 아침 브리핑 파이프라인
created: 2026-04-27
updated: 2026-04-27
type: operation
tags: [letstrade, pipeline, hermes, orchestration, korean-market, trading, agents]
sources: []
aliases: [morning briefing pipeline, letstrade pipeline, 아침 브리핑]
status: active
---

# letsTrade 아침 브리핑 파이프라인

## 목적

매일 아침 **사용자가 전달한 ticker 번호**를 기반으로 개별 주식 분석 브리핑을 Slack으로 전송한다.

- ETF 사용 금지 — 개별 회사 종목만 분석
- fallback ticker(005930, 000660)는 사용하지 않음
- 최종 결과물: 슬랙 채널 `C0ASSF514M8`에 한국어 메시지

---

## Parent Orchestrator

**Agent:** `lets_manager`
**지시문 파일:** `/home/leehg/github/Agents/orchestrator_instruction.md`
**Hermes profile:** `~/.hermes/profiles/lets_manager/`

```bash
# 실행 방법
hermes -p lets_manager chat -q "$(cat /home/leehg/github/Agents/orchestrator_instruction.md)"
```

---

## 파이프라인 구조

```
Step 0  — Run 디렉토리 생성 (RUN_ID, RUN_DIR)
Step 1  — [병렬] news / sentiment / sector
Step 1.5 — [순차] ticker 추출 (sector.md에서 종목코드 2개)
Step 2  — [병렬] fundamental / technical  (TICKER_A, TICKER_B 대상)
Step 3a — [병렬] bull / bear  (두 종목 동시 분석)
Step 3b — [순차] facilitator  (bull + bear 비교 → 최종 입장)
Step 4  — [병렬] aggressive / neutral / conservative
Step 5  — [순차] 가중평균 합산 (20/50/30%)
Step 6  — [순차] trader → Slack 전송
```

---

## 각 Agent의 역할과 출력

### Step 1 — Market-Level Analysis (병렬)

| Agent | 출력 파일 | 핵심 내용 |
|-------|----------|---------|
| `news` | `news.md` | 최근 12h 뉴스 요약, VIX/USD-KRW/US10Y 컨텍스트 |
| `sentiment` | `sentiment.md` | 외국인·기관·개인 수급, 공매도 비율 |
| `sector` | `sector.md` | 섹터 순위 1위 + 개별 종목 2개 (6자리 코드) |

`sector.md` 출력 형식 (파서가 의존):
```
섹터 순위: 1위 <섹터명>, score <X>
추천 종목 (개별 주식):
  - 종목A: <6자리코드> / <회사명> / <이유>
  - 종목B: <6자리코드> / <회사명> / <이유>
```

### Step 1.5 — Ticker 입력 검증 (순차)

`lets_manager`는 사용자가 전달한 ticker 번호를 그대로 사용한다.  
입력 ticker가 없으면 진행하지 않는다.  
legacy fallback인 `005930`(삼성전자), `000660`(SK하이닉스)는 현재 사용하지 않는다.

### Step 2 — Stock-Specific Analysis (병렬)

| Agent | 출력 파일 | 핵심 내용 |
|-------|----------|---------|
| `fundamental` | `fundamental.md` | PER/PBR/ROE, 외국인 수급, 재무 요약 (두 종목 비교) |
| `technical` | `technical.md` | RSI/MACD/볼린저, 손절가=max(스윙저점, 현가-2×ATR) |

### Step 3a — Debate (병렬)

| Agent | 출력 파일 | 핵심 내용 |
|-------|----------|---------|
| `bull` | `bull.md` | 두 종목 강세 논거 + 오늘 주력 종목 선택 |
| `bear` | `bear.md` | 두 종목 약세 논거 + 무효화 조건 (필수) |

### Step 3b — Facilitator (순차)

`bull.md` + `bear.md` 비교 → 신뢰도 델타 규칙 (>0.2 = 명확한 방향, else neutral) → `facilitator.md`

### Step 4 — Risk Management (병렬)

| Agent | 가중치 | Max 포지션 | 손절 |
|-------|--------|-----------|------|
| `aggressive` | 20% | 35% | -10% |
| `neutral` | 50% | 25% | -7% |
| `conservative` | 30% | 15% | -5% |

### Step 5 — Synthesis (순차)

3개 의견 가중평균 → 최종 포지션 크기 & 손절 수준 → `synthesis.md`

### Step 6 — Trader (순차)

`synthesis.md` + `facilitator.md` → Slack 메시지 → `C0ASSF514M8` 채널 → `trader.md`

---

## Spawn 명령 패턴

```bash
# 단일 agent 실행
hermes -p <profile> chat -q "<prompt>" > $RUN_DIR/<profile>.md 2>&1

# 병렬 실행 (백그라운드)
hermes -p news     chat -q "<news_prompt>"     > $RUN_DIR/news.md     2>&1 &
hermes -p sentiment chat -q "<sentiment_prompt>" > $RUN_DIR/sentiment.md 2>&1 &
hermes -p sector   chat -q "<sector_prompt>"   > $RUN_DIR/sector.md   2>&1 &
wait
```

---

## Run 디렉토리 구조

```
/home/leehg/github/Agents/runs/<YYYYMMDD_HHMMSS>/
├── news.md
├── sentiment.md
├── sector.md
├── tickers.md          ← TICKER_A, TICKER_B
├── fundamental.md
├── technical.md
├── bull.md
├── bear.md
├── facilitator.md
├── aggressive.md
├── neutral.md
├── conservative.md
├── synthesis.md
├── trader.md           ← 실제 Slack으로 전송된 메시지
└── run_summary.json
```

---

## Portfolio Constraints

| 항목 | 값 |
|------|---|
| 총 포트폴리오 | 4,000만원 |
| 현금 플로어 | 15% 이상 유지 |
| 일별 손실 한도 | -3% |
| 기본 손절 | -7% |

---

## 사용하는 Skills

| Skill | 사용 Agent |
|-------|-----------|
| [[skill-feed-collector|feed-collector]] | `news`, `sector`, `fundamental`, `sentiment` |
| [[skill-ls-broker|ls-broker]] | `lets_manager`, `technical`, `trader`, `aggressive`, `neutral`, `conservative` |

---

## Error Handling

| 상황 | 조치 |
|------|------|
| `sector.md` 미출력 또는 파싱 실패 | 사용자 ticker 입력이 없을 때만 legacy fallback을 고려했으나, 현재 운영 문서에서는 사용하지 않음. 입력이 없으면 진행 중단 |
| Step 2 agent 실패 | 분석 없이 진행, bull/bear에 "분석 없음" 명시 |
| Bull/Bear 한쪽 실패 | facilitator는 존재하는 쪽만 활용, neutral 입장 |
| 3개 risk 모두 0% | trader는 관망 메시지 발송 |
| Slack 전송 실패 | 1회 재시도, 실패 시 `trader_unsent.md` 저장 |

---

## Ticker-based runbook
- [[letstrade-user-ticker-pipeline-runbook]] — this document gives the current operational sequence for user-provided ticker runs.

## 제약사항
- cron job 생성/수정 금지 (orchestrator 역할 외)
- child agents는 추가 child를 spawn하지 않음
- 총 실행 목표: 시작 후 15분 이내 완료
- 각 병렬 그룹 타임아웃: 600초
