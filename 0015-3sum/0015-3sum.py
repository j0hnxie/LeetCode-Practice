class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # nums.sort()
        result = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            complements = {}
            for j in range(i + 1, len(nums)):
                # if i == j:
                #     continue
                comp = target - nums[j]
                if comp in complements:
                    insertion = [nums[i], nums[j], nums[complements[comp]]]
                    insertion.sort()
                    final = tuple(insertion)
                    result.add(final)
                complements[nums[j]] = j
        return result