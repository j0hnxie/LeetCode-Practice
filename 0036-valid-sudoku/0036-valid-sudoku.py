class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cur = board[i][j]
                    row = str(cur) + str(i) + "r"
                    col = str(cur) + str(j) + "c"
                    box = str(cur) + str(math.floor(i / 3)) + str(math.floor(j / 3)) + "b"
                    if row in seen or col in seen or box in seen:
                        return False
                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        return True