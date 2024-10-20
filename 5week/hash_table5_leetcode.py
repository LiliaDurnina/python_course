""" https://leetcode.com/problems/longest-consecutive-sequence/?envType=problem-list-v2&envId=hash-table"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        lg = 0
        for x in nums:
            if x - 1 not in nums:
                curr_x = x
                curr_lg = 1

                while curr_x + 1 in nums:
                    curr_x += 1
                    curr_lg += 1

                lg = max(lg, curr_lg)

        return lg
