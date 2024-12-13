"""https://leetcode.com/problems/binary-tree-right-side-view/?envType=problem-list-v2&envId=binary-tree"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        right_view = []
        que = deque([root])
        while que:
            level_length = len(que)
            for i in range(level_length):
                node = que.popleft()
                if i == level_length - 1:
                    right_view.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return right_view
