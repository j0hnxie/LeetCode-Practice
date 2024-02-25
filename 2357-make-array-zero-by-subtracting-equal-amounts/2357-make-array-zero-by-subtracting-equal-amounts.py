class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set(nums)
        
        unique.add(0)
        unique.remove(0)
        
        return len(unique)