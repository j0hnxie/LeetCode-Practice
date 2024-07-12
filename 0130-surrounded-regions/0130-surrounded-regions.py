class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def bfs(x, y):
            board[x][y] = 'W'
            queue = deque([(x, y)])
            while queue:
                cur_x, cur_y = queue.popleft()
                
                for add_x, add_y in dirs:
                    nex_x = cur_x + add_x
                    nex_y = cur_y + add_y
                
                    if nex_x < 0 or nex_y < 0 or nex_x >= m or nex_y >= n:
                        continue
                    
                    if board[nex_x][nex_y] != 'O':
                        continue
                    
                    board[nex_x][nex_y] = 'W'
                    nex = (nex_x, nex_y)
                    queue.append(nex)
        
        for row in range(m):
            for col in range(n):
                if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                    if board[row][col] == 'O':
                        bfs(row, col)
        # print(board)
                        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        # print(board)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'W':
                    board[row][col] = 'O'
        