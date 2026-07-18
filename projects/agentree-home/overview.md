---
title: agentree-home 저장소 개요
created: 2026-07-18
updated: 2026-07-18
type: project
tags: [ai-business, product, nextjs, supabase, workflow]
sources:
  - ~/Documents/workspace/agentree-home (저장소 구조 분석, 2026-07-18)
---

# agentree-home 저장소 개요

[[entities/agentree|Agentree]]의 공식 홈페이지(agentree.kr) 코드베이스. 회사 소개 사이트로 출발해 커뮤니티·오픈강의 운영 플랫폼으로 확장됐다.

## 기본 정보
- 로컬 경로: `~/Documents/workspace/agentree-home`
- 원격: `github.com/foresightvalue-create/agentree-home` · 배포: Vercel
- 스택: **Next.js 16.2.4 (App Router) + React 19 + Tailwind 4 + framer-motion + Supabase**

## 디렉토리 지도
| 경로 | 역할 |
|---|---|
| `app/` | 페이지·API. 랜딩, about, agents, lecture, community, open*, admin, `[slug]`(SEO 랜딩) |
| `app/api/` | community posts/comments, contacts, registrations, open-attendance/messages/status |
| `components/` | 랜딩 섹션 컴포넌트 (Hero, PainPoints, Consulting, Education, Contact 등) |
| `lib/` | Supabase 클라이언트(클라이언트/서버 admin 분리), Solapi 문자 알림(`server/solapi.ts`, `notify.ts`) |
| `supabase/` | community 스키마 + 마이그레이션 2개 (community_schema, admin_rls) |
| `scripts/` | `sync-slides.mjs`, `pull-drive-assets.mjs`, `seo-audit.mjs`, `submit-indexnow.mjs` |
| `hyperframes-hermes-sales/` | 강의 슬라이드 **원본** (HyperFrames 컴포지션, 세션 1·2 덱, 데모 영상) |
| `public/slides/` | 위 슬라이드의 **동기화 결과물** (dev/build 전 자동 복사) |
| `tests/` | open-messages·open-status 노드 테스트 (`npm test`) |

## 기능 축 3개
1. **회사 홈페이지** — B2B 랜딩 + `[slug]` 서비스별 SEO 페이지 (`app/seo.ts`에 정의)
2. **커뮤니티** — Supabase 게시판 + 가입(/join) + 관리자(/admin)
3. **오픈강의 운영** — 신청·출석·현황·메시지 → [[projects/agentree-home/open-lecture-ops|오픈강의 운영 시스템]]

## 작업 시 주의사항
- `CLAUDE.md` → `AGENTS.md`: "이 Next.js는 학습 데이터와 다르다. `node_modules/next/dist/docs/` 문서를 먼저 읽어라"
- `npm run dev`/`build` 앞에 `sync-slides`가 자동 실행됨 — `public/slides/`를 직접 수정하지 말 것 (원본은 `hyperframes-hermes-sales/slides/`)
- `.env`에 Supabase·Solapi 실키 존재 — 취급 주의
- SEO/GEO 장치가 사이트 전반에 깔려 있음 → [[concepts/geo-generative-engine-optimization|GEO]]

## 관련 페이지
- [[entities/agentree|Agentree (에이전트리)]]
- [[projects/agentree-home/development-history|개발 히스토리 (5단계 전개)]]
- [[projects/agentree-home/open-lecture-ops|오픈강의 운영 시스템]]
- [[entities/hermes-agent|Hermes Agent]] — 강의 슬라이드의 주제
