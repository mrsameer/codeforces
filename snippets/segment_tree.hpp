// Iterative segment tree over an arbitrary monoid.
// Build O(n), point update and range query O(log n).
#pragma once
#include <functional>
#include <vector>

template <typename T>
struct SegTree {
    int n;
    T identity;
    std::function<T(const T&, const T&)> merge;
    std::vector<T> tree;

    SegTree(const std::vector<T>& values, T identity_,
            std::function<T(const T&, const T&)> merge_)
        : n((int)values.size()), identity(identity_), merge(std::move(merge_)),
          tree(2 * (int)values.size(), identity_) {
        for (int i = 0; i < n; ++i) tree[n + i] = values[i];
        for (int i = n - 1; i > 0; --i) tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
    }

    void set(int i, const T& value) {
        for (tree[i += n] = value; i > 1; i >>= 1)
            tree[i >> 1] = merge(tree[i & ~1], tree[i | 1]);
    }

    // Half-open query on [l, r).
    T query(int l, int r) const {
        T left = identity, right = identity;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) left = merge(left, tree[l++]);
            if (r & 1) right = merge(tree[--r], right);
        }
        return merge(left, right);
    }
};
