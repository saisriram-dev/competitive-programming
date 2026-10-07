import sys

input = sys.stdin.readline


def solve():
    t_str = input().strip()
    if not t_str:
        return ""

    p = input().strip()
    n, m = len(t_str), len(p)
    a = list(map(int, input().split()))
    a = [x - 1 for x in a]

    def check(mid):
        x = a[:mid]
        j = 0

        for i in range(n):
            if i in x:
                continue
            if j < m and t_str[i] == p[j]:
                j += 1

        return j == m

    low = 0
    high = n
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

        return ans


t = int(input())
for _ in range(t):
    print(solve())
