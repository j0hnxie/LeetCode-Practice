class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        end_at_one, end_at_two = [1] * n, [1] * n
        res = 1

        for idx in range(1, n):
            if nums1[idx] >= nums1[idx - 1]:
                end_at_one[idx] = max(end_at_one[idx], end_at_one[idx - 1] + 1)
            
            if nums1[idx] >= nums2[idx - 1]:
                end_at_one[idx] = max(end_at_one[idx], end_at_two[idx - 1] + 1)
            
            if nums2[idx] >= nums1[idx - 1]:
                end_at_two[idx] = max(end_at_two[idx], end_at_one[idx - 1] + 1)

            if nums2[idx] >= nums2[idx - 1]:
                end_at_two[idx] = max(end_at_two[idx], end_at_two[idx - 1] + 1)
            
            res = max(res, max(end_at_one[idx], end_at_two[idx]))
            
        return res