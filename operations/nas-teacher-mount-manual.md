# NAS Teacher 마운트 매뉴얼

NAS(`192.168.0.4`)의 `teacher` 공유 폴더를 WSL의 `~/nas/teacher`에 마운트하는 전체 과정.

## 환경 정보

| 항목 | 값 |
|------|-----|
| NAS IP | `192.168.0.4` |
| NAS 사용자 | `leehg` |
| SSH 포트 (shell) | `2002` |
| SFTP 포트 (sshfs용) | `22` |
| WSL 마운트 포인트 | `~/nas/teacher` |
| SSH 키 | `~/.ssh/wsl_test_id_ed25519` |

> NFS는 이 NAS에서 비활성화되어 있어 SSHFS 방식을 사용한다.

---

## 1단계: 네트워크 연결 확인

```bash
ping -c 3 192.168.0.4
```

---

## 2단계: SSH 접속 확인

```bash
ssh -p 2002 leehg@192.168.0.4 'echo ok'
```

---

## 3단계: SSH 키 등록 (최초 1회)

SSH 키가 NAS에 등록되지 않으면 자동 마운트 스크립트가 실패한다.

### 3-1. 퍼블릭 키 확인

```bash
cat ~/.ssh/wsl_test_id_ed25519.pub
```

### 3-2. NAS에 로그인하여 키 등록

```bash
ssh -p 2002 leehg@192.168.0.4
```

NAS 셸에서:

```bash
mkdir -p ~/.ssh
echo "여기에 퍼블릭 키 내용 붙여넣기" >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
exit
```

### 3-3. 키 인증 동작 확인

```bash
ssh -i ~/.ssh/wsl_test_id_ed25519 -p 2002 leehg@192.168.0.4 'echo 키인증 성공'
```

---

## 4단계: 수동 마운트

```bash
mkdir -p ~/nas/teacher
sshfs -p 22 leehg@192.168.0.4:teacher ~/nas/teacher
```

마운트 확인:

```bash
ls ~/nas/teacher
df -h ~/nas/teacher
```

---

## 5단계: 자동 마운트 설정 확인

자동 마운트는 systemd user 서비스로 구성되어 있다.

- 스크립트: `~/.local/bin/mount-nas-teacher.sh`
- 서비스: `~/.config/systemd/user/nas-teacher-mount.service`

### 서비스 상태 확인

```bash
systemctl --user status nas-teacher-mount.service
```

### 서비스 수동 실행 (테스트)

```bash
# 기존 마운트 해제 후 스크립트 직접 실행
fusermount -u ~/nas/teacher 2>/dev/null; true
bash ~/.local/bin/mount-nas-teacher.sh && echo "성공"
```

### 서비스 재시작

```bash
systemctl --user restart nas-teacher-mount.service
systemctl --user status nas-teacher-mount.service
```

---

## 마운트 해제

```bash
fusermount -u ~/nas/teacher
```

---

## 트러블슈팅

### "Transport endpoint is not connected"

이전 마운트가 오류 상태로 남아 있을 때 발생.

```bash
fusermount -u ~/nas/teacher 2>/dev/null; true
sshfs -p 22 leehg@192.168.0.4:teacher ~/nas/teacher
```

### "bad option" / nfs 관련 오류

NFS가 NAS에서 비활성화 상태. SSHFS 방식(위 4단계)을 사용해야 한다.

### "RPC: Unable to receive"

`showmount` 명령이 실패하는 경우로, NFS 미지원을 의미. 동일하게 SSHFS를 사용.

### 자동 마운트 서비스가 실패하는 경우

SSH 키가 NAS에 등록되지 않은 것이 주원인. 3단계(SSH 키 등록)를 다시 수행.

서비스 로그 확인:

```bash
journalctl --user -u nas-teacher-mount.service -n 30
```

### 절대 경로로 SSHFS 연결 시 실패

Synology의 SFTP 루트와 shell 루트가 다르기 때문에 절대 경로(`/volume1/teacher`)가 동작하지 않을 수 있다. 반드시 상대 경로(`teacher`)를 사용.

---

## 부팅 후 자동 마운트 동작 구조

```
WSL 부팅
  └─ systemd user 데몬 시작 (Linger=yes로 로그인 없이도 동작)
       └─ network-online.target 충족
            └─ nas-teacher-mount.service 실행
                 └─ mount-nas-teacher.sh → sshfs 마운트
```

관련 파일:
- `~/.config/systemd/user/nas-teacher-mount.service`
- `~/.local/bin/mount-nas-teacher.sh`
