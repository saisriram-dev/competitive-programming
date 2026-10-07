import sys

input = sys.stdin.readline


def solve():
  t = input().strip()
  if not t:
    return ""

  p = input().strip()
  n, m = len(t), len(p)
  a = list(map(int, input().split()))
  a = [x - 1 for x in a]  # convert to 0-based

  def check(mid):
    removed = set(a[:mid])  # O(1) lookup
    j = 0  # pointer in p

    for i in range(n):
      if i in removed:
        continue
      if t[i] == p[j]:
        j += 1
        if j == m:  # fully matched p
          return True

    return False

  low = 0
  high = n  # can try removing up to n characters
  ans = 0

  while low <= high:
    mid = (low + high) // 2
    if check(mid):
      ans = mid  # mid is feasible → try to remove more
      low = mid + 1
    else:
      high = mid - 1

  return ans


t = int(input())
for _ in range(t):
  print(solve())
