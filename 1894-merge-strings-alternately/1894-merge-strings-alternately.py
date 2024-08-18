class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        n1, n2 = len(word1), len(word2)
        
        if n1 > n2:
            large = word1
            small = word2
        else:
            large = word2
            small = word1

        res = ""
        while idx < min(n1, n2):
            res += word1[idx]
            res += word2[idx]
            idx += 1
        
        res += large[idx:]
        return res