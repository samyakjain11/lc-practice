from typing import *

def totalFruit(self, fruits: List[int]) -> int:
    seen = set()
    last_index = {}
    res = 0

    l = 0
    
    for r in range(len(fruits)):
        if len(seen) <= 1:
            seen.add(fruits[r])
            last_index[fruits[r]] = r
            res = max(res, r - l + 1)
        elif fruits[r] in seen:
            last_index[fruits[r]] = r
            res = max(res, r - l + 1)
        else:
            # we actually have to do some things
            # first find the minimum last_index- DONE
            # next move the left pointer to last index= DONE
            # then find the fruit to remove- DONE
            # add the new fruit- DONE
            seen_list = list(seen)
            min_ind = min(last_index[seen_list[0]], last_index[seen_list[1]])
            l = min_ind + 1
            seen.remove(fruits[min_ind])
            seen.add(fruits[r])
            last_index[fruits[r]] = r
            res = max(res, r - l + 1)
    
    return res