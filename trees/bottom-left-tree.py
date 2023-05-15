# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def wrapper(curDepth, root) -> tuple(int, int):
            
        return 0