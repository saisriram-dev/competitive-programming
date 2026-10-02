import sys
input = sys.stdin.readline

def solve():
    n, a = map(int, input().split())
    arr = list(map(int, input().split()))

    greater = 0
    lesser = 0

    for x in arr:
        if x > a:
            greater += 1
        elif x < a:
            lesser += 1

    if lesser > greater:
        return a - 1
    else:
        return a + 1

t = int(input())
for _ in range(t):
    print(solve())
