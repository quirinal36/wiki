---
title: 그래프 뷰
---

# 그래프 뷰

위키 문서 간 `[[위키링크]]` 연결을 시각화한 그래프입니다. 노드를 클릭하면 해당 문서로 이동하고, 드래그·휠 줌이 가능합니다.

<div id="wiki-graph" style="width: 100%; height: 75vh; border: 1px solid var(--md-default-fg-color--lightest, #ddd); border-radius: 8px;"></div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script>
(function () {
  function initGraph() {
    var el = document.getElementById('wiki-graph');
    if (!el || typeof echarts === 'undefined') return;

    var isDark = document.body.getAttribute('data-md-color-scheme') === 'slate';
    var chart = echarts.init(el, isDark ? 'dark' : null);

    fetch('/assets/javascripts/graph.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        // Obsidian처럼 연결 수에 따라 노드 크기 스케일링
        data.nodes.forEach(function (n) {
          n.symbolSize = Math.max(6, Math.min(34, 5 + Math.sqrt(n.symbolSize || 1) * 4));
        });

        chart.setOption({
          backgroundColor: 'transparent',
          tooltip: { formatter: '{b}' },
          series: [{
            type: 'graph',
            layout: 'force',
            data: data.nodes,
            links: data.links,
            roam: true,
            draggable: true,
            label: {
              show: true,
              position: 'bottom',
              fontSize: 10,
              color: isDark ? '#aaa' : '#555',
              formatter: function (p) {
                return p.name.length > 18 ? p.name.slice(0, 17) + '…' : p.name;
              }
            },
            itemStyle: { color: isDark ? '#9a86fd' : '#7c6bd6' },
            lineStyle: { color: isDark ? '#555' : '#ccc', width: 1, curveness: 0.1 },
            emphasis: {
              focus: 'adjacency',
              label: { show: true, fontWeight: 'bold' },
              lineStyle: { width: 2 }
            },
            force: { repulsion: 120, gravity: 0.08, edgeLength: 60, friction: 0.2 },
            scaleLimit: { min: 0.3, max: 8 }
          }]
        });

        chart.on('click', function (params) {
          if (params.dataType === 'node' && params.data.value) {
            window.location.href = params.data.value;
          }
        });

        window.addEventListener('resize', function () { chart.resize(); });
      })
      .catch(function (e) {
        el.innerHTML = '<p style="padding:1em">graph.json 로드 실패: ' + e + '</p>';
      });
  }

  // Material instant navigation 대응 + 일반 로드 대응
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function () { initGraph(); });
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGraph);
  } else {
    initGraph();
  }
})();
</script>
