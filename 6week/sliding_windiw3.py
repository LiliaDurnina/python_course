"""https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        if len(p) > len(s):
            return []
        str = ""
        listic = []

        p = sorted(p)
        print(p)

        for i in range(0, len(s) - len(p) + 1):

            str = sorted(s[i : i + len(p)])

            if str == p:
                listic.append(i)
        return listic
