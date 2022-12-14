class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        result1 = []
        result2 = []
        replaceInterval = newInterval
        
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[0] > interval[1]:
                result1.append(interval)
            elif newInterval[1] < interval[0]:
                result2.append(interval)
            else:
                # print(interval)
                replaceInterval[0] = min(interval[0], replaceInterval[0])
                replaceInterval[1] = max(interval[1], replaceInterval[1])
                # print(replaceInterval)
                
        replaceInterval = [replaceInterval]
                
        # print(result)
        result.extend(result1)
        # print(result)
        result.extend(replaceInterval)
        # print(result)
        result.extend(result2)
        return result
            
                
                