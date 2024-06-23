class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        idx1, idx2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        pq = [(nums1[idx1] + nums2[idx2], (idx1, idx2))]
        visited = set((idx1, idx2))
        res = []
        
        while k > 0 and pq:
            _, (idx1, idx2) = heapq.heappop(pq)
            res.append((nums1[idx1], nums2[idx2]))
            
            if idx1 + 1 < n1 and (idx1 + 1, idx2) not in visited:
                visited.add((idx1 + 1, idx2))
                heapq.heappush(pq, (nums1[idx1 + 1] + nums2[idx2], (idx1 + 1, idx2)))
                
            if idx2 + 1 < n2 and (idx1, idx2 + 1) not in visited:
                visited.add((idx1, idx2 + 1))
                heapq.heappush(pq, (nums1[idx1] + nums2[idx2 + 1], (idx1, idx2 + 1)))
            
            k -= 1
        return res
        