n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = float("inf")
dp = [INF] * (x + 1)
dp[0] = 0

for s in range(1, x + 1):
    for c in coins:
        if c <= s and dp[s - c] != INF:
            dp[s] = min(dp[s], dp[s - c] + 1)

print(dp[x] if dp[x] != INF else -1)
