import sys

# Fast I/O for competitive programming
input = sys.stdin.readline

def solve():
    """
    Calculates the number of valid ways to replace '?' in the string.
    The string is valid if the characters at even indices form an alternating 
    binary sequence, and the characters at odd indices also form an alternating 
    binary sequence.
    """
    n = int(input().strip())
    s = input().strip()

    # We track two possible alternating patterns for the even indices:
    # Pattern 0: 0, 1, 0, 1, ... (Starts with 0)
    # Pattern 1: 1, 0, 1, 0, ... (Starts with 1)
    even_pattern_0_valid = True
    even_pattern_1_valid = True
    
    # We track the same two alternating patterns for the odd indices:
    odd_pattern_0_valid = True
    odd_pattern_1_valid = True

    for i in range(n):
        char = s[i]
        
        # '?' acts as a wildcard and can match any pattern, so we skip it
        if char == "?":
            continue
            
        # Determine what the character *should* be for "Pattern 0" (starting with '0')
        # We use integer division to map the index within the subsequence.
        #
        # For even indices (0, 2, 4, 6...): i//2 is 0, 1, 2, 3... -> expected '0', '1', '0', '1'
        # For odd indices  (1, 3, 5, 7...): i//2 is 0, 1, 2, 3... -> expected '0', '1', '0', '1'
        expected_char_for_pattern_0 = str((i // 2) % 2)
        
        if i % 2 == 0:
            # We are looking at an EVEN index
            if char != expected_char_for_pattern_0:
                # If it doesn't match Pattern 0, then Pattern 0 is ruined
                even_pattern_0_valid = False
            
            if char == expected_char_for_pattern_0:
                # If it perfectly matches Pattern 0, it means it violates Pattern 1
                # (because Pattern 1 is just the exact opposite of Pattern 0)
                even_pattern_1_valid = False
        else:
            # We are looking at an ODD index
            if char != expected_char_for_pattern_0:
                odd_pattern_0_valid = False
                
            if char == expected_char_for_pattern_0:
                odd_pattern_1_valid = False

    # Count how many valid patterns survived for the even and odd subsequences
    # It can be 2 (all '?'s), 1 (forced into one pattern), or 0 (impossible string)
    ways_even = (1 if even_pattern_0_valid else 0) + (1 if even_pattern_1_valid else 0)
    ways_odd = (1 if odd_pattern_0_valid else 0) + (1 if odd_pattern_1_valid else 0)

    # The total combinations are the independent valid ways multiplied together
    # Output modulo 998244353 to prevent massive numbers
    return (ways_even * ways_odd) % 998244353


if __name__ == "__main__":
    # Read number of test cases
    t = int(input().strip())
    for _ in range(t):
        print(solve())
