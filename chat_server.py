# -*- coding: utf-8 -*-
"""위키 채팅 백엔드.

.env 의 OPENROUTER_API_KEY 를 서버 측에서만 읽고, 위키 마크다운을 검색해
관련 문서를 컨텍스트로 붙여 OpenRouter 에 질의한다. 키는 브라우저에
노출되지 않는다. 표준 라이브러리만 사용 (추가 의존성 없음).

실행: python chat_server.py   (포트 8001)
"""
import json
import os
import re
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8001
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = os.environ.get("CHAT_MODEL", "anthropic/claude-haiku-4.5")

# 인덱싱에서 제외할 디렉터리 (빌드 산출물·내부 설정·아카이브)
SKIP_DIRS = {"site", ".git", ".obsidian", ".archive", "_archive", ".backup",
             ".claude", "templates", "__pycache__", "media"}
MAX_DOCS = 6          # 컨텍스트로 넣을 최대 문서 수
MAX_DOC_CHARS = 2500  # 문서당 최대 길이


def load_api_key():
    env_path = os.path.join(ROOT, ".env")
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError(".env 에서 OPENROUTER_API_KEY 를 찾지 못했습니다")


API_KEY = load_api_key()


def load_wiki():
    """루트 이하 모든 .md 문서를 (경로, 제목, 본문) 으로 로드."""
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
            docs.append({"rel": rel, "title": title, "text": text})
    return docs


WIKI = load_wiki()


def doc_url(rel):
    """마크다운 경로 → mkdocs 디렉터리 URL (index.md → /)."""
    rel = rel[:-3]  # strip .md
    if rel == "index":
        return "/"
    if rel.endswith("/index"):
        rel = rel[:-6]
    return "/" + rel + "/"


# 한국어 조사 — 토큰 끝에 붙으면 떼어낸 변형도 검색에 사용
_PARTICLES = ("은", "는", "이", "가", "을", "를", "의", "에", "에서", "으로", "로",
              "와", "과", "도", "만", "야", "이야", "부터", "까지", "처럼", "보다")


def tokenize(s):
    """영문/숫자 run 과 한글 run 을 분리 추출 ("agentree는" → "agentree", "는")
    하고, 한글 토큰은 조사를 뗀 변형도 추가한다."""
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
    """단순 키워드 스코어링으로 관련 문서 top-k 선택."""
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
                score += 1.0 + min(hits, 10) * 0.3   # 존재 보너스 + 빈도(상한)
            if t in title_low:
                score += 5.0                          # 제목 일치 가중
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


def call_openrouter(messages):
    payload = json.dumps({"model": MODEL, "messages": messages}).encode("utf-8")
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "Wiki Chat",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/health":
            self._send(200, {"ok": True, "docs": len(WIKI), "model": MODEL})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/chat":
            self._send(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            messages = body.get("messages", [])
            last_user = next((m["content"] for m in reversed(messages)
                              if m.get("role") == "user"), "")
            context_docs = retrieve(last_user)
            system = {"role": "system", "content": build_system_prompt(context_docs)}
            reply = call_openrouter([system] + messages[-10:])  # 최근 10턴만 전달
            sources = [{"title": d["title"], "url": doc_url(d["rel"])} for d in context_docs]
            self._send(200, {"reply": reply, "sources": sources})
        except Exception as e:  # noqa: BLE001 — 클라이언트에 원인 전달
            self._send(500, {"error": str(e)})

    def log_message(self, fmt, *args):  # 요청 로그 간소화
        print("[chat]", fmt % args)


if __name__ == "__main__":
    print(f"wiki chat server: {len(WIKI)} docs indexed, model={MODEL}, port={PORT}")
    ThreadingHTTPServer(("localhost", PORT), Handler).serve_forever()
