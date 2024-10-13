"""https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=array"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def f(nums, k):
            if len(nums) == 1:
                return nums[0]
            less = [int(x) for x in nums if x < nums[len(nums) // 2]]

            equal = [int(x) for x in nums if x == nums[len(nums) // 2]]

            more = [int(x) for x in nums if x > nums[len(nums) // 2]]

            if k <= len(more):

                return f(more, k)
            if len(more) < k <= len(equal) + len(more):
                return equal[0]

            return f(less, k - (len(more) + len(equal)))

        return f(nums, k)
