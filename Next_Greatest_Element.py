from typing import List


def next_greater_element(nums: List(int)):
    n = len(nums)
    result, stack = [-1] * n, []
    for i in range(n):
        while len(stack) != 0 and nums[i] >= nums[stack[-1]]:
            index = stack.pop(-1)
            result[index] = nums[i]
        stack.append(i)
    return result
