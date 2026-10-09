import sys
input = sys.stdin.readline
 
def solve():
    n, k = map(int, input().split())
    seq = input().strip()
 
    i = 0
    j = k - 1
    ans = float('inf')
 
    while j < n:
        ans = min(ans, seq[i: j + 1].count("W"))
        i += 1
        j += 1
 
    return ans
 
t = int(input())
for _ in range(t):
    print(solve())
