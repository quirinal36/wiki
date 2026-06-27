# Hermes Control Interface — 외부 네트워크 접속 설정

## 목표

`hermes-control-interface` 웹 서비스를 외부 네트워크에서 아래 주소로 접속 가능하게 설정.

```
http://turboguy36.iptime.org:8790
```

---

## 1. 프로젝트 환경변수 설정 (`.env`)

파일 경로: `/home/leehg/github/hermes-control-interface/.env`

### 변경 내용

| 항목 | 변경 전 | 변경 후 | 설명 |
|------|---------|---------|------|
| `PORT` | `10272` (기본값) | `8790` | 서비스 포트 변경 |
| `HOST` | `127.0.0.1` (기본값) | `0.0.0.0` | 모든 네트워크 인터페이스에서 수신 |
| `HCI_CORS_ORIGINS` | (미설정) | `http://turboguy36.iptime.org:8790` | 외부 도메인 CORS 허용 |

### 최종 `.env` 주요 설정

```env
# 포트
PORT=8790

# 호스트 (모든 인터페이스에서 수신)
HOST=0.0.0.0

# CORS 허용 도메인
HCI_CORS_ORIGINS=http://turboguy36.iptime.org:8790
```

---

## 2. 서버 바인딩 동작 원리

`server.js` 내부에서 아래와 같이 HOST 환경변수를 읽어 바인딩합니다.

```js
// server.js:4727
app.listen(PORT, process.env.HOST || '127.0.0.1', () => { ... });
```

- `HOST` 미설정 시: `127.0.0.1` → 루프백만 수신 (외부 접속 불가)
- `HOST=0.0.0.0` 설정 시: 모든 인터페이스에서 수신 (외부 접속 가능)

---

## 3. 서버 시작

```bash
cd /home/leehg/github/hermes-control-interface
node server.js
```

또는 백그라운드 실행:

```bash
nohup node server.js &>/tmp/hci.log &
```

---

## 4. WSL2 포트 노출 (Windows 필수 작업)

WSL2는 별도의 가상 네트워크에 있으므로, Windows에서 포트를 외부로 노출시키는 설정이 필요합니다.

### 4-1. WSL2 내부 IP 확인

WSL2 터미널에서:

```bash
hostname -I
# 예: 172.22.150.123
```

### 4-2. Windows 포트 프록시 설정

**Windows PowerShell (관리자 권한)**으로 실행:

```powershell
# WSL2 IP 확인
$wslIp = (wsl hostname -I).Trim()

# 포트 프록시 추가 (외부 8790 → WSL2 8790)
netsh interface portproxy add v4tov4 `
  listenport=8790 `
  listenaddress=0.0.0.0 `
  connectport=8790 `
  connectaddress=$wslIp
```

설정 확인:

```powershell
netsh interface portproxy show all
```

설정 삭제(필요 시):

```powershell
netsh interface portproxy delete v4tov4 listenport=8790 listenaddress=0.0.0.0
```

### 4-3. Windows 방화벽 규칙 추가

```powershell
New-NetFirewallRule `
  -DisplayName "HCI Port 8790" `
  -Direction Inbound `
  -Protocol TCP `
  -LocalPort 8790 `
  -Action Allow
```

---

## 5. ipTIME 공유기 포트포워딩

ipTIME 관리 페이지 (`http://192.168.0.1`) 에서:

1. **메뉴**: 고급 설정 → NAT/라우터 관리 → 포트포워드 설정
2. **규칙 추가**:

| 항목 | 값 |
|------|-----|
| 규칙 이름 | HCI-8790 |
| 내부 IP | Windows 호스트 IP (예: 192.168.0.xxx) |
| 외부 포트 | 8790 |
| 내부 포트 | 8790 |
| 프로토콜 | TCP |

---

## 6. 접속 확인

설정 완료 후 외부 네트워크(모바일 데이터 등)에서 접속:

```
http://turboguy36.iptime.org:8790
```

---

## 참고

- DDNS 도메인: `turboguy36.iptime.org` (ipTIME DDNS)
- 서비스 기본 포트: `10272` → 변경 후: `8790`
- 프로젝트 경로: `/home/leehg/github/hermes-control-interface`
