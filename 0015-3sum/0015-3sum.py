class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        prev = "A"
        idx = 0
        res = []

        while idx < n:
            num = nums[idx]
            if num == prev:
                idx += 1
                continue
              
            if num > 0:
                break

            l, r = idx + 1, n - 1
            while l < r:
                if nums[l] + nums[r] + num == 0:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    r -= 1
            prev = num
            idx += 1
        return res