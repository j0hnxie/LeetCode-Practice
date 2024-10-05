class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        memo = [False] * (target + 1)
        memo[0] = True
        for num in nums:
            for val in range(target, -1, -1):
                if num > val:
                    continue

                memo[val] = memo[val - num] or memo[val]
        # print(memo)
        return memo[target]