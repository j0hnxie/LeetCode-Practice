class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])
        return res[:k]