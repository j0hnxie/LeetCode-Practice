class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxTypes = sorted(boxTypes, key=lambda x: -x[1])
        n = len(boxTypes)
        
        res = 0
        index = 0
        for boxType in sortedBoxTypes:
            boxCount = min(boxType[0], truckSize)
            truckSize -= boxCount
            res += boxCount * boxType[1]
            if truckSize == 0:
                break
        return res
            