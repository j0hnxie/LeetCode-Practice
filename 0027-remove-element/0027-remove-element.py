class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        offset = 0
        start = 0
        for i in range(n):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        # print(start)
        return start