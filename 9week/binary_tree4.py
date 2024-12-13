"""https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=problem-list-v2&envId=binary-tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def flatten_tree(node):
            if not node:
                return None
            left = node.left
            right = node.right
            if left:
                flatten_tree(left)
            if right:
                flatten_tree(right)
            node.left = None
            node.right = left
            cur = node
            while cur.right:
                cur = cur.right

            cur.right = right

        flatten_tree(root)
