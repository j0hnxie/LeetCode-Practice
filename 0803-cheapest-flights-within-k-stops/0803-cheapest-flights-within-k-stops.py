class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for frm, to, price in flights:
            adj_list[frm].append((to, price))

        pq = [(0, 0, src)]
        seen = [float('inf')] * n
        dist[src] = 0

        while pq:
            dist_so_far, stops, node  = heapq.heappop(pq)

            if node == dst:
                return dist_so_far
            
            if stops > k or stops > seen[node]:
                continue

            seen[node] = stops
            
            for nex, price in adj_list[node]:
                heapq.heappush(pq, (dist_so_far + price, stops + 1, nex))

        return -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjs = [[] for i in range(n)]
        for flight in flights:
            # to dist
            adjs[flight[0]].append((flight[1], flight[2]))
            
        pq = []
        heapq.heappush(pq, (0, src, 0))
        stops = [float('inf') for i in range(n)]
        
        while pq:
            cur = heapq.heappop(pq)
            
            if cur[2] > k + 1 or cur[2] > stops[cur[1]]:
                continue
            
            stops[cur[1]] = cur[2]
                
            if cur[1] == dst:
                return cur[0]
            
            for adj in adjs[cur[1]]:
                heapq.heappush(pq, (adj[1] + cur[0], adj[0], cur[2] + 1))
        return -1
            