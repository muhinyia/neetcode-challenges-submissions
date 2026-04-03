class Solution:
    def isValid(self, s: str) -> bool:
        opening = "([{"
        hashMap = {")":"(", "]":"[", "}":"{"}
        stack = []
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    if hashMap[bracket] != stack[-1]:
                        return False
                    else:
                        stack.pop()

        return not stack