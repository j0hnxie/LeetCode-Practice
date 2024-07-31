class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}
        for time in times:
            src, dest, tim = time
            cur_adj = adj_list.get(src, [])
            cur_adj.append((tim, dest))
            adj_list[src] = cur_adj
        dist = [float('inf')] * (n + 1)
        dist[0] = 0
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            cur_dist, node = heapq.heappop(pq)
            adj = adj_list.get(node, [])

            for cur_adj in adj:
                path, next_node = cur_adj
                if dist[next_node] > cur_dist + path:
                    dist[next_node] = cur_dist + path
                    heapq.heappush(pq, (cur_dist + path, next_node))

        res = 0
        for num in dist:
            res = max(num, res)
        return res if res != float('inf') else -1