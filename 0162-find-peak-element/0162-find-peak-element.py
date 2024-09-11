class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        def isPeak(idx):
            if idx == 0:
                if nums[1] < nums[0]:
                    return 0
                else:
                    return 1
            elif idx == n - 1:
                if nums[-1] > nums[-2]:
                    return 0
                else:
                    return -1
            else:
                if nums[idx] <= nums[idx - 1]:
                    return -1
                elif nums[idx] <= nums[idx + 1]:
                    return 1
                else:
                    return 0

        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            movement = isPeak(m)
            # print(movement)
            if movement < 0:
                r = m - 1
            elif movement > 0:
                l = m + 1
            else:
                return m
        return -1