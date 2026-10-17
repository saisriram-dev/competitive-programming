import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = arr[0]
    max_ans = arr[0]

    for i in range(1, n):
        if arr[i - 1] % 2 != arr[i] % 2:
            dp[i] = max(arr[i], dp[i - 1] + arr[i])
        else:
            dp[i] = arr[i]

        max_ans = max(max_ans, dp[i])

    return max_ans

t = int(input())
for _ in range(t):
    print(solve())
