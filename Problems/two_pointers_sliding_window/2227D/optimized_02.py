import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    m = 2 * n

    x = arr.index(0)
    y = arr.index(0, x + 1)

    def expand(l, r):
        seen = [False] * (n + 1)
        mex = 0
        while l >= 0  and r < m and arr[l] == arr[r]:
            seen[arr[l]] = True
            while seen[mex]:
                mex += 1
            l -= 1
            r += 1
        return mex

    best = max(expand(x, x), expand(y, y))

    s = x + y
    if s % 2 == 0:
        best = max(best, expand(s // 2, s // 2))        # odd palindrome, x and y mirrored
    else:
        best = max(best, expand(s // 2, s // 2 + 1))    # even palindrome, x and y mirrored

    return best


t = int(input())
for _ in range(t):
    print(solve())
