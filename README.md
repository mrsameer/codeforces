# Codeforces

C++ and Python workspace for Codeforces practice and contests.

## Layout

```
template.cpp        starting point for every C++ solution
template.py         starting point for every Python solution
scripts/cf          build / run / sample-test helper
include/bits/       <bits/stdc++.h> shim for Apple clang (libc++ lacks it)
snippets/           reusable algorithm headers (C++)
snippets/py/        the same algorithms as importable Python modules
contests/           one folder per contest, e.g. contests/1234/a.cpp
practice/           solved problems by topic, e.g. practice/graphs/20c_dijkstra.py
```

`practice/README.md` covers the naming convention, how to add a problem, and
when to pick Python over C++.

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

## Choosing a language

The file extension picks the language — everything else is identical. Pass
`--py` to start a Python solution:

```bash
cf new contests/1234/a --py
```

That writes `a.py` from `template.py`. Writing the extension yourself works
too (`cf new contests/1234/a.py`).

For `build` / `run` / `test`, name the file with its extension to be explicit:

```bash
cf test contests/1234/a.py
```

Leaving the extension off resolves to whichever file exists, preferring `.cpp`
when you have both — handy for rewriting a too-slow Python solution in C++
without touching the sample files, which are shared between the two.

`build` compiles C++; for Python it byte-compiles the file, so a typo in an
unexercised branch surfaces before you spend a submission on it.

## Compile and run flags

C++ builds use `-std=c++20 -O2 -Wall -Wextra -Wshadow -DLOCAL` with
AddressSanitizer and UBSan enabled, so out-of-bounds access and undefined
behaviour fail loudly instead of silently passing samples. Override via
environment:

| Variable | Default | Effect |
| --- | --- | --- |
| `CF_STD` | `c++20` | C++ language standard |
| `CF_SANITIZE` | `1` | set to `0` to drop sanitizers |
| `CXX` | `g++` | C++ compiler |
| `CF_PYTHON` | `python3` | Python interpreter |

Sanitizers slow execution noticeably. If a solution is near the time limit
locally, re-check with `CF_SANITIZE=0 cf test ...` before assuming it is too
slow — Codeforces compiles without them.

Codeforces offers PyPy 3, which is usually several times faster than CPython on
tight loops. Local timings under `python3` are therefore pessimistic; install
PyPy and use `CF_PYTHON=pypy3 cf test ...` when a solution looks borderline.

## Templates

`template.cpp` includes the usual aliases (`ll`, `pii`, `all(x)`), a `dbg(...)`
macro that prints only under `-DLOCAL` (so it costs nothing on the judge), and
a multi-test `main` — comment out the `cin >> t;` line for single-test problems.

`template.py` mirrors it: token readers (`ni`, `ns`, `nints`, `nstrs`) that
parse all of stdin at once, `emit(...)` to queue output flushed in one write at
exit, a `dbg(...)` that only speaks when `cf` sets `CF_LOCAL`, and the same
multi-test `main` — delete the `t = ni()` line for single-test problems.

Both fast-IO paths read stdin to EOF, so neither template suits interactive
problems; those need line-at-a-time reads with an explicit flush after every
answer.

## Snippets

C++ snippets are header-only, drop-in via `#include "../../snippets/dsu.hpp"`
or by pasting the relevant struct into the submission.

| File | Contents |
| --- | --- |
| `dsu.hpp` | union-find with union by size + path compression |
| `segment_tree.hpp` | iterative segment tree over any monoid |
| `graph.hpp` | BFS, Dijkstra, topological sort |
| `number_theory.hpp` | sieves, factorization, `power_mod`, extended gcd |
| `modint.hpp` | `mint` / `mint998` modular arithmetic type |

`snippets/py/` carries the same algorithms as plain modules. Codeforces takes a
single file, so paste the class or function you need into your solution rather
than importing.

| File | Contents |
| --- | --- |
| `dsu.py` | `DSU` — union by size + path compression |
| `segment_tree.py` | `SegmentTree` over any monoid |
| `graph.py` | `bfs`, `dijkstra`, `topological_sort` |
| `number_theory.py` | sieves, `factorize`, `divisors`, `extended_gcd`, `Binomial` |

There is no Python equivalent of `modint.hpp` — ints are arbitrary precision
and `pow(base, exp, mod)` is built in.

`practice/` has a worked, sample-tested solution for each of these: `dsu/`,
`graphs/`, and `number_theory/` each solve a real problem with the snippet
pasted in, which is the shape an actual submission takes.

Codeforces runs real GCC, which has a genuine `<bits/stdc++.h>`, so the shim in
`include/` never needs to be submitted — it only makes local builds work.
