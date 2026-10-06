n, x, y = map(int, input().split())

def check(T):
    first = min(x, y)

    if T < first:
        return False

    remaining = T - first
    copies = (remaining // x) + (remaining // y)

    return copies >= n - 1

left, right = 0, (n * min(x, y))
ans = -1

while left <= right:
    mid = left + (right - left) // 2

    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
