class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        for start in range(n - len(needle) + 1):
            if haystack[start:start + len(needle)] == needle:
                return start
        return -1