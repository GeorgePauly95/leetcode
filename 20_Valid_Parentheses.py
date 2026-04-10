class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
