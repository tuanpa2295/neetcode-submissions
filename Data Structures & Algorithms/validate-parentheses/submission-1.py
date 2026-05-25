class Solution:
    def isValid(self, s: str) -> bool:
        seen = {"]": "[", ")": "(", "}": "{"}
        stack = []

        for c in s:
            if c in seen:
                if stack and seen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False