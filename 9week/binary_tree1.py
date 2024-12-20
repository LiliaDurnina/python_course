"""https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=problem-list-v2&envId=binary-tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)

        return 1 + max(left_d, right_d)
