class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        res = []
        curMerge = intervals[0]
        for i in range(len(intervals)):
            if intervals[i][0] <= curMerge[1]:
                curMerge = [min(curMerge[0], intervals[i][0]),
                           max(curMerge[1], intervals[i][1])]
            else:
                res.append(curMerge)
                curMerge = intervals[i]
        res.append(curMerge)
        return res
                