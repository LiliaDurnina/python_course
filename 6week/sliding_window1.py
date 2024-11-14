"""'https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 1
        str = s[i]
        maxStr = ""
        while j < len(s):
            if s[j] in str:
                if len(maxStr) < len(str):
                    maxStr = str
                i = str.find(s[j]) + 1
                str = str[i:]

            str += s[j]
            # print(i, str)
            j += 1
        if len(maxStr) < len(str):
            maxStr = str
        return len(maxStr)
