# -*- coding: utf-8 -*-
"""Vercel 서버리스 함수: POST /api/chat

wiki_index.json(빌드 시 생성)에서 관련 문서를 검색해 컨텍스트로 붙이고
OpenRouter 에 질의한다. API 키는 Vercel 환경변수 OPENROUTER_API_KEY 로
주입된다 — 코드·저장소에는 키가 없다. 표준 라이브러리만 사용.
"""
import json
import os
import re
import urllib.request
from http.server import BaseHTTPRequestHandler

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = os.environ.get("CHAT_MODEL", "anthropic/claude-haiku-4.5")
MAX_DOCS = 6
MAX_DOC_CHARS = 2500

_INDEX_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiki_index.json")
with open(_INDEX_PATH, encoding="utf-8") as _f:
    WIKI = json.load(_f)

_PARTICLES = ("은", "는", "이", "가", "을", "를", "의", "에", "에서", "으로", "로",
              "와", "과", "도", "만", "야", "이야", "부터", "까지", "처럼", "보다")


def tokenize(s):
    tokens = set()
    for t in re.findall(r"[a-z0-9]+|[가-힣]+", s.lower()):
        if len(t) >= 2:
            tokens.add(t)
        if re.match(r"[가-힣]", t):
            for p in sorted(_PARTICLES, key=len, reverse=True):
                if t.endswith(p) and len(t) - len(p) >= 2:
                    tokens.add(t[: len(t) - len(p)])
                    break
    return list(tokens)


def retrieve(query, k=MAX_DOCS):
    terms = tokenize(query)
    if not terms:
        return []
    scored = []
    for d in WIKI:
        low = d["text"].lower()
        title_low = d["title"].lower()
        score = 0.0
        for t in terms:
            hits = low.count(t)
            if hits:
                score += 1.0 + min(hits, 10) * 0.3
            if t in title_low:
                score += 5.0
        if score > 0:
            scored.append((score, d))
    scored.sort(key=lambda x: -x[0])
    return [d for _, d in scored[:k]]


def build_system_prompt(context_docs):
    parts = [
        "당신은 사용자의 개인 지식 위키를 안내하는 한국어 어시스턴트입니다.",
        "아래 위키 발췌를 근거로 답하세요. 발췌에 없는 내용은 일반 지식으로 보완하되, "
        "위키 근거와 일반 지식을 구분해 말하세요. 근거 문서는 제목으로 언급하세요.",
        "",
    ]
    for d in context_docs:
        parts.append(f"=== [{d['title']}] ({d['rel']}) ===")
        parts.append(d["text"][:MAX_DOC_CHARS])
        parts.append("")
    return "\n".join(parts)


def call_openrouter(messages, api_key):
    payload = json.dumps({"model": MODEL, "messages": messages}).encode("utf-8")
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-Title": "Wiki Chat",
        },
    )
    with urllib.request.urlopen(req, timeout=55) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, {"ok": True, "docs": len(WIKI), "model": MODEL})

    def do_POST(self):
        api_key = os.environ.get("OPENROUTER_API_KEY", "")
        if not api_key:
            self._send(500, {"error": "OPENROUTER_API_KEY 환경변수가 설정되지 않았습니다. "
                                      "Vercel 프로젝트 Settings → Environment Variables 에 추가해주세요."})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            messages = body.get("messages", [])
            last_user = next((m["content"] for m in reversed(messages)
                              if m.get("role") == "user"), "")
            context_docs = retrieve(last_user)
            system = {"role": "system", "content": build_system_prompt(context_docs)}
            reply = call_openrouter([system] + messages[-10:], api_key)
            sources = [{"title": d["title"], "url": d["url"]} for d in context_docs]
            self._send(200, {"reply": reply, "sources": sources})
        except Exception as e:  # noqa: BLE001 — 클라이언트에 원인 전달
            self._send(500, {"error": str(e)})
