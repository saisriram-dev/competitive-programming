import sys
input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    ans = n
    power = 2
    while power <= n:
        ans += n // power
        power *= 2
    out.append(ans)

print("\n".join(map(str, out)))
