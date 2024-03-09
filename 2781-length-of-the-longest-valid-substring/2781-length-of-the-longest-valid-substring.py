class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        no = set(forbidden)

        r = 0
        l = 0
        n = len(word)
        maxLen = 0
        while r <= n:
            valid = False
            while not valid:
                valid = True
                for i in range(max(r - 10, l), r):
                    if word[i:r] in no:
                        valid = False
                        l += 1
                        break
                
            maxLen = max(maxLen, r - l)
            r += 1
        return maxLen
        
        