class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        class DSU():
            def __init__(self, nodes):
                self.parent = list(range(nodes))
                self.rank = [0] * nodes
            
            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                elif self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                else:
                    self.parent[px] = py
                    if self.rank[px] == self.rank[py]:
                        self.rank[py] += 1
        
        dsu = DSU(len(vals))
        # organize nodes by value number
        val_counts = defaultdict(list)
        for idx, val in enumerate(vals):
            val_counts[val].append(idx)
        
        val_list = [(key, item) for key, item in val_counts.items()]
        val_list.sort()

        # create adj list
        adj_list = defaultdict(list)
        for a, b in edges:
            if vals[a] >= vals[b]:
                adj_list[a].append(b)
            if vals[b] >= vals[a]:
                adj_list[b].append(a)
        
        res = len(vals)
        for val, nodes in val_list:
            # union node with neighbors <= itself
            for node in nodes:
                for neighbor in adj_list[node]:
                    dsu.union(node, neighbor)
            
            # count number of nodes in each component
            parent_count = defaultdict(int)
            for node in nodes:
                parent_count[dsu.find(node)] += 1
            
            # add n * (n - 1) / 2 good paths for each component
            for parent, n in parent_count.items():
                res += n * (n - 1) // 2
            
        return res