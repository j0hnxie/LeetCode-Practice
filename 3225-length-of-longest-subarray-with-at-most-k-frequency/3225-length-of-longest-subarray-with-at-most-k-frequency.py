class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = 0
        current_num = 0
        counts = defaultdict(int)
        res = 0
        for l in range(n):
            while r < n:
                num = nums[r]
                counts[num] += 1
                if counts[num] > k:
                    counts[num] -= 1
                    break
                r += 1

            res = max(res, r - l)

            if r == n:
                break
            counts[nums[l]] -= 1
        return res
