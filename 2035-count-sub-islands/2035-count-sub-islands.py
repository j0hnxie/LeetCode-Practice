class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0

        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    grid2[row][col] = 0
                    match = True
                    queue = deque([(row, col)])
                    while queue:
                        cur_x, cur_y = queue.popleft()

                        if grid1[cur_x][cur_y] == 0:
                            match = False

                        for dx, dy in dirs:
                            next_x, next_y = cur_x + dx, cur_y + dy

                            if next_x >= m or next_y >= n or next_x < 0 or next_y < 0:
                                continue

                            if grid2[next_x][next_y] == 1:
                                grid2[next_x][next_y] = 0
                                queue.append((next_x, next_y))
                    
                    if match:
                        # print(str(row) + " " + str(col))
                        res += 1
        return res