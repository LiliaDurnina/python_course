""" https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict = {}

        for i, num in enumerate(nums):
            if num in dict:
                if abs(i - dict[num]) <= k:
                    return True
            dict[num] = i

        return False
