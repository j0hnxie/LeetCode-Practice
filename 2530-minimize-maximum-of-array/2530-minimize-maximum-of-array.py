class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = sum(nums) // n, max(nums)

        def isPossible(m):
            carry = 0
            for idx in range(n - 1, 0, -1):
                num = nums[idx] + carry
                carry = max(num - m, 0)

            return carry + nums[0] <= m

        while l < r:
            m = l + (r - l) // 2
            if isPossible(m):
                r = m
            else:
                l = m + 1

        return r