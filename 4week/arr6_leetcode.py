"""https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=array"""


class Solution:
    def countPrimes(self, n: int) -> int:

        a = [int(x) for x in range(0, n)]
        if n <= 1:
            return 0

        for i in range(2, len(a)):
            if a[i] != 0:

                for x in range(i * i, len(a), i):
                    a[x] = 0

        return len([x for x in a if x != 0]) - 1
