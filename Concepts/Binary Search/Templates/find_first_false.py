def check():
    pass

def find_fisrt_false(low, high):
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid):
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    return ans
