class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        cur = set()
        n = len(s)
        start = 0
        res = 0
        
        for i in range(n):
            while s[i] in cur:
                cur.remove(s[start])
                start += 1
            cur.add(s[i])
            res = max(len(cur), res)
        return res