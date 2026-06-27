---
title: Hermes Profile + Slack App 연동 설정 매뉴얼
created: 2026-06-10
updated: 2026-06-10
type: query
tags: ['tooling', 'workflow']
sources: []
---

# Hermes Profile + Slack App 연동 설정 매뉴얼

> 새로운 Hermes profile을 생성하고, Slack App을 만들어 해당 채널에서 멘션으로 대화할 수 있도록 연동하는 전체 절차.

---

## 1. Hermes Profile 생성

```bash
hermes profile create <프로필명>
```

생성된 프로필 경로: `~/.hermes/profiles/<프로필명>/`

> ⚠️ alias 이름이 시스템 명령(`/usr/bin/red` 등)과 충돌하면 `hermes profile alias`가 실패함.
> 이 경우 직접 wrapper 스크립트를 생성한다.

```bash
# ~/.local/bin/<alias명> 파일 생성
cat > ~/.local/bin/<alias명> << 'EOF'
#!/usr/bin/env bash
exec hermes --profile <프로필명> "$@"
EOF
chmod +x ~/.local/bin/<alias명>
```

---

## 2. Slack App 생성

1. https://api.slack.com/apps 접속 → **Create New App** → **From scratch**
2. App Name 입력 (예: `redi`), 워크스페이스 선택 → **Create App**

---

## 3. Socket Mode 활성화

**Settings → Socket Mode**
- Enable Socket Mode → **On**
- App-Level Token 생성:
  - Token Name 자유 입력
  - Scope: `connections:write` 추가
  - **Generate** → `xapp-1-...` 토큰 복사

---

## 4. Event Subscriptions 설정

**Features → Event Subscriptions**
- Enable Events → **On**
- **Subscribe to bot events** 에 추가:
  - `app_mention`
  - `message.channels`
  - `message.im` (DM 응답도 원한다면)

---

## 5. OAuth & Permissions 설정

**Features → OAuth & Permissions → Bot Token Scopes** 에 추가:

| Scope | 용도 |
|-------|------|
| `chat:write` | 메시지 전송 |
| `chat:write.public` | 초대 없이 공개 채널에 전송 |
| `channels:read` | 공개 채널 목록 조회 |
| `groups:read` | 프라이빗 채널 목록 조회 |
| `mpim:read` | 멀티파티 DM 조회 |
| `im:read` | 1:1 DM 조회 |
| `app_mentions:read` | 멘션 이벤트 수신 |

---

## 6. 워크스페이스에 App 설치

**Settings → Install App → Install to Workspace** → 허용

→ `xoxb-...` **Bot User OAuth Token** 복사

> ⚠️ Scope 변경 시마다 **Reinstall to Workspace** 필요. 토큰이 재발급될 수 있으므로 확인 후 `.env` 업데이트.

---

## 7. Profile .env 설정

```bash
# ~/.hermes/profiles/<프로필명>/.env
SLACK_BOT_TOKEN=xoxb-...        # Bot User OAuth Token
SLACK_APP_TOKEN=xapp-1-...      # App-Level Token (Socket Mode용)
SLACK_ALLOWED_USERS=U...        # 응답할 Slack User ID (쉼표 구분 가능)
SLACK_HOME_CHANNEL=C...         # 홈 채널 ID
```

> Slack User ID 확인: Slack에서 해당 사람 프로필 → **More** → **Copy member ID**
> 채널 ID 확인: 채널명 우클릭 → **View channel details** → 하단에 Channel ID

---

## 8. Profile config.yaml에 gateway port 설정

```bash
# ~/.hermes/profiles/<프로필명>/config.yaml 의 gateway 섹션에 추가
```

```yaml
gateway:
  api_server:
    enabled: true
    extra:
      host: 0.0.0.0
      port: <포트번호>   # 다른 프로필과 겹치지 않는 번호 사용
```

> 현재 사용 중인 포트 참고:
> - `default`: 8642
> - `gaia`: 8650
> - `redi`: 8644

---

## 9. Slack 채널에 App 초대

Slack 채널에서:
```
/invite @<앱이름>
```

---

## 10. Gateway 실행

```bash
# tmux로 백그라운드 실행 (권장)
tmux new-session -d -s <세션명>_gateway 'hermes --profile <프로필명> gateway run'

# 로그 확인
tail -f ~/.hermes/profiles/<프로필명>/logs/gateway.log

# 상태 확인
hermes --profile <프로필명> gateway status
```

---

## 11. 동작 확인

Slack 채널에서 `@<앱이름> 안녕` 멘션 → 응답 오면 완료 ✅

---

## 트러블슈팅

| 증상 | 원인 | 조치 |
|------|------|------|
| `missing_scope: connections:write` | App-Level Token에 스코프 없음 | App-Level Token 재생성 (scope: `connections:write`) |
| `missing_scope: groups:read` | Bot Token 스코프 부족 | OAuth & Permissions에 스코프 추가 후 Reinstall |
| 멘션해도 로그에 아무것도 안 찍힘 | Socket Mode 비활성 또는 Event Subscriptions 미설정 | Socket Mode ON, `app_mention` 이벤트 추가 후 Reinstall |
| `Channel directory built: 0 target(s)` | 채널 조회 스코프 부족 또는 채널 미초대 | `groups:read`, `mpim:read` 추가 + 채널에 `/invite` |
| gateway가 응답하지만 특정 유저 무시 | `SLACK_ALLOWED_USERS` 미설정 또는 User ID 불일치 | `.env`의 `SLACK_ALLOWED_USERS` 확인 |

---

## 관련 파일 경로

```
~/.hermes/profiles/<프로필명>/
├── config.yaml        # 모델, gateway port 등 설정
├── .env               # Slack 토큰, 채널 ID
└── logs/
    └── gateway.log    # 실시간 로그
~/.local/bin/<alias명> # alias wrapper 스크립트
```
