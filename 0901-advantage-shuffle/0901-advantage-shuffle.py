class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums = sorted(nums1)
        pq = [(-num, idx) for idx, num in enumerate(nums2)]
        heapq.heapify(pq)
        result = [-1] * n

        end = n - 1
        start = 0
        while pq:
            cur_num, cur_idx = heapq.heappop(pq)
            if -cur_num >= nums[end]:
                result[cur_idx] = nums[start]
                start += 1
            else:
                result[cur_idx] = nums[end]
                end -= 1

        
        return result
        
