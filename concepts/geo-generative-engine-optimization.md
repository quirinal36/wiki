---
title: GEO (Generative Engine Optimization)
created: 2026-07-18
updated: 2026-07-18
type: concept
tags: [ai-business, product, marketing, llm, geo]
sources:
  - ~/Documents/workspace/agentree-home (SEO/GEO 구현 코드·커밋, 2026-07-18)
aliases: [AIEO, 생성형 엔진 최적화, AI 검색 최적화]
---

# GEO (Generative Engine Optimization)

## 정의
검색엔진(SEO)이 아니라 **생성형 AI 답변엔진**(ChatGPT, Perplexity, AI Overviews 등)에 자신의 콘텐츠가 인용·추천되도록 최적화하는 작업. AIEO(AI Engine Optimization)로도 불린다. "구글에서 상위 노출"이 아니라 "AI의 답변 안에 등장"이 목표다.

## 왜 중요한가
- 검색 트래픽이 AI 답변으로 이동하면서 전통 SEO만으로는 발견되지 않는 영역이 커지고 있다.
- AI가 크롤링·인용하기 좋은 구조(명시적 허용, 기계가독 요약, 구조화 데이터)는 별도의 설계가 필요하다.
- 지역·니치 사업자에게는 "AI에게 추천받는 업체"가 새로운 진입 기회다.

## 실전 체크리스트 — agentree-home 구현 사례
[[projects/agentree-home/overview|agentree-home]]에 실제 적용된 GEO 스택:
- `llms.txt` / `llms-full.txt` — AI가 읽을 사이트 요약 제공
- `robots.ts`에서 AI 크롤러(GPTBot 등) **명시 허용**
- JSON-LD 구조화 데이터 (ProfessionalService 스키마)
- sitemap·canonical·RSS 피드 정비
- IndexNow 제출 스크립트 (`scripts/submit-indexnow.mjs`) + SEO 감사 스크립트
- 서비스별·지역별(전주·전북) SEO 랜딩 페이지 (`app/[slug]`)
- 동적 OG 이미지 — 공유 시점의 정보 최신성 유지

## 서비스로서의 GEO
[[entities/agentree|Agentree]]는 GEO를 자사 사이트에 적용할 뿐 아니라 **서비스 필러**로도 판매한다 — Perplexity식 답변 목업 섹션, CEP(Category Entry Point) 발굴 등이 랜딩에 포함돼 있다.

## Open Questions
- GEO 효과 측정 방법: AI 답변 인용 여부를 어떻게 추적·정량화할 것인가?
- llms.txt 표준의 실제 채택률 — 주요 AI 크롤러가 얼마나 존중하는가?

## 관련 페이지
- [[entities/agentree|Agentree (에이전트리)]] — GEO를 서비스로 제공
- [[projects/agentree-home/overview|agentree-home 저장소 개요]] — 구현 코드
- [[projects/agentree-home/development-history|개발 히스토리]] — 7월 초 "SEO/GEO 총력전" 단계
