class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            adj_list = {}
            indegrees = {}

            for edge in edges:
                first, second = edge
                cur_neighbors = adj_list.get(first, [])
                cur_neighbors.append(second)
                adj_list[first] = cur_neighbors
                indegrees[second] = indegrees.get(second, 0) + 1
            
            queue = deque()
            for node in range(1, k + 1):
                indegrees[node] = indegrees.get(node, 0)
                if indegrees[node] == 0:
                    queue.append(node)

            res = []
            while queue:
                cur_node = queue.popleft()
                res.append(cur_node)
                neighbor_nodes = adj_list.get(cur_node, [])

                for neighbor_node in neighbor_nodes:
                    indegrees[neighbor_node] = indegrees.get(neighbor_node, 0) - 1
                    if indegrees[neighbor_node] == 0:
                        queue.append(neighbor_node)
                        
            return res if len(res) == k else None

        
        res = [[0] * k for _ in range(k)]
        row_positions = topo_sort(rowConditions)
        col_positions = topo_sort(colConditions)

        if not row_positions or not col_positions:
            return []

        for x, row in enumerate(row_positions):
            for y, col in enumerate(col_positions):
                if row == col:
                    res[x][y] = row

        return res