"""https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=binary-tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, curPath, curSum):
            if not node:
                return
            curPath.append(node.val)
            curSum += node.val
            if not node.left and not node.right and curSum == targetSum:
                result.append(list(curPath))
            dfs(node.left, curPath, curSum)
            dfs(node.right, curPath, curSum)
            curPath.pop()

        dfs(root, [], 0)
        return result
