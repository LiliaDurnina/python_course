"""https://leetcode.com/problems/basic-calculator-ii/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""

"""обратная польская"""


class Solution:
    def calculate(self, s: str) -> int:
        cache = []
        new = ""
        for i in s:
            if i in "*/":
                new += "$"
                if len(cache) != 0 and cache[-1] in "*/":
                    new += cache[-1]
                    cache.pop()
                cache.append(i)
            elif i in "+-":
                new += "$"
                while len(cache) > 0:
                    new += cache[-1]
                    cache.pop()
                cache.append(i)
            elif i != " ":
                new += i
        new += "$"
        new += "".join([str(cache[x]) for x in range(len(cache) - 1, -1, -1)])
        # print(f"polish entry: {new}")
        cache = []
        atoi = ""
        for i in new:
            if i in "+*-/":
                if i == "+":
                    counter = cache[-1] + cache[-2]
                elif i == "-":
                    counter = cache[-2] - cache[-1]
                elif i == "/":
                    counter = cache[-2] // cache[-1]
                elif i == "*":
                    counter = cache[-2] * cache[-1]
                cache.pop()
                cache.pop()
                cache.append(counter)
            elif i == "$":
                cache.append(int(atoi))
                atoi = ""
            else:
                atoi += i

        return cache[0]
