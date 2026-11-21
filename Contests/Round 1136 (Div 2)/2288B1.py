import sys

input = sys.stdin.readline


def solve():
    x, y, n = map(int, input().split())
    spell = input().strip()

    best = x + y
    for ch in spell:
        if x + y == 0:
            break
        if ch == "-":
            if y >= 2:
                y -= 1
                x += 1
            elif y == 1 and x >= 1:
                x -= 1
            elif y == 1:
                y = 0
                x = 1
            else:
                x -= 1
        else:
            if y >= 1:
                y += 1
            else:
                x -= 1
                y += 1
        best = max(best, x + y)
    return best


t = int(input())
out = [str(solve()) for _ in range(t)]
print("\n".join(out))
