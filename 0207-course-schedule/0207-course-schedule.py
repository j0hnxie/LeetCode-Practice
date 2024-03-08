class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        visited = 0
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegree[cur] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                visited += 1
        
        while queue:
            cur = queue.popleft()
            
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    visited += 1
            
        
        return visited == numCourses