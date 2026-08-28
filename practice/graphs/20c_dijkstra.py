"""Codeforces 20C — Dijkstra?  https://codeforces.com/problemset/problem/20/C

Shortest path from 1 to n in a weighted undirected graph, printing the route
rather than its length. Dijkstra with a parent array; -1 when n is unreachable.

Adapted from snippets/py/graph.py — the addition is `parent`, which records
the edge that last improved each vertex so the path can be walked back.
"""
import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])

    adj: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for e in range(m):
        a, b, w = int(data[2 + 3 * e]), int(data[3 + 3 * e]), int(data[4 + 3 * e])
        adj[a].append((b, w))
        adj[b].append((a, w))

    INF = float("inf")
    dist: list[float] = [INF] * (n + 1)
    parent = [0] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))

    if dist[n] == INF:
        print(-1)
        return

    path = []
    v = n
    while v:
        path.append(v)
        v = parent[v]
    print(" ".join(map(str, reversed(path))))


main()
