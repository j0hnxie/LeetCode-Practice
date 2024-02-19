class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        pq = []
        for key, value in counts.items():
            heapq.heappush(pq, (value * -1, key))
        
        res = []
        for i in range(k):
            top = heapq.heappop(pq)
            res.append(top[1])
        
        return res