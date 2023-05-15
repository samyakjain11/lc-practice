# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findHeight(root):
            if not root:
                return 0
            else:
                return 1 + max(findHeight(root.right), findHeight(root.left))
            
        return findHeight(root)