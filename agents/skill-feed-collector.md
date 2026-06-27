---
title: Skill — feed-collector
created: 2026-04-27
updated: 2026-04-27
type: operation
tags: [skill, hermes, supabase, news, rss, stocks, korean-market, trending]
sources: []
aliases: [feed-collector skill, FeedCollector skill, news skill]
status: active
---

# Skill: feed-collector

## 목적

RSS 피드를 수집해 Supabase에 저장하는 FeedCollector 프로젝트의 데이터를 **web search 없이** 직접 쿼리한다.
뉴스 기사, 트렌딩 스코어, 종목 매칭(ticker → 기사) 데이터를 제공한다.

## 파일 위치

```
/home/leehg/github/Agents/skills/feed-collector/SKILL.md
```

## 데이터 소스

| 테이블 | 내용 |
|--------|------|
| `articles` | 기사 제목, 요약, URL, 발행일, 카테고리 |
| `article_stats` | 트렌딩 스코어, 언급 횟수 |
| `article_mentions` | 기사 ↔ 종목코드(ticker) 매핑 |
| `stock_daily` | 종목 일별 종가, 등락률 |

- **Supabase URL:** `https://wtdqqrjzsrtjtjtldjzu.supabase.co`
- **수집 주기:** 8시간마다 자동 실행 (collector agent)
- **프로젝트 위치:** `/home/leehg/github/FeedCollector`

---

## Query 1 — 최근 기사 조회 (query_news.py)

```python
import subprocess, json

result = subprocess.run(
    ["python", "/home/leehg/github/FeedCollector/query_news.py"],
    capture_output=True, text=True,
    cwd="/home/leehg/github/FeedCollector"
)
data = json.loads(result.stdout)
articles = data["articles"]
print(f"총 {data['count']}건")
```

반환 필드: `id`, `title`, `summary`, `url`, `published_at`, `category_id`

**사용 agent:** `news` (최근 12h 기사 수집, 매크로 이슈 파악)

---

## Query 2 — 트렌딩 기사 + 종목 매칭

```python
import os, json
from supabase import create_client

url = "https://wtdqqrjzsrtjtjtldjzu.supabase.co"
key = os.getenv("SUPABASE_ANON_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind0ZHFxcmp6c3J0anRqdGxkanp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI1NzI0NzEsImV4cCI6MTg5MDMzODQ3MX0.eJg2eFVbKHYfKvE2_uw-JF1-zC4t5vBJfHDh28hvF8")
sb = create_client(url, key)

# 1. 트렌딩 스코어 상위 기사
stats = sb.table("article_stats").select("article_id,trending_score,mention_count") \
    .order("trending_score", desc=True).limit(10).execute().data

article_ids = [s["article_id"] for s in stats]

# 2. 기사 제목/요약
articles = sb.table("articles").select("id,title,summary,url,published_at") \
    .in_("id", article_ids).execute().data
articles_map = {a["id"]: a for a in articles}

# 3. 매칭된 종목
mentions = sb.table("article_mentions").select("article_id,ticker,company_name") \
    .in_("article_id", article_ids).execute().data

# 4. 종목별 최신 주가
tickers = list({m["ticker"] for m in mentions})
stocks = {}
if tickers:
    stock_data = sb.table("stock_daily").select("ticker,date,close,change_rate,company_name") \
        .in_("ticker", tickers).order("date", desc=True).limit(len(tickers) * 2).execute().data
    for s in stock_data:
        if s["ticker"] not in stocks:
            stocks[s["ticker"]] = s

# 결과 조합
results = []
for art_id in article_ids:
    art = articles_map.get(art_id, {})
    art_mentions = [m for m in mentions if m["article_id"] == art_id]
    results.append({
        "title": art.get("title"),
        "published_at": art.get("published_at"),
        "trending_score": next((s["trending_score"] for s in stats if s["article_id"] == art_id), 0),
        "matched_stocks": [
            {
                "ticker": m["ticker"],
                "company": m.get("company_name"),
                "change_rate": stocks.get(m["ticker"], {}).get("change_rate"),
                "close": stocks.get(m["ticker"], {}).get("close"),
            }
            for m in art_mentions
        ]
    })

print(json.dumps(results, ensure_ascii=False, indent=2))
```

반환 예시:
```json
[
  {
    "title": "SK하이닉스, HBM4 양산 시작...",
    "trending_score": 87.3,
    "matched_stocks": [
      { "ticker": "000660", "company": "SK하이닉스", "change_rate": 2.4, "close": 198000 }
    ]
  }
]
```

**사용 agent:** `sector` (trending 종목 파악 → 티커 후보 도출)

---

## Query 3 — 특정 종목 언급 기사 조회

```python
import os
from supabase import create_client

url = "https://wtdqqrjzsrtjtjtldjzu.supabase.co"
key = os.getenv("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
sb = create_client(url, key)

ticker = "000660"  # 조회할 종목코드

mentions = sb.table("article_mentions").select("article_id,ticker,company_name") \
    .eq("ticker", ticker).execute().data
article_ids = [m["article_id"] for m in mentions]

if article_ids:
    articles = sb.table("articles").select("title,summary,url,published_at") \
        .in_("id", article_ids).order("published_at", desc=True).limit(5).execute().data
    for a in articles:
        print(f"[{a['published_at'][:10]}] {a['title']}")
```

**사용 agent:** `fundamental` (특정 종목 관련 최신 뉴스 확인)

---

## 의존성

```bash
pip install supabase
```

## 주의사항

- **읽기 전용** — 기사 저장/수정은 수행하지 않음
- collector agent가 최소 8시간 이내 실행된 경우에만 최신 데이터 보장
- `SUPABASE_ANON_KEY` 환경변수 없으면 하드코딩된 anon key 사용 (공개 읽기 권한)
