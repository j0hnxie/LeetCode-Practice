class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        memo = [[] for _ in range(n)]
        result = []

        for idx, num in enumerate(nums):
            for idx2 in range(idx):
                if num % nums[idx2] == 0:
                    if len(memo[idx2]) >= len(memo[idx]):
                        memo[idx] = memo[idx2].copy()

            memo[idx].append(num)
            if len(memo[idx]) > len(result):
                result = memo[idx].copy()
        
        # print(memo)
        return result
            