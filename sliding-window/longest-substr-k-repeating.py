from collections import defaultdict

def longestSubstring( s: str, k: int) -> int:
    res = 0
    for l in range(len(s)):
        freq = defaultdict(int)
        for r in range(l, len(s)):
            freq[s[r]] += 1
            eligible = True
            for v in freq.values():
                if v < k:
                    eligible = False
                    break
            if eligible:
                res = max(res, r - l + 1)
    return res

print(longestSubstring("aaabb", 3))