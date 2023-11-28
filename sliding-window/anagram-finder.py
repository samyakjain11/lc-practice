from typing import List

def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        
        res = []
        letters_unfulfilled = list(p)
        indices_for_fulfilled_letters = set()

        l = 0
        for r in range(len(s)):
            if r - l + 1 > len(p):
                if l in indices_for_fulfilled_letters:
                    letters_unfulfilled.append(s[l])
                l += 1
            if s[r] in p and s[r] in letters_unfulfilled:
                letters_unfulfilled.remove(s[r]) 
                indices_for_fulfilled_letters.add(r)
                if len(letters_unfulfilled) == 0:
                    res.append(l)
        return res