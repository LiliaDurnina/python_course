""" https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        listic = []
        fifo = []
        step = len(words[0])
        if len(words) * step > len(s):
            return []
        arr = []
        arr = [str(a) for a in s if a not in arr]
        if len(set(words)) == 1 and len(set(arr)) == 1 and words[0] == arr[0]:
            list = [int(x) for x in range(0, len(s) - step * len(words) + 1)]
            return list
        for i in range(0, len(s) - len(words) * step + 1):
            fifo = words.copy()
            for y in range(0, len(words)):
                start = i + step * y
                end = start + step
                if s[start:end] in fifo:
                    fifo.remove(s[start:end])
                else:
                    break
            if len(fifo) == 0:
                listic.append(i)
        return listic
