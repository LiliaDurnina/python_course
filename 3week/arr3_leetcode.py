"""https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=array"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        response = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j != k and j < len(nums):
                # print(i, j, k)
                if nums[i] + nums[j] + nums[k] == 0:
                    response.append([nums[i], nums[j], +nums[k]])
                    j = j + 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return response
