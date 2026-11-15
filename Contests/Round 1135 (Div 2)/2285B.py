import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    binary_string = input().strip()

    count_ones = binary_string.count("1")
    count_zeros = n - count_ones

    if count_ones >= count_zeros and k > 0:
        while count_ones < n and k > 0:
            count_ones += 1
            count_zeros -= 1
            k -= 1
    else:
        while count_zeros < n and k > 0:
            count_zeros += 1
            count_ones -= 1
            k -= 1

    return (
        1
        + (count_ones * (count_ones + 1)) // 2
        + (count_zeros * (count_zeros + 1)) // 2
    )


t = int(input())
for _ in range(t):
    print(solve())
