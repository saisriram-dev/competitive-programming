import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * n
    max_score = 0

    for i in range(n - 1, -1, -1):
        next_idx = i + arr[i]

        if next_idx < n:
            dp[i] = arr[i] + dp[next_idx]
        else:
            dp[i] = arr[i]

        max_score = max(max_score, dp[i])

    return max_score


t = int(input())
for _ in range(t):
    print(solve())
