class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = defaultdict(set)
        for idx, num in enumerate(arr):
            nums[num].add(idx)
        
        for idx, num in enumerate(arr):
            if len(nums[num * 2]) != 0:
                if len(nums[num * 2]) == 1 and idx in nums[num * 2]:
                    continue
                return True

            if (num % 2 == 0 and len(nums[num // 2]) != 0):
                if len(nums[num // 2]) == 1 and idx in nums[num // 2]:
                    continue
                return True
        return False