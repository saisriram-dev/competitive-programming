import sys

input = sys.stdin.readline


def max3(arr):
    arr = arr[:]  # copy so the original list isn't modified
    top = []
    for _ in range(3):
        m = max(arr)
        idx = arr.index(m)
        top.append((m, idx))
        arr[idx] = -1  # mark as used, keeps other indices unchanged
    return top


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    top3_a = max3(a)
    top3_b = max3(b)
    top3_c = max3(c)

    best = 0

    for va, ia in top3_a:
        for vb, ib in top3_b:
            if ia == ib:
                continue
            for vc, ic in top3_c:
                if ic == ia or ic == ib:
                    continue
                best = max(best, va + vb + vc)

    return best


t = int(input())
for _ in range(t):
    print(solve())
