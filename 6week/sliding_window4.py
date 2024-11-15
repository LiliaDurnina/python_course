"""https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        if len(nums) <= 2:
            return 0
        i = 0
        j = 1
        dif = nums[j] - nums[i]
        j = 2
        cur = 2
        response = 0

        while j < len(nums):
            if nums[j] - nums[j - 1] == dif:
                cur += 1
            else:
                if cur > 2:
                    response += sum(cur - x for x in range(2, cur + 1))
                cur = 2
                dif = nums[j] - nums[j - 1]
            j += 1
        if cur > 2:
            response += sum(cur - x for x in range(2, cur))
        print(response)
        return response
