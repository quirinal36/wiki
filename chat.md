---
title: 위키 채팅
---

# 위키 채팅

위키 문서를 근거로 답하는 AI 채팅입니다. 질문하면 관련 문서를 찾아 함께 표시합니다.

<div id="chat-app">
  <div id="chat-log"></div>
  <form id="chat-form">
    <textarea id="chat-input" rows="2" placeholder="위키에 대해 질문해보세요… (Enter 전송, Shift+Enter 줄바꿈)"></textarea>
    <button type="submit" id="chat-send">전송</button>
  </form>
  <p id="chat-status"></p>
</div>

<style>
#chat-app { max-width: 100%; }
#chat-log {
  min-height: 40vh; max-height: 62vh; overflow-y: auto;
  border: 1px solid var(--md-default-fg-color--lightest, #ddd);
  border-radius: 10px; padding: 1em; margin-bottom: .8em;
  display: flex; flex-direction: column; gap: .7em;
  background: var(--md-code-bg-color, #f8f8f8);
}
.chat-msg { max-width: 85%; padding: .6em .9em; border-radius: 12px;
  line-height: 1.55; font-size: .78rem; white-space: pre-wrap; word-break: break-word; }
.chat-msg.user { align-self: flex-end; background: var(--md-primary-fg-color, #4051b5); color: #fff;
  border-bottom-right-radius: 3px; }
.chat-msg.bot { align-self: flex-start; background: var(--md-default-bg-color, #fff);
  border: 1px solid var(--md-default-fg-color--lightest, #ddd); border-bottom-left-radius: 3px; }
.chat-msg.bot .sources { margin-top: .6em; padding-top: .5em;
  border-top: 1px dashed var(--md-default-fg-color--lightest, #ccc); font-size: .68rem; }
.chat-msg.bot .sources a { display: inline-block; margin: .15em .3em .15em 0; padding: .1em .55em;
  border-radius: 999px; background: var(--md-accent-fg-color--transparent, rgba(83,109,254,.1)); }
#chat-form { display: flex; gap: .5em; align-items: flex-end; }
#chat-input { flex: 1; resize: vertical; padding: .55em .8em; font: inherit; font-size: .78rem;
  border: 1px solid var(--md-default-fg-color--lightest, #ccc); border-radius: 8px;
  background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #222); }
#chat-send { padding: .55em 1.3em; border: 0; border-radius: 8px; cursor: pointer;
  background: var(--md-primary-fg-color, #4051b5); color: #fff; font: inherit; font-size: .78rem; }
#chat-send:disabled { opacity: .5; cursor: wait; }
#chat-status { font-size: .68rem; opacity: .7; margin: .4em 0 0; min-height: 1em; }
</style>

<script>
(function () {
  // 로컬 mkdocs serve(포트 8000)에서는 별도 채팅 서버(8001)를,
  // Vercel 배포에서는 같은 도메인의 서버리스 함수(/api/chat)를 사용
  var API = (location.hostname === 'localhost' || location.hostname === '127.0.0.1')
    ? 'http://localhost:8001/api/chat'
    : '/api/chat';
  var history = [];

  function initChat() {
    var form = document.getElementById('chat-form');
    if (!form || form.dataset.bound) return;   // instant navigation 중복 초기화 방지
    form.dataset.bound = '1';

    var log = document.getElementById('chat-log');
    var input = document.getElementById('chat-input');
    var send = document.getElementById('chat-send');
    var status = document.getElementById('chat-status');

    function bubble(role, text, sources) {
      var div = document.createElement('div');
      div.className = 'chat-msg ' + (role === 'user' ? 'user' : 'bot');
      div.textContent = text;
      if (sources && sources.length) {
        var s = document.createElement('div');
        s.className = 'sources';
        s.appendChild(document.createTextNode('근거 문서: '));
        sources.forEach(function (src) {
          var a = document.createElement('a');
          a.href = src.url; a.textContent = src.title;
          s.appendChild(a);
        });
        div.appendChild(s);
      }
      log.appendChild(div);
      log.scrollTop = log.scrollHeight;
      return div;
    }

    function submit() {
      var text = input.value.trim();
      if (!text || send.disabled) return;
      input.value = '';
      bubble('user', text);
      history.push({ role: 'user', content: text });
      send.disabled = true;
      status.textContent = '위키를 검색하고 답변을 생성하는 중…';

      fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history })
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data.error) throw new Error(data.error);
          history.push({ role: 'assistant', content: data.reply });
          bubble('bot', data.reply, data.sources);
          status.textContent = '';
        })
        .catch(function (e) {
          var hint = API.indexOf('localhost:8001') !== -1
            ? '\n채팅 서버(chat_server.py, 포트 8001)가 실행 중인지 확인해주세요.'
            : '\n잠시 후 다시 시도해주세요. 계속되면 Vercel 함수 로그를 확인해주세요.';
          bubble('bot', '오류가 발생했습니다: ' + e.message + hint);
          status.textContent = '';
        })
        .finally(function () {
          send.disabled = false;
          input.focus();
        });
    }

    form.addEventListener('submit', function (e) { e.preventDefault(); submit(); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); submit(); }
    });
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initChat(); });
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChat);
  } else {
    initChat();
  }
})();
</script>
