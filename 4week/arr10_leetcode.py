"""https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=array"""

from itertools import permutations as a


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        response = []
        for x in a(nums):
            if [i for i in x] not in response:
                response.append([i for i in x])
        print(response)
        return response
