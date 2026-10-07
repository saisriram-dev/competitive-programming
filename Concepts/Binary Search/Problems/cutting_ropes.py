def max_rope_length(lengths: list[float], K: int) -> float:
    # Helper predicate function
    def check(x: float) -> bool:
        if x == 0:
            return True
        pieces = sum(int(length // x) for length in lengths)
        return pieces >= K

    # Set search boundaries
    low = 0.0
    high = max(lengths) if lengths else 0.0

    # Fixed-iteration float binary search
    for _ in range(100):
        mid = low + (high - low) / 2.0
        
        if check(mid):
            low = mid   # Length 'mid' is possible; search higher
        else:
            high = mid  # Length 'mid' is too long; search lower

    return low
