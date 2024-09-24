"""' https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenofstr = 0
        s1 = ""
        for i in s:
            if s1.find(i) == -1:
                s1 = s1 + i
                maxLenofstr = max(maxLenofstr, len(s1))
            else:
                s1 = s1[(s1.rfind(i) + 1) :] + i
                maxLenofstr = max(maxLenofstr, len(s1))
        return maxLenofstr
