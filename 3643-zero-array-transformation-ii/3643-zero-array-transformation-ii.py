class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        result = 0
        cur = 0
        boundaries = [0] * (n + 1)
        for idx, num in enumerate(nums):
            while cur + boundaries[idx] < num:
                if result == len(queries):
                    return -1

                left, right, val = queries[result]

                if right >= idx:
                    boundaries[max(left, idx)] += val
                    boundaries[right + 1] -= val

                result += 1
            cur += boundaries[idx]
        
        return result
