// Disjoint Set Union with union by size and path compression.
// find/unite are effectively O(1) amortized.
#pragma once
#include <numeric>
#include <vector>

struct DSU {
    std::vector<int> parent, size_;
    int components;

    explicit DSU(int n) : parent(n), size_(n, 1), components(n) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        while (parent[x] != x) x = parent[x] = parent[parent[x]];
        return x;
    }

    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (size_[a] < size_[b]) std::swap(a, b);
        parent[b] = a;
        size_[a] += size_[b];
        --components;
        return true;
    }

    bool same(int a, int b) { return find(a) == find(b); }
    int size(int x) { return size_[find(x)]; }
};
