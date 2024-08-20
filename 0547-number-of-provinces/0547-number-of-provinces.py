class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for adj in range(n):
                if isConnected[node][adj]:
                    if adj not in visited:
                        visited.add(adj)
                        dfs(adj)

        n = len(isConnected)
        visited = set()
        res = 0

        for node in range(n):
            if node not in visited:
                res += 1
                visited.add(node)
                dfs(node)
        
        return res
