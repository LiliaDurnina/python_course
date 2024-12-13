"""'https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for node in range(2, n + 1):
            for root in range(1, node + 1):
                left = dp[root - 1]
                right = dp[node - root]
                dp[node] += left * right

        return dp[n]
