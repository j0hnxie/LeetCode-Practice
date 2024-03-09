class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 1
        firstNeg = float('inf')
        maxLen = -1
        lastZero = -1
        
        for idx, num in enumerate(nums):
            prefix *= num
            if prefix < 0:
                if firstNeg == float('inf'):
                    firstNeg = idx
                curLen = idx - firstNeg
            elif prefix > 0:
                curLen = idx - lastZero
            else:
                lastZero = idx
                firstNeg = float('inf')
                prefix = 1
                curLen = 0
            
            maxLen = max(curLen, maxLen)
        
        
        return maxLen
            
        