# Hermes Agent 멀티 프로필 Slack 연동 회의록

**날짜:** 2026년 6월 9일
**참여자:** U0ASMGY0E2Y (오퍼레이터), red (Hermes Agent / deepseek-v4-pro), orange (Hermes Agent / qwen3.7-plus)
**채널:** Slack `#redi-room` 스레드

---

## 안건: Hermes Agent 멀티 프로필 간 메시지 조회 가능성 검토

### 1. 현황 파악

- **red** (`U0B94CJJHHS`): deepseek/deepseek-v4-pro, Slack 게이트웨이 실행 중
- **orange**: qwen/qwen3.7-plus, Slack 게이트웨이 실행 중
- 두 프로필 모두 동일 Slack 워크스페이스에 연결된 상태
- `hermes profile list`로 확인 시 두 프로필 모두 gateway `running`

### 2. Slack 플랫폼 제약 확인

**핵심 발견:** Slack은 봇(bot) 간 메시지 전달을 원천 차단함

- Slack API 설계상 봇 메시지는 다른 봇에게 전달되지 않음 (무한 루프 방지)
- 각 Hermes 프로필은 별개의 Slack App/Bot으로 동작
- 따라서 red와 orange는 **Slack 실시간 메시지**를 서로 수신할 수 없음

### 3. 대체 조회 방법 발견

| 방법 | red → orange | orange → red |
|------|:---:|:---:|
| Slack 실시간 메시지 | ❌ | ❌ |
| `session_search(profile=...)` 크로스 조회 | ✅ | ✅ |
| API Server (red:8644, orange:8645) | 이론상 가능 | 이론상 가능 |

**세션 DB 크로스 조회**를 통해 상대 프로필의 전체 대화 기록을 읽을 수 있음을 실험으로 확인함.

### 4. orange 현재 작업 현황 (세션 조회 결과)

- **"클로드 코드 팀 협업 분석"**: maily.so 아티클(셀피쉬클럽 AAA팀)을 NotebookLM으로 분석 중. 오디오 생성 진행 중 (task_id: `c70e6a3b`)
- **"잭 도시 미니 AGI 실험"**: 이전에 완료된 NotebookLM 분석. 오디오 + Obsidian 아카이빙 완료
- **"NotebookLM-py: Reverse-Engineered API"**: 기술 세션

### 5. 향후 방안 논의

1. **단기**: `session_search`로 상대 프로필의 작업 상황을 비동기적으로 조회하는 패턴 확립
2. **중기**: Kanban 시스템으로 두 프로필 간 작업 분배 워크플로우 구축
   - 양쪽 모두 `kanban.dispatch_in_gateway: true` 설정 확인됨
   - 디스패처가 자동으로 태스크 분배 가능
3. **장기**: Slack 봇 간 실시간 소통이 필요하면 User Token(`xoxp-`) 기반 접근 검토

### 6. 결론

- **Slack 실시간 메시지 수신은 불가능** (Slack 플랫폼 제약)
- **세션 DB 크로스 조회는 가능** — 비동기 협업 패턴으로 활용 가능
- **이 스레드 내 모든 메시지는 동일 사용자(U0ASMGY0E2Y)가 발신**했으므로, red의 세션만으로도 스레드 전체 내용을 포함한 회의록 작성 가능

---

## 결정 사항

1. 두 프로필 간 협업은 `session_search` + `Kanban` 기반으로 진행
2. 실시간 상호 메시지 조회가 필요할 경우, Slack 대신 API Server 경유 통신 검토
3. 이 회의록은 Obsidian `wiki/summaries/` 디렉토리에 아카이빙

---
*작성: red (Hermes Agent), 2026-06-09*
