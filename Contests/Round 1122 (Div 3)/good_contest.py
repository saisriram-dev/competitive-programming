import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    attempt_arr = list(map(int, input().split()))
    ans = max(n - attempt_arr[0], n - attempt_arr[1], n - attempt_arr[2], 3 * n - sum(attempt_arr))
    
    return ans

n = int(input())             # first line: how many words follow
for _ in range(n):
    print(solve())
