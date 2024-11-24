"""https://leetcode.com/problems/minimum-window-substring/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        length = len(dict_t)

        l, r = 0, 0
        window_counts = {}

        min_len = len(s) + 1
        min_left, min_right = 0, 0

        f = 0

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                f += 1

            while l <= r and f == length:
                char = s[l]

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left, min_right = l, r + 1

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    f -= 1

                l += 1

            r += 1
        if min_len != len(s) + 1:
            return s[min_left:min_right]
        else:
            return ""
