# We are given hours, a list of the number of hours worked per day for a given employee.
# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
# Return the length of the longest well-performing interval.
from typing import *

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # definitely some form of sliding interval
        # maybe DP??
        correlation = [-1 if hour <= 8 else 1 for hour in hours]
        # now we must find longest interval whose sum is >= 1
        # naive solution is n*n-1 for all combinations
        
        return 0