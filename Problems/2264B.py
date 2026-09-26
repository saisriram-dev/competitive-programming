import heapq
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    if m == 1:
        return max(arr)

    running_sum = 0
    max_heap = []
    ans = float('-inf')

    for i in range(n):
        if len(max_heap) == m - 1:
            current_score = m * arr[i] - running_sum
            ans = max(ans, current_score)

        if len(max_heap) < m - 1:
            heapq.heappush(max_heap, -arr[i])
            running_sum += arr[i]

        elif -max_heap[0] > arr[i]:
            largest_helper = -heapq.heappop(max_heap)
            running_sum -= largest_helper

            heapq.heappush(max_heap, -arr[i])
            running_sum += arr[i]

    return ans

t = int(input().strip())
for _ in range(t):
    print(solve())
