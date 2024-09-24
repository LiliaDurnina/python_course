""" https://leetcode.com/problems/zigzag-conversion/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        minus = 2
        for i in range(0, numRows):
            if numRows + numRows - 2 == 0 or len(s) < numRows:
                return s
            if i == numRows - 1 or i == 0:
                result += "".join(
                    [str(s[x]) for x in range(i, len(s), numRows + numRows - 2)]
                )
            else:
                x = i
                while x < len(s):
                    if x == i:
                        result += s[i]
                    else:
                        result += s[x - minus] + s[x]
                    x = x + numRows + numRows - 2
                if x >= len(s) and x - minus < len(s):
                    result += s[x - minus]
                minus += 2

        return result
