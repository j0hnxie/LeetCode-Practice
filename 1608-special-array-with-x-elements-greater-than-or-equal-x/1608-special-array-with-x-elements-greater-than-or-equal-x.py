class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [0] * (n + 1)
        
        for num in nums:
            for index in range(0, min(num, n) + 1):
                counts[index] += 1
        
        # print(counts)
        
        for count, idx in enumerate(counts):
            if count == idx:
                return idx
        
        return -1