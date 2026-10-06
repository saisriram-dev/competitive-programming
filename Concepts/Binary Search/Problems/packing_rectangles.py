w, h, n = map(int, input().split())

def check(x):
    return (x // w) * (x // h) >= n

left, right = 0, max(w, h) * n

ans = -1
while left <= right:
    mid = left + (right - left) // 2

    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
