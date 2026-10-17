n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 0

for price, page in zip(prices, pages):
    for b in range(x, price - 1, -1):
        dp[b] = max(
            dp[b], dp[b - price] + page
        )

print(dp[x])
