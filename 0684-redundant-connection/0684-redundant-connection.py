class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU():
            def __init__(self):
                self.rank = [0] * 1001
                self.parent = [node for node in range(1001)]

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                elif self.rank[px] < self.rank[py]:
                    self.parent[py] = px
                    self.rank[px] += 1
                else:
                    self.parent[px] = py
                    self.rank[py] += 1
                return True
        
        dsu = DSU()
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        return [-1, -1]