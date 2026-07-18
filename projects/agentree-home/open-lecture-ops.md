---
title: Agentree 오픈강의 운영 시스템
created: 2026-07-18
updated: 2026-07-18
type: project
tags: [ai-business, automation, workflow, education, supabase]
sources:
  - ~/Documents/workspace/agentree-home (app/open*, lib/, git history, 2026-07-18)
---

# Agentree 오픈강의 운영 시스템

[[entities/agentree|Agentree]]가 오픈강의를 신청부터 출석·안내까지 자체 홈페이지 안에서 운영하는 시스템. [[projects/agentree-home/overview|agentree-home]] 저장소에 구현돼 있다.

## 2026-07-20 회차 (직전 회차 기준)
- 일시: 2026-07-20(월) 16:00~18:00 · 장소: 전북테크비즈센터 1층 대강당
- 정원: 100명 → 120명 상향 (신청 진행바 실시간 반영)
- 세션 구성: 세션 1 "AI Agent evolution" (v7.2 덱) + 세션 2 AX 사례·데모 덱 — [[entities/hermes-agent|Hermes Agent]] 데모 영상, NemoClaw 에필로그 포함
- 슬라이드 원본은 `hyperframes-hermes-sales/slides/`, 빌드 시 `public/slides/`로 동기화

## 기능 구성 요소
| 기능 | 위치 | 설명 |
|---|---|---|
| 신청 랜딩 + 인라인 폼 | `/open` + `api/registrations` | Supabase 적재, 동적 OG 이미지 |
| 출석 설문 | `/open/attendance` | 응답 제출 후에만 행사 안내(주차 지도 등) 공개 |
| 신청 현황 | `/open-status` | 상태 필터·정렬·편집, 불참 응답 필터 |
| 메시지 센터 | `/open-messages` | 참가자 대상 안내 메시지 |
| 관리자 대시보드 | `/admin` | 신청·문의 리드 통합 관리 (RLS 마이그레이션 적용) |
| 문자 알림 | `lib/server/solapi.ts`, `notify.ts` | Solapi로 신청·문의 시 관리자 알림 |

## 재사용 가치
소규모 행사 운영에 필요한 "신청 → 알림 → 출석 → 사후 안내" 루프를 외부 폼 도구 없이 자체 스택(Next.js + Supabase + Solapi)으로 완결한 사례. 다음 행사나 유사 프로젝트에서 그대로 복제 가능한 패턴이다.

## 관련 페이지
- [[entities/agentree|Agentree (에이전트리)]]
- [[projects/agentree-home/overview|저장소 개요]]
- [[projects/agentree-home/development-history|개발 히스토리]] — 날짜 연기 이력, D-day 커밋 급증
