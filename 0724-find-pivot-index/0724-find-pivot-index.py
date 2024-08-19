class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        before = [0] * n
        after = [0] * n
        
        cur = 0
        for idx in range(n - 1, -1, -1):
            num = nums[idx]
            after[idx] = cur
            cur += num

        cur = 0
        for idx in range(n):
            num = nums[idx]
            before[idx] = cur
            cur += num

            if before[idx] == after[idx]:
                return idx
        


        return -1
        