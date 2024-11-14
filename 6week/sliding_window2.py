""" https://leetcode.com/problems/repeated-dna-sequences/solutions/3268539/c-faster-than-75-sliding-window/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        listic = []
        str = ""
        dict = {}
        for i in range(0, len(s) - 9):
            str = s[i : i + 10]
            if str not in dict.keys():
                dict[str] = 1
            else:
                dict[str] += 1
        for key in dict.keys():
            if dict[key] >= 2:
                listic.append(key)
        print(listic)
        return listic
