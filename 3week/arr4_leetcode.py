""" https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=problem-list-v2&envId=array"""

from itertools import permutations as a


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        response = []
        for x in a(nums):
            response.append([i for i in x])
        print(response)
        return response
