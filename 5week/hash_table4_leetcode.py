"""https://leetcode.com/problems/top-k-frequent-elements/?envType=problem-list-v2&envId=hash-table"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        dict = {}
        arr = []
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        p = sorted([dict.get(x) for x in dict.keys()])[::-1]
        p = p[0:k]
        for i in dict.keys():
            if dict.get(i) in p:
                k -= 1
                arr.append(i)
            if k == 0:
                break
        print(arr)
        return arr
