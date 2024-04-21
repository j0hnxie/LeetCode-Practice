class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (n + 1)
        memo[1] = 1
        
        for idx in range(1, n + 1):
            max_length = 0
            for idx2 in range(idx):
                if nums[idx2 - 1] < nums[idx - 1]:
                    max_length = max(max_length, memo[idx2])
            memo[idx] = max_length + 1
        # print(memo)
        return max(memo)