"""https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        odd = 0
        count_k = 0
        less_k = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odd += 1

            while odd > k:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1

            less_k += r - left + 1

        odd = 0
        left = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odd += 1

            while odd > k - 1:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1

            count_k += r - left + 1

        return less_k - count_k
