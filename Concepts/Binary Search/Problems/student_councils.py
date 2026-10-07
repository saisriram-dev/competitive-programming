import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = list(map(int, input().split()))

def possible(x):
    if x == 0:
        return True
    
    total = 0
    need = x * k
    for val in a:
        total += min(x, val)
        if total >= need:
            return True
    return total >= need

low = 0
high = sum(a) // k          # tight and safe upper bound
ans = 0

while low <= high:
    mid = (low + high) // 2
    if possible(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
