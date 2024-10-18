class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "-",
        }
        arr = []
        if digits == "":
            return []
        while len(digits) < 4:
            digits += "0"

        for x0 in dict.get(digits[0]):

            for x1 in dict.get(digits[1]):
                for x2 in dict.get(digits[2]):
                    for x3 in dict.get(digits[3]):
                        s = x0 + x1 + x2 + x3
                        s = s.replace("-", "")
                        arr += [s]

        return arr
