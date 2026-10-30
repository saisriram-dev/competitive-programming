import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    first = float('inf')
    last = float('-inf')
    
    for i in range(n):
        if arr[i] != 0:
            first = min(first, i)
            last = max(last, i)

    if first == float('inf'):
        return " ".join(map(str, arr))

    for i in range(int(first), int(last + 1)):
        if i == first or i == last:
            arr[i] = 1
        elif arr[i] != 0 and arr[i] != 1:
            arr[i] = 0

    return " ".join(map(str, arr))

t = int(input())
for _ in range(t):
    print(solve())
