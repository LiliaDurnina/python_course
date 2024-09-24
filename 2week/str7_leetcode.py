"""https://leetcode.com/problems/longest-valid-parentheses/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []
        curr = [0] * len(s)
        i = 0
        while i < len(s):
            if len(stack) == 0:
                stack.append(i)
            elif s[stack[-1]] + s[i] == "()":
                curr[stack[-1]] = 1
                curr[i] = 1
                stack.pop()
            else:
                stack.append(i)
            i += 1
        counter = 0
        for i in range(0, len(curr)):
            if curr[i] == 0:
                counter = 0
            else:
                curr[i] = counter + curr[i]
                counter += 1
        return max(curr)
