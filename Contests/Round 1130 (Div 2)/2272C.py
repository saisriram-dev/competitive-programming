import sys
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    gaps = [a[i + 1] - a[i] for i in range(n - 1)]

    def check(k):
        # isolated[i]: no neighbour of a[i] within distance k
        iso = [False] * n
        for i in range(n):
            left = i > 0 and gaps[i - 1] <= k
            right = i < n - 1 and gaps[i] <= k
            iso[i] = not (left or right)

        cnt = 0
        i = 0
        while i < n:
            if iso[i]:
                cnt += 1
                if i + 1 < n and iso[i + 1] and gaps[i] <= 2 * k:
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        return cnt <= x

    low, high = 1, max(gaps)
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())
for _ in range(t):
    print(solve())
