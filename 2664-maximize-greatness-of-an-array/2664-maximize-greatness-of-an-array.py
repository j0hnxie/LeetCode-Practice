class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        # lower, upper = sorted(nums), sorted(nums)

        upper_l, upper_r = 0, n - 1
        lower_l = 0
        result = 0
        while upper_l <= upper_r:
            upper_value, lower_value = nums[upper_l], nums[lower_l]
            if upper_value <= lower_value:
                upper_r -= 1
            else:
                result += 1
                upper_l += 1
            lower_l += 1

        return result