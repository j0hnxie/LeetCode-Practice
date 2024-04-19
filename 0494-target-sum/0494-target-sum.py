class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)
        cur = [0] * (2 * tot + 1)
        prev = [0] * (2 * tot + 1)
        prev[tot + nums[0]] = 1
        prev[tot - nums[0]] += 1
        for idx in range(1, n):
            for tar in range(-tot, tot + 1):
                new_tar = tar + tot
                if prev[new_tar] > 0:
                    cur[new_tar + nums[idx]] += prev[new_tar]
                    cur[new_tar - nums[idx]] += prev[new_tar]
            prev = cur
            cur = [0] * (2 * tot + 1)
        return prev[target + tot] if abs(target) <= tot else 0