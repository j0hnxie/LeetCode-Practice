class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def testPalindrome(i, j):
            count = 0
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    return count
                i -= 1
                j += 1
                count += 1
            return count
        
        res = 0
        for i in range(n):
            res += testPalindrome(i, i)
            res += testPalindrome(i, i + 1)
        return res
            