from collections import Counter
 
def get_mode(freq):
    if not freq:
        return 0
    max_f = max(freq.values())
    candidates = [v for v, f in freq.items() if f == max_f]
    return max(candidates)
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rem = Counter(a)
    cur_freq = Counter()
    res = []
    for _ in range(n):
        best_mode = -1
        best_v = -1
        for v in list(rem.keys()):
            if rem[v] == 0:
                continue
            # try adding v
            cur_freq[v] += 1
            new_mode = get_mode(cur_freq)
            cur_freq[v] -= 1
            if cur_freq[v] == 0:
                del cur_freq[v]
            if new_mode > best_mode or (new_mode == best_mode and v > best_v):
                best_mode = new_mode
                best_v = v
        # commit the best
        res.append(best_v)
        rem[best_v] -= 1
        cur_freq[best_v] += 1
        if rem[best_v] == 0:
            del rem[best_v]
    print(*res)