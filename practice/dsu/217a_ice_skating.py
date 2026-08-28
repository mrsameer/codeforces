"""Codeforces 217A — Ice Skating.
https://codeforces.com/problemset/problem/217/A

Two points are already connected when they share an x or a y coordinate, so
group them with a DSU; joining c components into one costs c - 1 new edges.

DSU is pasted in from snippets/py/dsu.py — Codeforces takes a single file.
"""
import sys


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def unite(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1
        return True


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    points = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]

    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                dsu.unite(i, j)
    print(dsu.components - 1)


main()
