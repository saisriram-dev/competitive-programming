# PREFIX SUM ARRAY (also called Cumulative Sum Array)


# WHAT IS IT?
# A prefix sum array stores the running total of elements up to every index.
# After building it once, any range sum can be answered in constant time.

# ORIGINAL ARRAY:
#   a = [10, 20, 30, 40, 50]
#   indices: 0   1   2   3   4

# PREFIX ARRAY WE WILL BUILD:
#   prefix = [0, 10, 30, 60, 100, 150]
#   meaning:
#     prefix[0] = 0                  (empty sum - useful base case)
#     prefix[1] = a[0]               = 10
#     prefix[2] = a[0]+a[1]          = 30
#     prefix[3] = a[0]+a[1]+a[2]     = 60
#     prefix[4] = a[0]...a[3]        = 100
#     prefix[5] = a[0]...a[4]        = 150  (sum of entire array)

# TIME & SPACE COMPLEXITY
# Building the prefix array : O(n) time, O(n) extra space
# Answering one range query : O(1) time
# Answering q range queries : O(n + q) total time
#
# Without prefix sums, each range sum would take O(n) time → O(n·q) total.
# Prefix sums turn that into O(n + q), which is dramatically better when q is large.

# WHEN / WHY SHOULD YOU USE PREFIX SUMS?

# Use them when:
#   1. The array is STATIC (does not change after creation).
#   2. You have MANY range-sum queries (or need sums repeatedly).
#   3. You need the sum of any contiguous subarray quickly.

# Classic problem types:
#   • Range Sum Queries (LeetCode 303 – Range Sum Query - Immutable)
#   • Subarray sum equals K (LeetCode 560)
#   • Number of subarrays with sum in a given range
#   • 2D prefix sums for matrix range queries
#   • Difference arrays (the reverse idea – useful for range updates)
#   • Sliding window / cumulative frequency problems
#   • Finding equilibrium index, pivot index, etc.

# DO NOT use them when:
#   • The array keeps changing (then use Fenwick Tree / Segment Tree)
#   • You only need a single sum (just loop once)
#   • You need non-contiguous sums or more complex queries

# CODE WITH DETAILED EXPLANATIONS


a = [10, 20, 30, 40, 50]          # Original array (0-based indexing)
n = len(a)                        # n = 5

# Create prefix array of size n+1.
# Why n+1?  So that prefix[0] can be 0 and the formula stays clean:
# sum(L, R) = prefix[R+1] - prefix[L]
prefix = [0] * (n + 1)

# Build the prefix sum array
# Loop runs from i = 1 to n
# At each step: prefix[i] = prefix[i-1] + a[i-1]
# This is a classic dynamic-programming style accumulation.
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]

print("Prefix array:", prefix)
# Output: [0, 10, 30, 60, 100, 150]


# HOW TO ANSWER RANGE SUM QUERIES
# Formula (0-based indices L and R inclusive):
#   sum from a[L] to a[R]  =  prefix[R+1] - prefix[L]
#
# Why does this work?
#   prefix[R+1] = a[0] + a[1] + ... + a[R]
#   prefix[L]   = a[0] + a[1] + ... + a[L-1]
#   subtracting cancels everything before L → leaves exactly a[L..R]

def range_sum(L, R):
    """
    Returns sum of a[L..R] (inclusive) in O(1) time.
    Preconditions: 0 ≤ L ≤ R < n
    """
    return prefix[R + 1] - prefix[L]


# ---------- Examples ----------
print("Sum of whole array a[0..4]:", range_sum(0, 4))   # 150
print("Sum a[1..3] (20+30+40):",     range_sum(1, 3))   # 90
print("Sum a[2..4] (30+40+50):",     range_sum(2, 4))   # 120
print("Single element a[3]:",        range_sum(3, 3))   # 40


# EXTRA: Handling 1-based indexing (common in competitive programming)
# If the problem gives you 1-based indices, just shift them:
#   sum from index L to R (1-based) = prefix[R] - prefix[L-1]
#
# Example:
#   1-based query L=2, R=4  →  corresponds to a[1], a[2], a[3]
#   answer = prefix[4] - prefix[1] = 100 - 10 = 90
