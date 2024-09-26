"""https://leetcode.com/problems/largest-time-for-given-digits/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD"""

from itertools import permutations as a


class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:

        hour = "-1"
        minute = "0"
        if min(arr) >= 3:
            return ""
        for x in a(str(str(arr[0]) + str(arr[1]) + str(arr[2]) + str(arr[3]))):
            s = "".join(x)
            if 0 <= int(s[0] + s[1]) <= 23 and 0 <= int(s[2] + s[3]) <= 59:
                if int(s[0] + s[1]) > int(hour):
                    hour, minute = s[0] + s[1], s[2] + s[3]
                if int(s[0] + s[1]) == int(hour) and int(s[2] + s[3]) >= int(minute):
                    hour, minute = s[0] + s[1], s[2] + s[3]
        if hour == "-1":
            return ""
        return hour + ":" + minute
