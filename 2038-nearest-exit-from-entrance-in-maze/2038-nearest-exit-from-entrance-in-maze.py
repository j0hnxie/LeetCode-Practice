class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = set([(entrance[0], entrance[1])])
        queue = deque([(entrance[0], entrance[1])])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        distance = 0

        while queue:
            sz = len(queue)
            for _ in range(sz):
                cur_x, cur_y = queue.popleft()

                for dx, dy in dirs:
                    nex_x = cur_x + dx
                    nex_y = cur_y + dy

                    if nex_x < 0 or nex_x >= m or nex_y < 0 or nex_y >= n:
                        if distance != 0:
                            return distance
                        continue

                    if maze[nex_x][nex_y] == "+":
                        continue
                    
                    if (nex_x, nex_y) in visited:
                        continue

                    visited.add((nex_x, nex_y))
                    queue.append((nex_x, nex_y))
            distance += 1
        return -1