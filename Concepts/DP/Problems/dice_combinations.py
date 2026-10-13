MOD = 10**9 + 7

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for s in range(1, n + 1):
    for k in range(1, 7):
        if k <= s:
            dp[s] = (dp[s] + dp[s - k]) % MOD

print(dp[n])
