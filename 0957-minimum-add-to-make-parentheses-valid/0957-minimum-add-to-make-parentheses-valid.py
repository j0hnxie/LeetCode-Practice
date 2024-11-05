class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        result = 0
        for char in s:
            if char == "(":
                opened += 1
            elif char == ")":
                if not opened:
                    result += 1
                else:
                    opened -= 1
        result += opened
        return result