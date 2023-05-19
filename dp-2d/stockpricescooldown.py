from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def subproblem(index, buying):
            if index >= len(prices):
                return 0

            if (index, buying) in cache:
                return cache[(index, buying)]

            hold = subproblem(index + 1, buying)
            if buying:
                buy = subproblem(index + 1, not buying) - prices[index]
                cache[(index, buying)] = max(buy, hold)
            else:
                sell = subproblem(index + 2, not buying) + prices[index]
                cache[(index, buying)] = max(sell, hold)
            return cache[(index, buying)]

        return subproblem(0, True)
            