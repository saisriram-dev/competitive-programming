import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    odd = []
    even = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if len(odd) % 2 == 0:
        return "Moggity"

    if (len(odd) == 1 and len(even) == 1) or (len(odd) == 3 and len(even) == 0):
        return "Larpity"

    return "Moggity"


t = int(input())
for _ in range(t):
    print(solve())
