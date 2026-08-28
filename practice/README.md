# Practice

Solved problems, filed by the technique they exercise. Each one is a complete
submission — paste the file into Codeforces as-is.

## Naming

```
practice/<topic>/<id><index>_<slug>.<ext>
```

`<id><index>` is the Codeforces problem id, lowercased: problem 217A becomes
`217a`. That keeps a problem findable from its number alone (`ls practice/**/217a*`)
and makes it obvious which ones you have already done.

Topics are just folders — add one whenever a technique earns it.

| Folder | Exercises |
| --- | --- |
| `basics/` | input parsing, loops, strings — no algorithm to speak of |
| `dsu/` | `snippets/py/dsu.py` |
| `graphs/` | `snippets/py/graph.py` |
| `number_theory/` | `snippets/py/number_theory.py` |
| `example/` | the original C++ walkthrough |

## Adding a problem

```bash
cf new practice/graphs/1234a_slug --py
```

Paste the problem's sample input into `1234a_slug.1.in` and its expected output
into `1234a_slug.1.out`. Add `.2.in` / `.2.out` for the second sample, and keep
going — every `*.N.in` runs.

```bash
cf test practice/graphs/1234a_slug
```

Cases beyond the official samples are worth adding by hand: n = 1, an empty or
maximal input, the case the statement warns about. Samples are chosen to be
readable, not to be adversarial.

## Snippets are pasted, not imported

Codeforces accepts one file, so `217a_ice_skating.py` carries its own copy of
`DSU` rather than importing `snippets/py/dsu.py`. Copy the struct or class you
need into the solution and trim it to the methods you actually call.

The snippet modules stay importable for local experiments — `sys.path.insert(0,
"snippets/py")` from the repo root — but nothing under `practice/` relies on that.

## Choosing a language

Reach for Python when the problem is about getting the idea right: string
manipulation, big integers (no overflow to reason about), dictionaries and
sorting, anything where `itertools` or `collections` does the work. Constructive
and ad-hoc problems are usually quicker to write and easier to debug.

Reach for C++ when the constraints are the difficulty: n up to 1e5 with an
O(n log n) inner loop, heavy recursion, tight per-operation costs, or a time
limit under 2 seconds on a hot path. Interactive problems also want C++ here,
since both templates read stdin to EOF.

Sample files key off the stem, so a Python solution and its C++ rewrite share
test data:

```bash
cf test practice/graphs/1234a_slug.py     # too slow?
cp template.cpp practice/graphs/1234a_slug.cpp
cf test practice/graphs/1234a_slug        # no extension → prefers .cpp
```

Before giving up on a Python solution, re-time it under PyPy, which is what
Codeforces actually runs:

```bash
CF_PYTHON=pypy3 cf test practice/graphs/1234a_slug.py
```

## Verifying a solution you are unsure of

For counting and construction problems, a brute force you trust beats staring at
the code. Write the obvious O(n!) or O(n^3) version, run both over small random
inputs, and compare:

```python
for _ in range(1000):
    case = random_small_case()
    assert fast(case) == brute(case), case
```

Every solution in here was checked that way before its `.out` files were
written: 71A and 158A against a direct reimplementation, 217A against BFS
component counting, 26A against trial-division factorization, and 20C against
Floyd-Warshall over a few hundred random graphs.
