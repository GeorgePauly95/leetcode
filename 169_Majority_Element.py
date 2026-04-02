from typing import List


class HashMapSolution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        print(counts)
        max_count, max_num = 0, 1
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                max_num = num
        return max_num


class BoyerMooreSolution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            elif candidate != num:
                count -= 1
        return candidate
