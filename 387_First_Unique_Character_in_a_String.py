class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = {}
        for c in s:
            if c not in result:
                result[c] = 1
            else:
                result[c] += 1
        for i in range(len(s)):
            if result[s[i]] == 1:
                return i
        return -1
