class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for idx, char in enumerate(s):
            last[char] = idx
        
        idx = 0
        size = 0
        res = []
        n = len(s)
        end = -1

        while idx < n:
            end = max(end, last[s[idx]])
            while idx < n and idx <= end:
                end = max(end, last[s[idx]])
                idx += 1
                size += 1
            
            res.append(size)
            size = 0

        return res
        
        
