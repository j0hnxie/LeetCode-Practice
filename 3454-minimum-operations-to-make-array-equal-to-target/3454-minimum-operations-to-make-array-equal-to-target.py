class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        prev_diff = target[0] - nums[0]
        res = abs(prev_diff)
        n = len(nums)

        for idx in range(1, n):
            num = nums[idx]
            cur_target = target[idx]
            diff = cur_target - num

            if diff > 0:
                if prev_diff > 0:
                    res += max(diff - prev_diff, 0)
                else:
                    res += diff
            elif diff < 0:
                if prev_diff < 0:
                    res += max(prev_diff - diff, 0)
                else:
                    res += abs(diff)
            prev_diff = diff
        return res


