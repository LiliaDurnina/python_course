"""https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1484760371/?envType=problem-list-v2&envId=binary-tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[inorder_index + 1 :], postorder)

        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root
