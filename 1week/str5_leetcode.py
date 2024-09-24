""" https://leetcode.com/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        p = ""
        for i in s:
            if i == " ":
                if len(p) != 0:
                    words.append(p)
                    p = ""
            else:
                p += i
        if p != "":
            words.append(p)
        words = [words[i] for i in range(len(words) - 1, -1, -1)]
        return " ".join(words)
