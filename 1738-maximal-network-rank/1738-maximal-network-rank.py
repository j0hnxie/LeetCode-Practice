class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]

        for road in roads:
            a, b = road
            adj[a].add(b)
            adj[b].add(a)
        
        maxRank = 0
        for a in range(n):
            curRank = 0
            for b in range(a + 1, n):
                curRank = len(adj[a]) + len(adj[b])
                curRank -= 1 if b in adj[a] else 0
                maxRank = max(maxRank, curRank)
        return maxRank


        
        

