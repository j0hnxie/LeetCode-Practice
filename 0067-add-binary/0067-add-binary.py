class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aInt = int(a, 2)
        bInt = int(b, 2)
        resultInt = aInt + bInt
        result = "{0:b}".format(resultInt)
        return result