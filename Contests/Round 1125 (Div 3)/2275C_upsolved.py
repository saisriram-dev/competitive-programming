import sys
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n < 5:
        print(0)
        return

    values = []
    for i in range(n - 4):
        values.append(arr[i] + arr[i+2] - arr[i+4])

    freq = defaultdict(int)
    ans = 0

    for j in range(len(values)):
        val = values[j]
        
        matches = freq[val]
        
        if j >= 2 and values[j - 2] == val:
            matches -= 1
        if j >= 4 and values[j - 4] == val:
            matches -= 1
            
        ans += matches
        
        freq[val] += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()
