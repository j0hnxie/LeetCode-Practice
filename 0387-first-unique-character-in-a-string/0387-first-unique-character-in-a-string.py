class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0 for i in range(26)]
        for char in s:
            counts[ord(char) - 97] += 1
        for index in range(len(s)):
            if counts[ord(s[index]) - 97] == 1:
                return index
        return -1