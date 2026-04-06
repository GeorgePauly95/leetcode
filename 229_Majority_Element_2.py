from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        results, output, n = {}, [], len(nums)
        for num in nums:
            if num not in results:
                results[num] = 1
            else:
                results[num] += 1
        for result in results:
            if results[result] > math.floor(n / 3):
                output.append(result)
        return output
