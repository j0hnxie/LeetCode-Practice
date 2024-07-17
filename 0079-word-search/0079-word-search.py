class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index):
            # print(x, y)
            
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            
            if board[x][y] != word[index]:
                return False
            elif index == len(word) - 1:
                return True
            
            # print(x, y, index)
            visited.add((x, y))
            final = False
            for i, j in self.dirs:
                newX = x + i
                newY = y + j
                
                if (newX, newY) in visited:
                    continue
                
                if dfs(newX, newY, index + 1):
                    final = True
                    break
            visited.remove((x, y))
            return final
            
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
        