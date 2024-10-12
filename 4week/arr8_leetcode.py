"""https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=array"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        dict = {}
        appear = len(nums) / 3
        response = []
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1

        for k in dict.keys():
            if dict[k] > appear:
                response.append(k)
        print(response)
        return response
