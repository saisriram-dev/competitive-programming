import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    mex = 0

    x = arr.index(0)
    y = arr.index(0, x + 1)

    def expand(center):
        l, r = center, center
        curr = 0
        seen = set()

        while l >= 0 and r < len(arr) and arr[l] == arr[r]:   # fix 1: bounds check
            seen.add(arr[l])
            while curr in seen:                                # fix 2: check curr, not mex
                curr += 1
            l -= 1
            r += 1

        return curr                                            # fix 3: return curr

    mex = max(expand(x), expand(y))

    if (x + y) % 2 == 0:
        mex = max(mex, expand((x + y) // 2))                   # fix 4: // instead of /
    else:
        l = (x + y) // 2                                       # fix 5: l was used before assignment
        r = l + 1
        curr = 0
        seen = set()
        while l >= 0 and r < len(arr) and arr[l] == arr[r]:    # fix 1 again: bounds check
            seen.add(arr[l])
            while curr in seen:                                # fix 2 again: check curr
                curr += 1
            l -= 1
            r += 1

        mex = max(mex, curr)

    return mex                                                 # fix 6: solve() must return


t = int(input())
for _ in range(t):
    print(solve())
