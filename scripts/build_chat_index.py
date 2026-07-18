# -*- coding: utf-8 -*-
"""위키 마크다운 → api/wiki_index.json 채팅 검색 인덱스 생성.

Vercel 서버리스 함수(api/chat.py)는 배포 시 위키 원본에 접근하는 대신
이 스크립트가 만든 인덱스를 읽는다. Vercel buildCommand 와 로컬에서
모두 실행 가능. 표준 라이브러리만 사용.

실행: python scripts/build_chat_index.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "api", "wiki_index.json")

SKIP_DIRS = {"site", ".git", ".obsidian", ".archive", "_archive", ".backup",
             ".claude", "templates", "__pycache__", "media", "api", "scripts",
             "node_modules"}
MAX_DOC_CHARS = 2500  # 문서당 저장 길이 (컨텍스트 주입 상한과 동일)


def doc_url(rel):
    rel = rel[:-3]
    if rel == "index":
        return "/"
    if rel.endswith("/index"):
        rel = rel[:-6]
    return "/" + rel + "/"


def main():
    docs = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md") or name in ("chat.md", "graph.md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            try:
                text = open(path, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
            title = m.group(1).strip() if m else os.path.splitext(name)[0]
            docs.append({
                "rel": rel,
                "title": title,
                "url": doc_url(rel),
                "text": text[:MAX_DOC_CHARS],
            })
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False)
    print(f"wiki_index.json: {len(docs)} docs, {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
