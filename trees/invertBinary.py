# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if root:
                root.right, root.left = root.left, root.right
                helper(root.right)
                helper(root.left)
        
        helper(root)
        return root