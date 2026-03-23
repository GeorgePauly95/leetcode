class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in map and map[other_num] != i:
                return [i, map[other_num]]


# Time Complexity: O(n)
