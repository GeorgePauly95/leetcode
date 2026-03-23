class Solution:
    def climbStairs(self, n: int, memo={1: 1, 2: 2}) -> int:
        if n not in memo.keys():
            memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]


# Time Complexity: O(n)
