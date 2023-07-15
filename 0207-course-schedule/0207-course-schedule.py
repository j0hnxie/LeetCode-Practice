class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def dfs(cur):
            if visited[cur] == -1:
                return False
            elif visited[cur] == 1:
                return True
            
            visited[cur] = -1
            for i in graph[cur]:
                if not dfs(i):
                    return False
                
            visited[cur] = 1
            return True
                
        
        visited = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        