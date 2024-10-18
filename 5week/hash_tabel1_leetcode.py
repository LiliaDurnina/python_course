"""https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table"""


class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        stroka = ""

        for i in dict.keys():
            ost = num // dict.get(i)
            num -= ost * dict.get(i)
            stroka += ost * i
            if num == 0:
                return stroka

        print(stroka)
        return stroka
