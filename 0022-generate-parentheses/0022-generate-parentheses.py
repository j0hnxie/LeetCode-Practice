class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [(0, 0, '')]
        res = []
        
        while stack:
            top = stack.pop()
            
            if len(top[2]) == n * 2:
                res.append(top[2])
                continue
            
            if top[0] < n:
                stack.append((top[0] + 1, top[1], top[2] + '('))
                
            if top[0] > top[1]:
                stack.append((top[0], top[1] + 1, top[2] + ')'))
        
        return res
        
        