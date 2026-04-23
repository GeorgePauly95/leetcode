from typing import List


class LinearSpaceSolution:
    def missingNumber(self, nums: List[int]) -> int | None:
        n = len(nums)
        result = list(range(0, n + 1))
        for num in nums:
            result[num] = -1
        for candidate in result:
            if candidate != -1:
                return candidate
