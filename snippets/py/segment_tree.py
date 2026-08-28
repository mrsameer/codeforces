"""Iterative segment tree over any monoid (associative op + identity).

    tree = SegmentTree([1, 2, 3], min, INF)
    tree.update(1, 0)
    tree.query(0, 3)   # half-open [l, r)
"""
from collections.abc import Callable, Sequence
from typing import Any


class SegmentTree:
    def __init__(
        self,
        values: Sequence[Any],
        op: Callable[[Any, Any], Any],
        identity: Any,
    ) -> None:
        self.n = len(values)
        self.op = op
        self.identity = identity
        self.tree = [identity] * (2 * self.n)
        self.tree[self.n:] = values
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i: int, value: Any) -> None:
        """Set position i to value."""
        i += self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left: int, right: int) -> Any:
        """Fold the half-open range [left, right)."""
        res_l = res_r = self.identity
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                res_l = self.op(res_l, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res_r = self.op(self.tree[right], res_r)
            left //= 2
            right //= 2
        return self.op(res_l, res_r)
