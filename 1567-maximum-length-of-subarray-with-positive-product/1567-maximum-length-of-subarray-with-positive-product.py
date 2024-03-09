class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 1
        firstNeg = -1
        maxLen = 0
        lastZero = -1
        
        for idx, num in enumerate(nums):
            curLen = 0
            prefix *= num
            if prefix < 0:
                if firstNeg == -1:
                    firstNeg = idx
                    curLen = -1
                else:
                    curLen = idx - firstNeg
            elif prefix > 0:
                curLen = idx - lastZero
            else:
                lastZero = idx
                firstNeg = -1
                prefix = 1
                curLen = 0
            
            maxLen = max(curLen, maxLen)
        
        
        return maxLen
            
        