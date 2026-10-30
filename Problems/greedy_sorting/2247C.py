import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a == b:
        return 0

    if 1 not in a or 0 not in b:
        return -1

    ones_in_wrong = 0
    for i in range(n):
        if a[i] != b[i] and a[i] == 1:
            ones_in_wrong += 1

    if ones_in_wrong % 2 == 1:
        return 1

    return 2


t = int(input())
for _ in range(t):
    print(solve())
