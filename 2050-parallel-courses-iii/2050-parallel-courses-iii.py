class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {}
        indegrees = [0] * n
        
        for pre, post in relations:
            if pre - 1 in graph:
                graph[pre - 1].append(post - 1)
            else:
                graph[pre - 1] = [post - 1]
            indegrees[post - 1] += 1
            
        memo = [0] * n
        queue = deque()
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
            
        while queue:
            cur = queue.popleft()
            memo[cur] += time[cur]
            neighbors = graph.get(cur, [])
            for neighbor in neighbors:
                indegrees[neighbor] -= 1
                memo[neighbor] = max(memo[neighbor], memo[cur])
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
            
        return max(memo)