"""https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        maxPalindrome = ""
        k = -1
        for i in s:
            k += 1
            s2 = s[k:]

            flag = 1
            while s2.rfind(i) != 0 and flag != 0:
                if s2[: s2.rfind(i) + 1] == s2[: s2.rfind(i) + 1][::-1]:
                    palindrome = s2[: s2.rfind(i) + 1]
                    flag = 0
                else:
                    s2 = s2[: s2.rfind(i)]
            if len(palindrome) > len(maxPalindrome):
                maxPalindrome = palindrome
        return maxPalindrome
