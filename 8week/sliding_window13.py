""" https://leetcode.com/problems/longest-harmonious-subsequence/?envType=problem-list-v2&envId=sliding-window  """


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        max_len = 0

        for key in dict:
            if key + 1 in dict:
                len = dict[key] + dict[key + 1]
                max_len = max(max_len, len)

        return max_len
