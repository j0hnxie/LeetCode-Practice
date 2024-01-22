class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums2 = set()
        res = []
        maxNum = nums[0]
        for i in nums:
            if i in nums2:
                res.append(i)
            else:
                nums2.add(i)
            maxNum = max(maxNum, i)
            
        for i in range(1, maxNum):
            if i not in nums2:
                res.append(i)
        
        if len(res) == 1:
            res.append(maxNum + 1)
        
        return res