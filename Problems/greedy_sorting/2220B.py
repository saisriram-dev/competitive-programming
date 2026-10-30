import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and arr[i] == arr[j]:
            j += 1

        cnt = max(cnt, j - i)
        i = j

    return "YES" if cnt < m else "NO"

t = int(input())
for _ in range(t):
    print(solve())
