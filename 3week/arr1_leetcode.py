""" https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=array"""


def firstMissingPositive(nums: list[int]) -> int:
    nums = sorted([x for x in nums if x >= 1])
    print(nums)
    if len(nums) == 0 or nums[0] != 1:
        return 1

    for i in range(0, len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            return nums[i] + 1
    return nums[-1] + 1


print(firstMissingPositive([0, 2, 2, 1, 1]))
