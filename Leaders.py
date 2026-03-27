class Solution:
    def leaders(self, arr):
        n, max = len(arr), 0
        result = []
        for i in range(n - 1, -1, -1):
            if arr[i] >= max:
                result.append(arr[i])
                max = arr[i]
        result.reverse()
        return result
