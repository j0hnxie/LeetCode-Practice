class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -1 * stone)
        
        while len(pq) > 1:
            large = heapq.heappop(pq)
            small = heapq.heappop(pq)
            if large != small:
                heapq.heappush(pq, large - small)
            
        return -1 * pq.pop() if pq else 0
        