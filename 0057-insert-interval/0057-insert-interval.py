class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        marked = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                marked = True
                break
                
        if not marked:
            intervals.append(newInterval)
        
        i = 0
        result = []
        while i < len(intervals):
            cur = intervals[i]
            while i < len(intervals) and min(cur[1], intervals[i][1]) - max(cur[0], intervals[i][0]) >= 0:
                cur = [min(cur[0], intervals[i][0]), max(cur[1], intervals[i][1])]
                i += 1
            i -= 1
            result.append(cur)
            i += 1
        return result