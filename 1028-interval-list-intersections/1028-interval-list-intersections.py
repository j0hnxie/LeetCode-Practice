class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        first_idx, second_idx = 0, 0

        result = []
        while first_idx < m and second_idx < n:
            first_interval, second_interval = firstList[first_idx], secondList[second_idx]

            if min(first_interval[1], second_interval[1]) >= max(first_interval[0], second_interval[0]):
                    result.append([max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])
            
            if first_interval[1] < second_interval[1]:
                first_idx += 1
            else:
                second_idx += 1
        return result