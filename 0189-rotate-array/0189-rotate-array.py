class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        temp = nums[n - k:]

        for idx in range(n - 1, k - 1, -1):
            nums[idx] = nums[idx - k]
        
        for idx in range(k):
            nums[idx] = temp[idx]