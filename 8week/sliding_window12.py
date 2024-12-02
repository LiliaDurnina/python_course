"""https://leetcode.com/problems/longest-repeating-character-replacement/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        max_count = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            dict[s[right]] = dict.get(s[right], 0) + 1
            max_count = max(max_count, dict[s[right]])
            while (right - left + 1) - max_count > k:
                dict[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
