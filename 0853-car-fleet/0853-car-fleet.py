class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:        
        n = len(position)
        pq = []
        res = [float('-inf')]
        
        for i in range(n):
            heapq.heappush(pq, (-1 * position[i], speed[i]))
        
        while pq:
            pos, spe = heapq.heappop(pq)
            pos *= -1
            time = (target - pos) / spe
            
            if time > res[-1]:
                res.append(time)
        
        return len(res) - 1