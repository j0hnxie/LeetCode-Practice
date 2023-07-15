class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def dfsHelper(graph, cur, visited, done):
            adjList = graph.get(cur, [])
            
            if cur in visited:
                return False
            
            if cur in done:
                return True
            
            visited.add(cur)
            done.add(cur)
            for adj in adjList:
                if not dfsHelper(graph, adj, visited, done):
                    return False
            visited.remove(cur)
            return True
            
        
        graph = {}
        for i in prerequisites:
            cur = graph.get(i[1], [])
            cur.append(i[0])
            graph[i[1]] = cur
            
        for node in graph:
            visit = set()
            done = set()
            if node not in done and not dfsHelper(graph, node, visit, done):
                return False
        
        return True
        
        