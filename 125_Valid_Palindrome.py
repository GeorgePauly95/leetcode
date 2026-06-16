class Solution:
    def isPalindrome(self, s: str) -> bool:
        transformed_s = list(s.lower())
        for i in range(len(transformed_s)):
            if transformed_s[i].isalnum() is False:
                transformed_s[i] = None
        result = [letter for letter in transformed_s if letter is not None]
        print("result:", result)
        n = len(result)
        for i in range(n):
            if result[i] != result[n - 1 - i]:
                return False
        return True


class PythonicSolution:
    def isPalindrome(self, s: str) -> bool:
        transformed_s = "".join(char.lower() for char in s if char.isalnum() is True)
        n = len(transformed_s)
        left, right = 0, n - 1
        while left < right:
            if transformed_s[left] != transformed_s[right]:
                return False
            left += 1
            right -= 1
        return True
