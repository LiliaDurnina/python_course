""" https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        response = 0
        n = len(arr)

        if n < k:
            return 0
        su_m = sum(arr[0:k])
        if su_m / k >= threshold:
            response += 1
        for i in range(k, n):
            su_m = su_m - arr[i - k] + arr[i]
            if su_m / k >= threshold:
                response += 1

        return response
