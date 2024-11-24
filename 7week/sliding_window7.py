"""https://leetcode.com/problems/find-the-k-beauty-of-a-number/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        response = 0

        for i in range(len(str(num)) - k + 1):
            stroka = str(num)[i : i + k]
            if int(stroka) != 0:
                if num % int(stroka) == 0:
                    response += 1

        return response
