from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for root_pointer in range(n):
            # if two root pointers are the same then the second one can be ignored
            if root_pointer > 0 and nums[root_pointer] == nums[root_pointer - 1]:
                continue
            left_pointer = root_pointer + 1
            right_pointer = n - 1
            while left_pointer < right_pointer:
                total = nums[root_pointer] + nums[left_pointer] + nums[right_pointer]
                if total < 0:
                    left_pointer += 1
                elif total > 0:
                    right_pointer -= 1
                else:
                    result.append(
                        [nums[root_pointer], nums[left_pointer], nums[right_pointer]]
                    )
                    # if a triplet is found, then duplicates for the left pointer and the right pointer each
                    # can be checked for
                    while (
                        left_pointer < right_pointer
                        and nums[left_pointer] == nums[left_pointer + 1]
                    ):
                        left_pointer += 1
                    while (
                        left_pointer < right_pointer
                        and nums[right_pointer] == nums[right_pointer - 1]
                    ):
                        right_pointer -= 1

                    left_pointer += 1
                    right_pointer -= 1
        return result
