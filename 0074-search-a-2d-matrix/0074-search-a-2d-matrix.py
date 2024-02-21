class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m * n - 1
        
        while l <= r:
            mid = int(l + (r - l) / 2)
            row = mid // n
            col = mid % n
            cur = matrix[row][col]
            
            if cur < target:
                l = mid + 1
            elif cur > target:
                r = mid - 1
            else:
                return True
        return False