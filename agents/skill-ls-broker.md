---
title: Skill — ls-broker
created: 2026-04-27
updated: 2026-04-27
type: operation
tags: [skill, hermes, ls-securities, broker, account, portfolio, realtime-price, korean-market]
sources: []
aliases: [ls-broker skill, LS증권 skill, broker skill, 계좌 조회]
status: active
---

# Skill: ls-broker

## 목적

LS증권 Open API를 통해 **실제 보유 종목**, **계좌 잔고**, **실시간 현재가**, **주문 내역**을 조회한다.
`/home/leehg/github/letsTrade/bot`의 `lets_trade` 패키지를 직접 import해서 사용한다.

## 파일 위치

```
/home/leehg/github/Agents/skills/ls-broker/SKILL.md
```

## 패키지 위치

```
/home/leehg/github/letsTrade/bot/src/lets_trade/api/
├── account.py    # AccountApi — 잔고/보유 종목
├── stock.py      # StockApi — 현재가/호가/체결
├── order.py      # OrderApi — 주문 내역 (주문 실행도 가능하나 skill에서는 금지)
├── history.py    # HistoryApi — 분봉/일봉/틱 차트
├── auth.py       # 토큰 발급/갱신 (LSApiClient 내부에서 자동 처리)
├── client.py     # LSApiClient — 공통 HTTP 클라이언트
└── config.py     # LSApiConfig — 환경변수 로드
```

---

## 환경 변수 (필수)

| 변수 | 설명 | 비고 |
|------|------|------|
| `LS_APP_KEY` | LS증권 앱키 | 없으면 ValueError |
| `LS_APP_SECRET` | LS증권 앱시크릿 | 없으면 ValueError |
| `LS_ACCOUNT_NO` | 계좌번호 10자리 | 기본값 빈 문자열 |
| `LS_ENVIRONMENT` | `simulation` 또는 `production` | 기본값 `simulation` |

> `production` 설정 시 **실제 계좌**에 접근한다. skill 사용 시에는 읽기 조회만 수행한다.

---

## sys.path 설정 (항상 포함)

모든 코드 스니펫에 첫 두 줄이 반드시 필요하다:

```python
import sys
sys.path.insert(0, "/home/leehg/github/letsTrade/bot/src")
```

---

## Query 1 — 계좌 잔고 + 보유 종목

파이프라인 시작 전 **현재 포트폴리오 상태** 파악에 사용.

```python
import sys, json
sys.path.insert(0, "/home/leehg/github/letsTrade/bot/src")

from lets_trade.api import LSApiClient, AccountApi

with LSApiClient() as client:
    balance = AccountApi(client).get_balance()

print(json.dumps({
    "deposit": balance.deposit,
    "available": balance.available,
    "total_eval": balance.total_eval,
    "total_profit": balance.total_profit,
    "profit_rate": round(balance.profit_rate, 2),
    "positions": [
        {
            "ticker": p.symbol,
            "name": p.name,
            "qty": p.quantity,
            "avg_price": round(p.avg_price),
            "current_price": p.current_price,
            "market_value": p.market_value,
            "profit_loss": round(p.profit_loss),
            "profit_rate": round(p.profit_rate, 2),
        }
        for p in balance.positions
    ]
}, ensure_ascii=False, indent=2))
```

반환 예시:
```json
{
  "deposit": 8500000,
  "available": 6200000,
  "total_eval": 42300000,
  "total_profit": 1850000,
  "profit_rate": 4.57,
  "positions": [
    {
      "ticker": "005930",
      "name": "삼성전자",
      "qty": 50,
      "avg_price": 72000,
      "current_price": 74500,
      "market_value": 3725000,
      "profit_loss": 125000,
      "profit_rate": 3.47
    }
  ]
}
```

**사용 agent:** `lets_manager` (포지션 파악), `risk agents` (available 기준 포지션 크기 계산)

---

## Query 2 — 실시간 현재가 (단일 / 복수)

추천 종목의 **실제 시장가** 확인. Slack 메시지에 현재가 기재 시 필수.

```python
import sys, json
sys.path.insert(0, "/home/leehg/github/letsTrade/bot/src")

from lets_trade.api import LSApiClient, StockApi

with LSApiClient() as client:
    stock = StockApi(client)

    # 단일 종목
    p = stock.get_price("000660")
    print(f"{p.name}({p.symbol}): {p.price:,}원 ({p.change_rate:+.2f}%)")

    # 복수 종목 일괄
    prices = stock.get_multiple_prices(["005930", "000660"])
    for ticker, p in prices.items():
        print(json.dumps({
            "ticker": p.symbol, "name": p.name,
            "price": p.price, "change": p.change,
            "change_rate": p.change_rate, "volume": p.volume,
            "open": p.open_price, "high": p.high_price,
            "low": p.low_price, "prev_close": p.prev_close,
        }, ensure_ascii=False))
```

**사용 agent:** `trader` (Slack 메시지 현재가 기재), `technical` (장중 진입 시점 정밀화)

---

## Query 3 — 호가 창 (매수/매도 10단계)

```python
import sys
sys.path.insert(0, "/home/leehg/github/letsTrade/bot/src")

from lets_trade.api import LSApiClient, StockApi

with LSApiClient() as client:
    book = StockApi(client).get_orderbook("000660")

print("매도호가 (낮은순):", list(zip(book.ask_prices[:5], book.ask_volumes[:5])))
print("매수호가 (높은순):", list(zip(book.bid_prices[:5], book.bid_volumes[:5])))
```

**사용 agent:** `technical` (매수/매도벽 분석으로 진입 가격 정밀화)

---

## Query 4 — 당일 주문 내역

```python
import sys
sys.path.insert(0, "/home/leehg/github/letsTrade/bot/src")

from lets_trade.api import LSApiClient, OrderApi

with LSApiClient() as client:
    orders = OrderApi(client).get_orders()  # date="YYYYMMDD" 가능

for o in orders:
    print(f"[{o.order_time}] {o.side} {o.name}({o.symbol}) "
          f"주문{o.order_qty}주 / 체결{o.exec_qty}주 @{o.exec_price:,} — {o.status}")
```

**사용 agent:** `lets_manager` (오늘 이미 체결된 종목 파악)

---

## Agent별 사용 목적 요약

| Agent | Query | 목적 |
|-------|-------|------|
| `lets_manager` | Q1, Q4 | 현재 포지션 + 당일 체결 파악 |
| `fundamental` | Q1 | 보유 종목의 평균단가 vs 현재가 비교 |
| `technical` | Q2, Q3 | 현재가 + 호가로 진입 시점 정밀화 |
| `trader` | Q2 | Slack 메시지에 실제 현재가 기재 |
| `aggressive/neutral/conservative` | Q1 | `available` 기준 포지션 크기 계산 |

---

## 주의사항

- **주문 실행 금지** — 이 skill은 read-only 조회만 허용. 주문은 trader agent가 별도 승인 후 처리
- 장외 시간 호출 시 `get_price()` 결과는 전일 종가를 반환할 수 있음
- `LSApiClient`는 context manager(`with`)로 쓰는 것이 권장 (자동 토큰/연결 정리)
- 토큰은 자동 갱신됨 — 401 응답 시 `LSAuthClient`가 내부에서 재발급 처리
