import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    col, cnt = [], []
    for x in a:
        if col and col[-1] == x:
            cnt[-1] += 1
        else:
            col.append(x)
            cnt.append(1)

    m = len(col)
    for i in range(m - 1):
        if cnt[i] >= 2 and cnt[i + 1] >= 2:
            return m + 2

    for i in range(m):
        if cnt[i] < 2:
            continue

        if i + 1 < m and (i + 2 >= m or col[i] != col[i + 2]):
            return m + 1
        if i - 1 >= 0 and (i - 2 < 0 or col[i] != col[i - 2]):
            return m + 1
    

t = int(input())
for _ in range(t):
    print(solve())
