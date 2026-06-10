---
title: NAS teacher bind persistence
created: 2026-04-23
updated: 2026-05-01
type: operation
tags: [nas, synology, sshfs, sftp, bind-mount, setup, persistence]
sources: []
aliases: [teacher bind persistence, NAS teacher mount persistence, Synology teacher bind]
status: active
---

# NAS teacher bind persistence

## Purpose
Record the NAS/WSL setup that makes the Synology `teacher` directory available consistently after reboot.

## Context
- NAS host: `192.168.0.4`
- SSH port used for admin access: `2002`
- WSL-side mount point: `~/nas/teacher`
- NAS source path: `/volume1/teacher`
- NAS home path used for the shared view: `/var/services/homes/leehg/teacher`

## What was verified
- SSH shell access to the NAS works.
- SFTP access on port `22` works.
- `teacher` exists on the NAS at `/volume1/teacher`.
- The NAS-side home path `/var/services/homes/leehg/teacher` exists.
- WSL can mount the NAS view at `/home/leehg/nas/teacher`.

## Persistence approach
A boot script was created on the NAS:
- `/usr/local/etc/rc.d/S99teacher-bind.sh`

The script is intended to re-establish the bind-style exposure after reboot.

Important separation:
- NAS-side bind mount exposes `/volume1/teacher` inside the NAS namespace.
- WSL-side mount must still attach that NAS export again after reboot.
- So a working NAS script alone does not make `/home/leehg/nas/teacher` persist in WSL.

## Why the mount probably fails after reboot
Most likely causes:
1. The WSL mount is not configured to auto-run on startup.
2. SSHFS login is not passwordless, so boot-time mount cannot authenticate.
3. The remote path is wrong for SFTP/SSHFS namespace visibility.
   - Try the SFTP-visible path first, often `teacher` or a home-relative path.
   - If `/volume1/teacher` is not visible over SSHFS, use the NAS-side bind target instead.

## Recommended WSL-side autostart
If SSHFS is the chosen transport, create a systemd user service or fstab entry in WSL that mounts to:
- `/home/leehg/nas/teacher`

Example fstab pattern (adjust the remote path after confirming what SFTP can see):
```fstab
leehg@192.168.0.4:teacher  /home/leehg/nas/teacher  fuse.sshfs  _netdev,reconnect,ServerAliveInterval=15,ServerAliveCountMax=3,IdentityFile=/home/leehg/.ssh/id_ed25519,allow_other  0  0
```

If `teacher` is not visible over SFTP, try a different remote path that matches the NAS-side bind exposure.

## NAS-side verification commands
Use SSH on port `2002` and run:

```bash
grep "teacher" /proc/mounts
ls -ld /var/services/homes/leehg/teacher
findmnt -T /var/services/homes/leehg/teacher
```

## WSL-side verification commands
```bash
ls -ld /home/leehg/nas/teacher
findmnt /home/leehg/nas/teacher
mount | grep '/home/leehg/nas/teacher'
```

## Notes
- This page is a living operational record, not a fixed spec.
- If the NAS layout changes, update the paths and commands here.
- If a cleaner persistent mechanism is found later, migrate the procedure and keep this page as history.
- Current local test result: `ssh -i /home/leehg/.ssh/wsl_test_id_ed25519` is not yet accepted by the NAS on either port `22` or `2002` (`Permission denied (publickey,password)`).
- That means the WSL autostart service is written and enabled, but the NAS auth layer still has to be fixed before the mount can succeed automatically.
