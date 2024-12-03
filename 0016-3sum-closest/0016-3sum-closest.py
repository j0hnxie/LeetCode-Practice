class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        print(nums)

        res, diff = float('inf'), float('inf')
        for idx in range(n):
            l, r = idx + 1, n - 1
            while l < r:
                cur = nums[idx] + nums[l] + nums[r]
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return target

                if abs(target - cur) < diff:
                    diff = abs(target - cur)
                    res = cur

        return res