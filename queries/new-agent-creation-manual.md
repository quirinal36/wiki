---
title: 새 Agent 생성 매뉴얼
created: 2026-04-23
updated: 2026-04-27
type: query
tags: [ai-agents, workflow, tooling, automation]
sources:
  - raw/notes/2026-04-23-agent-creation-manual-request.md
aliases: [new agent creation manual, agent creation manual, 새 에이전트 생성 매뉴얼]
status: active
---

> Source note: `raw/notes/2026-04-23-agent-creation-manual-request.md`

# 새 Agent 생성 매뉴얼

## User question
앞으로 agent 를 새로 만들고 싶을 때 따라 할 수 있는 manual

## Short answer
Hermes에서 새 agent를 만든다는 것은 보통 새 profile을 분리하고, 그 profile 전용 설정(.env, config.yaml, gateway service, home channel, allowlist)을 정리한 뒤, 독립적으로 시작/검증하는 절차를 뜻한다.

## Manual

### 1) 새 agent의 역할부터 정한다
- 무엇을 맡길지 정한다.
- 대화 채널은 Slack인지, Telegram도 필요한지 정한다.
- 기존 `hermes-gateway.service`와 `hermes-gateway-trader.service`를 건드리지 않을지 정한다.
- 이 agent가 기존 agent와 같은 엔진인지, 완전히 별도 운영인지 정한다.

### 2) profile 이름을 정한다
- 새 agent는 보통 `~/.hermes/profiles/<profile-name>/` 형태로 분리한다.
- 이름은 짧고 안정적으로 정한다.
- 예: `gaia`, `news`, `labs`

### 3) 기존 프로필을 기준점으로 복사하거나 초기화한다
- 새 profile 디렉터리를 만든다.
- 필요한 경우 기존 profile의 설정을 참고해 `config.yaml`과 `.env`를 채운다.
- 비밀값은 새로 넣고, 기존 토큰을 그대로 복붙한 뒤 혼용하지 않는다.

### 4) 메시징 설정을 독립시킨다
- 어떤 플랫폼을 쓸지 정한다.
- Slack만 쓸 거면 Telegram 관련 값은 비활성화한다.
- 새 agent의 홈 채널을 명시한다.
  - 예: `SLACK_HOME_CHANNEL=C01234567890`
  - 예: `SLACK_HOME_CHANNEL_NAME=current-thread-channel`
- allowed users도 profile별로 분리한다.

### 5) gateway를 profile 단위로 설치한다
- 새 agent는 전용 gateway service로 띄우는 것이 안전하다.
- 기존 서비스는 끄지 않는다.
- profile 전용 service가 생성되면, 그 service가 해당 profile의 `.env`와 상태 파일을 읽는지 확인한다.

### 6) 상태 충돌이 없는지 점검한다
- stale PID/state 파일이 남아 있으면 정리한다.
- 새 agent가 이전 agent의 홈 채널이나 락 파일을 잘못 물고 있지 않은지 확인한다.
- 시작이 안 되면 `gateway_state.json`, `gateway.pid`, `channel_directory.json`을 순서대로 의심한다.

### 7) 실제 연결을 확인한다
- `hermes --profile <name> status --all`
- `hermes --profile <name> gateway status`
- `send_message(action='list')`
- 테스트 메시지 1회 전송
- Slack이면 실제 channel ID와 thread ID가 맞는지 확인

### 8) 운영용 체크리스트를 남긴다
- profile 이름
- 홈 채널 ID
- 허용 사용자 ID
- 사용 플랫폼
- 어떤 서비스가 이 profile을 담당하는지
- 테스트 성공 여부

## Troubleshooting

### 채널은 맞는데 send_message가 실패할 때
- 현재 running service가 같은 `.env`를 읽는지 확인한다.
- 전역 `.env`와 profile `.env`가 서로 다른 홈 채널을 가리키는지 확인한다.
- `channel_directory.json`이 옛 스레드 정보만 들고 있지 않은지 확인한다.
- gateway를 재시작한 뒤 다시 `send_message(action='list')`를 확인한다.

### Slack 홈 채널이 바뀌지 않을 때
- profile `.env`의 `SLACK_HOME_CHANNEL`을 확인한다.
- 서비스 재시작 후 런타임 환경이 실제로 반영됐는지 확인한다.
- 전역 `.env`가 같은 키를 다른 값으로 덮고 있지 않은지 확인한다.

### 새 agent를 만들 때 제일 중요한 원칙
- 새 agent는 “새 폴더”보다 “새 운영 경계”에 가깝다.
- 설정, 채널, allowlist, service, state 파일을 분리해야 나중에 꼬이지 않는다.

## Supporting wiki pages
- [[hermes-agent]]
- [[trader-agent]]
- [[obsidian-workflow]]
- [[llm-wiki]]
- [[long-term-vault-operating-policy]]
