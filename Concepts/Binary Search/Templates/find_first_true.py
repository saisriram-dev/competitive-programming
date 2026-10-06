def check():
    pass

def find_first_true(low, high):
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
