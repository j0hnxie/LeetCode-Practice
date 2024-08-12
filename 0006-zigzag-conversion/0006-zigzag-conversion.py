class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        height = numRows
        width = math.ceil(n / (max(numRows - 2, 0) + numRows)) * (max(numRows - 2, 0) + 1)
        zigzag = [[""] * width for _ in range(height)]
        idx = 0
        cur_x, cur_y = 0, 0
        while idx < n:
            cur_x = 0
            while cur_x < numRows and idx < n:
                zigzag[cur_x][cur_y] = s[idx]
                cur_x += 1
                idx += 1
            
            cur_x -= 1
            counter = 0
            while counter < max(numRows - 2, 0) and idx < n:
                cur_y += 1
                cur_x -= 1
                zigzag[cur_x][cur_y] = s[idx]
                idx += 1
                counter += 1
            cur_y += 1
        
        res = ""
        for row in zigzag:
            for char in row:
                res += char
        return res