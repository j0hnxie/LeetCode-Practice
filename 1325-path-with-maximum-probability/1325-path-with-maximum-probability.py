class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distance = [float('-inf')] * n
        distance[start_node] = 0

        adj_list = defaultdict(list)
        for idx, (src, dest) in enumerate(edges):
            succ = succProb[idx]
            adj_list[src].append((dest, succ))
            adj_list[dest].append((src, succ))

        pq = [(-1, start_node, -1)]
        while pq:
            dist, current, prev = heapq.heappop(pq)
            dist *= -1
            if current == end_node:
                return dist
            elif dist < distance[current]:
                continue

            for neighbor, prob in adj_list[current]:
                if neighbor == prev:
                    continue

                new_dist = dist * prob
                if new_dist > distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (-new_dist, neighbor, current))
        
        return 0 if distance[end_node] == float('-inf') else distance[end_node]



