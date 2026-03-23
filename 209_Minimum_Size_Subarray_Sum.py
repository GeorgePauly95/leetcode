from typing import List


class BruteforceSolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        lengths = []
        for i in range(0, n):
            for j in range(i, n):
                if sum(nums[i : j + 1]) >= target:
                    lengths.append(len(nums[i : j + 1]))
                    break
        if len(lengths) == 0:
            return 0
        return min(lengths)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_pointer = 0
        result = 10**10
        window_sum = 0
        for right_pointer in range(0, len(nums)):
            window_sum += nums[right_pointer]

            while window_sum >= target:
                result = min(result, right_pointer - left_pointer + 1)
                window_sum -= nums[left_pointer]
                left_pointer += 1
        if result == 10**10:
            return 0
        return result
