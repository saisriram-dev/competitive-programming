import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = n - k + 1

    seen = set(a[:p])
    m = next((v for v in range(p) if v not in seen), -1)
    if m == -1:
        return "-1"

    # any prefix element >= p is safe to swap out
    i = next(idx for idx in range(p) if a[idx] >= p)
    j = a.index(m)          # m is guaranteed to be outside the prefix
    return f"{i + 1} {j + 1}"

for _ in range(int(input())):
    print(solve())
