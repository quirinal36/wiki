---
title: Vault 헬스체크 결과 (2026-06-25)
type: query
created: 2026-06-25
updated: 2026-06-25
tags: [meta, lint, maintenance]
status: active
---

# Vault 점검 결과 — 2026-06-25

전체 lint 실행 후 중복 통합까지 완료. wiki 노트 **100 → 67** (33개 삭제). 모든 변경은 git 추적 중이라 복구 가능.

## 긴급 수정 필요 (완료)

- **대량 중복 노트**: 같은 원본을 여러 번 요약한 노트 33개를 원본당 canonical 1개로 통합·삭제.
  - ChatGPT 교육 패러다임 (원본 1개 → 요약 9개) → `chatgpt-3.5-years-later` 유지
  - 린치핀·부족 전략 (요약 5개) → `linchpin-and-tribe-strategy` 유지
  - AI 생존전략(뇌과학), 학습자의 비밀, 컴활 자격증, 컴퓨터학과 조언, 코딩 교육 (각 3개) → 각 1개 유지
  - `vibecoding` → `vibe-coding`로 통합 (vibe-coding-education은 별도 개념이라 유지)
  - `lets-coding-and-play` 3개 → 1개 (수어번역 프로젝트 사실 병합), `seth-godin` 2개 → 1개
  - queries/ 한글 `*-summary` 7개 → summaries canonical로 통합
- **링크 재연결**: 삭제된 노트를 가리키던 17개 파일의 wikilink를 canonical로 갱신.
- **index 정합성**: "총 페이지 96" 표기가 실제와 불일치 → 67로 정정하고 한 줄 요약 전면 재생성.

## 정리 권장 (완료)

- **frontmatter 누락**: `hermes-control-interface-external-access.md`에 YAML frontmatter 추가.

## 참고 사항

- **깨진 링크**: 실제 깨진 wikilink 없음. `log.md`의 `[[concepts]]`/`[[entities]]` 2건은 과거 수정 내역을 서술한 텍스트라 오탐.
- **고립 노트**: 템플릿·시설관리·edudata 일부 노트가 링크 없이 존재. 성격상 독립 문서라 방치 가능.
- **SCHEMA.md 부재**: SOUL.md는 단일 `SCHEMA.md` 운영 규칙을 권장하나 현재 `schema/` 폴더(3개 파일)로 분산. 통합 검토 권장.

## 제안 작업 (미실행 — 추가 검토 필요)

- **운영 request 요약 중복**: agent-creation / letstrade / hermes-web-ui / claw-empire 등은 summaries와 queries에 유사 노트가 공존. 상호 링크가 많아 이번엔 보존. 다음 점검 때 통합 검토.
- **루트 정리**: `무제.canvas`, `블로그-업로드용-템플릿.md` 등 템플릿류를 `templates/` 폴더로 이동.
- **schema/ → SCHEMA.md 통합**.

관련 노트: [[index]], [[log]]
