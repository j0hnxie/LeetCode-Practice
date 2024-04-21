class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {}
        
        for u, v in edges:
            cur_adj = adj.get(u, [])
            cur_adj.append(v)
            adj[u] = cur_adj
            
            cur_adj = adj.get(v, [])
            cur_adj.append(u)
            adj[v] = cur_adj
        
        stack = [source]
        visited = set(stack)
        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            
            neighs = adj.get(cur, [])
            for neigh in neighs:
                if neigh in visited:
                    continue
                
                visited.add(neigh)
                stack.append(neigh)
        
        return False