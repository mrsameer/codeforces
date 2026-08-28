"""Disjoint Set Union with union by size and path compression.

find/unite are effectively O(1) amortized.
"""


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
        """Merge the sets of a and b; False if they were already joined."""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def set_size(self, x: int) -> int:
        return self.size[self.find(x)]
