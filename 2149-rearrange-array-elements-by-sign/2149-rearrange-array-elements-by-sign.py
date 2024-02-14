class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos.popleft()
            else:
                nums[i] = neg.popleft()
        return nums