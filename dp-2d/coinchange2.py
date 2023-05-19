    
from typing import *

def change(amount: int, coins: List[int]) -> int:
    cache = {}
    combs_found = set()
    def subproblem(leftover, building_comb):
        print(leftover)
        if leftover < 0:
            return 0

        if leftover == 0:
            if str(sorted(building_comb)) not in combs_found:
                combs_found.add(str(sorted(building_comb)))
                return 1
            else:
                return 0
        
        if leftover in cache:
            return cache[leftover]
        
        res = 0
        for coin in coins:
            if coin <= leftover:
                building_comb.append(coin)
                res += subproblem(leftover - coin, building_comb.copy())
                building_comb.remove(coin)
        
        cache[leftover] = res
        return res
    
    return subproblem(amount, [])

print(change(5, [1,2,5]))