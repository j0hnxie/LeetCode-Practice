class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums) / 2
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] > n:
                return i
        return -1