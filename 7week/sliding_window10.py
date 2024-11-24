""" https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        n = len(nums)
        left = 0
        current_sum = 0
        min_len = 1000000
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if min_len != 1000000:
            return min_len
        else:
            return 0
