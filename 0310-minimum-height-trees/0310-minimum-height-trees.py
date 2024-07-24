class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [node for node in range(n)]

        adj_list = [set() for node in range(n)]

        for edge in edges:
            a, b = edge
            adj_list[a].add(b)
            adj_list[b].add(a)

        cur_leaves = []
        for node in range(n):
            if len(adj_list[node]) == 1:
                cur_leaves.append(node)
        
        remaining = n
        while remaining > 2:
            remaining -= len(cur_leaves)
            next_leaves = []
            while cur_leaves:
                cur_node = cur_leaves.pop()
                
                for neighbor in adj_list[cur_node]:
                    adj_list[neighbor].remove(cur_node)
                    if len(adj_list[neighbor]) == 1:
                        next_leaves.append(neighbor)
            cur_leaves = next_leaves
        return cur_leaves
        
            

        