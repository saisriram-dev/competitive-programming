import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    seq = input().strip()

    current_w = seq[: k].count("W")
    min_w = current_w

    for i in range(k, n):
        if seq[i - k] == "W":
            current_w -= 1
        if seq[i] == "W":
            current_w += 1

        min_w = min(min_w, current_w)

    return min_w

t = int(input())
for _ in range(t):
    print(solve())
