import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    a_rebuild = [None] * n
    left = 0
    right = n - 1
    for i in range(n):
        if i % 2 == 0:
            a_rebuild[left] = a[i]
            left += 1
        else:
            a_rebuild[right] = a[i]
            right -= 1

    visible = [False] * n

    # visible from the left: strictly taller than everything to its left
    mx = 0
    for i in range(n):
        if a_rebuild[i] > mx:
            visible[i] = True
            mx = a_rebuild[i]

    # visible from the right: strictly taller than everything to its right
    mx = 0
    for i in range(n - 1, -1, -1):
        if a_rebuild[i] > mx:
            visible[i] = True
            mx = a_rebuild[i]

    c = sum(visible)

    print(c)
    print(" ".join(str(num) for num in a_rebuild))


t = int(input())
for _ in range(t):
    solve()
