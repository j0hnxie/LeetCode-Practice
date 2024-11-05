class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = ""
        for char in s:
            if char == "(":
                stack.append("")
            elif char == ")":
                if stack:
                    current = stack.pop()
                    if stack:
                        stack[-1] += "(" + current + char
                    else:
                        result += "(" + current + char
            else:
                if not stack:
                    result += char
                else:
                    stack[-1] += char

        result += "".join(stack)
        return result