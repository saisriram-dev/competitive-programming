import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    if n == 1:
        return "0"
    
    k = (n + 1) // 2
    lines = [str(k)]
    
    for i in range(1, k + 1):
        lines.append(f"{i} {i + k - 1}")
    return "\n".join(lines)

t = int(input())
out = []
for _ in range(t):
    out.append(solve())
print("\n".join(out))
