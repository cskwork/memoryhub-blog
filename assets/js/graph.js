// Force-directed graph for the home page.
// Loads the language-specific graph payload, draws it with vis-network,
// and navigates to the node URL on click. Falls back to a clear message
// if the data file is missing or vis-network fails to load.
(function () {
  function init() {
    var root = document.getElementById('graph');
    if (!root) return;
    var src = root.getAttribute('data-graph');
    if (!src) return;

    var loading = document.createElement('div');
    loading.className = 'graph-loading';
    loading.textContent = 'Loading graph…';
    root.appendChild(loading);

    fetch(src)
      .then(function (resp) {
        if (!resp.ok) throw new Error('graph fetch failed: ' + resp.status);
        return resp.json();
      })
      .then(function (payload) {
        if (typeof vis === 'undefined' || !vis.Network) {
          throw new Error('vis-network not loaded');
        }
        loading.remove();
        render(root, payload);
      })
      .catch(function (err) {
        console.error(err);
        loading.textContent = 'Graph unavailable.';
      });
  }

  function render(root, payload) {
    var isSmall = window.matchMedia('(max-width: 640px)').matches;
    var groupStyles = {
      category: { color: { background: '#3b82f6', border: '#1d4ed8' }, font: { color: '#ffffff', size: isSmall ? 13 : 16 }, shape: 'dot' },
      tag:      { color: { background: '#14b8a6', border: '#0f766e' }, font: { color: '#ffffff', size: isSmall ? 10 : 12 }, shape: 'dot' },
      post:     { color: { background: '#a78bfa', border: '#7c3aed' }, font: { color: '#1f2937', size: isSmall ? 0 : 11 }, shape: 'dot' }
    };

    var nodes = payload.nodes.map(function (n) {
      var style = groupStyles[n.group] || groupStyles.post;
      return {
        id: n.id,
        label: n.label,
        group: n.group,
        value: n.value || 1,
        url: n.url || '',
        color: style.color,
        font: style.font,
        shape: style.shape,
        title: n.label + (n.group === 'category' ? ' (category)' : n.group === 'tag' ? ' (tag)' : '')
      };
    });

    var data = {
      nodes: new vis.DataSet(nodes),
      edges: new vis.DataSet(payload.edges.map(function (e, i) {
        return { id: 'e' + i, from: e.from, to: e.to, color: { color: 'rgba(150,150,150,0.35)' }, width: 0.8 };
      }))
    };

    var options = {
      nodes: { borderWidth: 1, scaling: { min: isSmall ? 4 : 6, max: isSmall ? 22 : 32 } },
      edges: { smooth: { type: 'continuous' } },
      physics: {
        solver: 'forceAtlas2Based',
        forceAtlas2Based: { gravitationalConstant: isSmall ? -35 : -45, springLength: isSmall ? 70 : 90, springConstant: 0.04, avoidOverlap: 0.4 },
        stabilization: { iterations: isSmall ? 160 : 220, fit: true }
      },
      interaction: {
        hover: true,
        tooltipDelay: 120,
        hideEdgesOnDrag: true,
        zoomView: true,
        dragView: true,
        multiselect: false,
        navigationButtons: !isSmall
      },
      layout: { improvedLayout: false }
    };

    var network = new vis.Network(root, data, options);

    network.on('click', function (event) {
      if (!event.nodes || !event.nodes.length) return;
      var node = data.nodes.get(event.nodes[0]);
      if (node && node.url) {
        window.location.href = node.url;
      }
    });

    network.once('stabilizationIterationsDone', function () {
      network.setOptions({ physics: { enabled: false } });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
