def maxVowels(s: str, k: int) -> int:
    res = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    l,r = 0,0

    cur_vowels = 0
    while l < len(s) - k + 1:
        while r < l + k:
            cur_vowels += 1 if s[r] in vowels else 0
            r += 1
            res = max(cur_vowels, res)
        cur_vowels -= 1 if s[l] in vowels else 0
        l += 1
    return res

maxVowels("weallloveyou", 7)