"""https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:

        n = len(nums)
        left = 0
        count = 0
        freq = {}
        cur = 0
        for right in range(n):
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1
            cur += freq[nums[right]] - 1
            while cur >= k:
                count += n - right
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                cur -= freq.get(nums[left], 0)
                left += 1

        return count


# print(count_good_subarrays([3, 1, 4, 3, 2, 2, 4], 2))
