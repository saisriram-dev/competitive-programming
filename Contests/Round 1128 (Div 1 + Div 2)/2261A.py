import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()

    k = s.count('1')
    if k == 1:
        return 0
    if k == 2:
        return 1

    return s.rfind('1') - s.find('1')

t = int(input())
for _ in range(t):
    print(solve())
