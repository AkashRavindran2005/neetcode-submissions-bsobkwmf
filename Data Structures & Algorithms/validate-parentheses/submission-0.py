class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seen = {")":"(" , "}":"{", "]":"["}
        for i in s:
            if i in seen:
                if stack and stack[-1] == seen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False