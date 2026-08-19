# Codeforces

C++ workspace for Codeforces practice and contests.

## Layout

```
template.cpp        starting point for every solution
scripts/cf          build / run / sample-test helper
include/bits/       <bits/stdc++.h> shim for Apple clang (libc++ lacks it)
snippets/           reusable algorithm headers
contests/           one folder per contest, e.g. contests/1234/a.cpp
practice/           topic practice, e.g. practice/graphs/dijkstra.cpp
```

## Usage

Add the helper to your PATH once:

```bash
export PATH="$PATH:/Volumes/Extreme SSD/sameer_workspace/codeforces/scripts"
```

Then, per problem:

```bash
cf new contests/1234/a
```

That copies `template.cpp` to `contests/1234/a.cpp` and creates empty
`a.1.in` / `a.1.out` sample files. Paste the problem's sample input and
expected output into those, add `a.2.in` / `a.2.out` for more cases, then:

```bash
cf test contests/1234/a
```

Other commands:

```bash
cf build contests/1234/a
```

```bash
cf run contests/1234/a
```

`run` compiles and reads from your terminal; `test` diffs actual against
expected output for every `*.N.in` file, ignoring trailing whitespace.

## Compile flags

Local builds use `-std=c++20 -O2 -Wall -Wextra -Wshadow -DLOCAL` with
AddressSanitizer and UBSan enabled, so out-of-bounds access and undefined
behaviour fail loudly instead of silently passing samples. Override via
environment:

| Variable | Default | Effect |
| --- | --- | --- |
| `CF_STD` | `c++20` | language standard |
| `CF_SANITIZE` | `1` | set to `0` to drop sanitizers |
| `CXX` | `g++` | compiler |

Sanitizers slow execution noticeably. If a solution is near the time limit
locally, re-check with `CF_SANITIZE=0 cf test ...` before assuming it is too
slow — Codeforces compiles without them.

## Template

`template.cpp` includes the usual aliases (`ll`, `pii`, `all(x)`), a `dbg(...)`
macro that prints only under `-DLOCAL` (so it costs nothing on the judge), and
a multi-test `main` — comment out the `cin >> t;` line for single-test problems.

## Snippets

Header-only, drop-in via `#include "../../snippets/dsu.hpp"` or by pasting the
relevant struct into the submission.

| File | Contents |
| --- | --- |
| `dsu.hpp` | union-find with union by size + path compression |
| `segment_tree.hpp` | iterative segment tree over any monoid |
| `graph.hpp` | BFS, Dijkstra, topological sort |
| `number_theory.hpp` | sieves, factorization, `power_mod`, extended gcd |
| `modint.hpp` | `mint` / `mint998` modular arithmetic type |

Codeforces runs real GCC, which has a genuine `<bits/stdc++.h>`, so the shim in
`include/` never needs to be submitted — it only makes local builds work.
