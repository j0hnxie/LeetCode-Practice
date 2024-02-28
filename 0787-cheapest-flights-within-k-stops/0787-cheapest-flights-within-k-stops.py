class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        dist[src] = 0
        
        for i in range(k + 1):
            temp = [dist[j] for j in range(n)]
            changed = False
            
            for flight in flights:
                if temp[flight[0]] != float('inf'):
                    dist[flight[1]] = min(dist[flight[1]], temp[flight[0]] + flight[2])
                    changed = True
            
            if not changed:
                break
        return dist[dst] if dist[dst] != float('inf') else -1
            
            