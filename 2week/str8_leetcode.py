"""https://leetcode.com/problems/count-and-say/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        curr_s = ""
        for i in range(1, n):
            x = 0
            counter = 0
            for y in range(0, len(s)):
                if s[x] == s[y]:

                    counter += 1
                else:
                    curr_s += str(counter) + s[x]
                    counter = 1
                    x = y
            s = curr_s + str(counter) + s[x]
            curr_s = ""
        return s
