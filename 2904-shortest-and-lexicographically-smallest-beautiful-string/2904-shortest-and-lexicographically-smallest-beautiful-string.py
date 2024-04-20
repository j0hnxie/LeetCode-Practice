class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = float('inf')
        n = len(s)
        
        count = 0
        l = 0
        
        for r in range(n):
            dig = s[r]
            if dig == "1":
                count += 1
            
            if count < k:
                continue
            
            while count > k:
                if l >= n:
                    return str(res) if res != float('inf') else ""
                    
                if s[l] == "1":
                    count -= 1
                l += 1
            cur = int(s[l:r + 1])
            res = min(res, cur)
        
        return str(res) if res != float('inf') else ""