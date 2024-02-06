class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            cur = counts.get(char, 0)
            cur += 1
            counts[char] = cur
        for index in range(len(s)):
            if counts[s[index]] == 1:
                return index
        return -1