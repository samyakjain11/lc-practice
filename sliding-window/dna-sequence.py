from typing import *

def findRepeatedDnaSequences(s: str) -> List[str]:
    seen_sequences = set()
    res = set()

    s_len = len(s)
    if s_len <= 10:
        return []
    
    for l in range(s_len - 9):
        r = l + 10
        # sequence is actually [l, r - 1] since last index excluded
        cur_sequence = s[l : r]
        if cur_sequence in seen_sequences:
            res.add(cur_sequence)
        else:
            seen_sequences.add(cur_sequence)

    return list(res)

findRepeatedDnaSequences("AAAAAAAAAAA")