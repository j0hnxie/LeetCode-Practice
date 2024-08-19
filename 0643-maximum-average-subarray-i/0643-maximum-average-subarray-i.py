class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        total = sum(nums[:k])
        
        result = total / k
        for idx in range(k, n):
            prev_num = nums[idx - k]
            num = nums[idx]
            total += num
            total -= prev_num
            result = max(result, total / k)

        return result
