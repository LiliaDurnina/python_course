"""https://leetcode.com/problems/subarray-product-less-than-k/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        if k == 0 or k == 1:
            return 0
        if len(nums) < 2:
            if nums[0] < k:
                return 1
        response = 0
        i = 0
        j = 0
        curr = 1

        for i in range(len(nums)):
            curr = curr * nums[i]
            while curr >= k:
                curr = curr // nums[j]
                j += 1
            response += i - j + 1

        print(response)
        return response
