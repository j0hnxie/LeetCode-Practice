class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sort = sorted(nums)
        
        total = 0
        operation = 0
        for num in sort:
            if num - total != 0:
                operation += 1
                total += num - total
            
        return operation