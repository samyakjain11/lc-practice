from typing import *


def findTargetSumWays(self, nums: List[int], target: int) -> int:
    cache = {}
    def recursive_subproblem(index, cur_sum):

        # besides edge cases
        add = recursive_subproblem(index + 1, cur_sum + nums[index] )
        subtract = recursive_subproblem(index + 1, cur_sum - nums[index])
        res = sum(add, subtract)
        return res
    
    
    return 0