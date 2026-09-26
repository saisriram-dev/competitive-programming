from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    count = Counter(arr)
    if count[0] > count[1]:
        return "Elsie"
    else:
        return "Bessie"

t = int(input().strip())
for _ in range(t):
    print(solve())
