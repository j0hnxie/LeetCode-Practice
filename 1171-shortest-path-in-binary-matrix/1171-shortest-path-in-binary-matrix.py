class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        grid[0][0] = 1
        queue = deque([(0, 0)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        length = 1
        while queue:
            sz = len(queue)
            for _ in range(sz):
                cur_x, cur_y = queue.popleft()

                if cur_x == n - 1 and cur_y == n - 1:
                    return length
                
                for add_x, add_y in dirs:
                    new_x, new_y = cur_x + add_x, cur_y + add_y

                    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
                        continue

                    if grid[new_x][new_y] == 1:
                        continue

                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y))

            length += 1
        return -1