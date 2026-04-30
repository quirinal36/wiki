---
title: NAS teacher bind persistence
created: 2026-04-23
updated: 2026-04-23
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
```

## Notes
- This page is a living operational record, not a fixed spec.
- If the NAS layout changes, update the paths and commands here.
- If a cleaner persistent mechanism is found later, migrate the procedure and keep this page as history.
