// Common graph traversals on adjacency lists.
#pragma once
#include <cstdint>
#include <queue>
#include <vector>

using Graph = std::vector<std::vector<int>>;
// (neighbour, weight) pairs for the weighted routines.
using WGraph = std::vector<std::vector<std::pair<int, std::int64_t>>>;

// Shortest path in edge count from `source`; unreachable nodes stay -1.
inline std::vector<int> bfs(const Graph& g, int source) {
    std::vector<int> dist(g.size(), -1);
    std::queue<int> q;
    dist[source] = 0;
    q.push(source);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g[u])
            if (dist[v] == -1) { dist[v] = dist[u] + 1; q.push(v); }
    }
    return dist;
}

// Dijkstra for non-negative weights; unreachable nodes stay INF.
inline std::vector<std::int64_t> dijkstra(const WGraph& g, int source) {
    const std::int64_t INF = (std::int64_t)4e18;
    std::vector<std::int64_t> dist(g.size(), INF);
    using State = std::pair<std::int64_t, int>;
    std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
    dist[source] = 0;
    pq.push({0, source});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;          // stale entry
        for (auto [v, w] : g[u])
            if (d + w < dist[v]) { dist[v] = d + w; pq.push({dist[v], v}); }
    }
    return dist;
}

// Topological order of a DAG; empty result means the graph has a cycle.
inline std::vector<int> topo_sort(const Graph& g) {
    int n = (int)g.size();
    std::vector<int> indeg(n, 0), order;
    for (int u = 0; u < n; ++u) for (int v : g[u]) ++indeg[v];
    std::queue<int> q;
    for (int u = 0; u < n; ++u) if (indeg[u] == 0) q.push(u);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : g[u]) if (--indeg[v] == 0) q.push(v);
    }
    if ((int)order.size() != n) order.clear();
    return order;
}
