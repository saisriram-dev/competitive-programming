import sys
from collections import Counter
input = sys.stdin.readline

def solve():
    arr = list(map(int, input().split()))
    rounds = 0

    while True:
        counts = Counter(arr)
        for count in counts.values():
            if count > 1:
                return rounds
                break
        
        max_val = max(arr)
        min_val = min(arr)

        if max_val > min_val:
            max_index = arr.index(max_val)
            arr[max_index] -= 1

            min_index = arr.index(min_val)
            arr[min_index] += 1

        
        rounds += 1

    
t = int(input())
for _ in range(t):
    print(solve())
