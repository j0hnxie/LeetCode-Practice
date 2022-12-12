# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            midTF = isBadVersion(mid)
            if midTF:
                if isBadVersion(mid - 1):
                    r = mid - 1
                else:
                    return mid
            else:
                if not isBadVersion(mid + 1):
                    l = mid + 1
                else:
                    return mid + 1
                
        return -1