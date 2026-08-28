"""BFS, Dijkstra and topological sort over adjacency lists.

Unweighted graphs are list[list[int]]; weighted ones list[list[tuple[int, int]]]
holding (neighbour, weight).
"""
import heapq
from collections import deque

INF = float("inf")


def bfs(adj: list[list[int]], source: int) -> list[int]:
    """Shortest distances in edges; -1 for unreachable vertices."""
    dist = [-1] * len(adj)
    dist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def dijkstra(adj: list[list[tuple[int, int]]], source: int) -> list[float]:
    """Shortest distances over non-negative weights; INF for unreachable."""
    dist: list[float] = [INF] * len(adj)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def topological_sort(adj: list[list[int]]) -> list[int]:
    """Kahn's algorithm; returns [] when the graph has a cycle."""
    n = len(adj)
    indegree = [0] * n
    for u in range(n):
        for v in adj[u]:
            indegree[v] += 1
    queue = deque(u for u in range(n) if indegree[u] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else []
