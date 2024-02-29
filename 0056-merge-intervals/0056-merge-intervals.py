class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals, key=lambda x: x[0])
        
        res = []
        
        for interval in sort:
            if not res:
                res.append(interval)
            else:
                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], interval[1])
                else:
                    res.append(interval)
        return res