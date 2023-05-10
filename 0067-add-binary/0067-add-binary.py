class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
#         aInt = int(a, 2)
#         bInt = int(b, 2)
#         resultInt = aInt + bInt
#         result = bin(resultInt).replace("0b", "")
#         return result
        
        aLen = len(a) - 1
        bLen = len(b) - 1
        result = ""
        nextOne = 0
        
        while aLen >= 0 or bLen >= 0:
            aDigit = 0
            bDigit = 0
            if aLen >= 0:
                aDigit = int(a[aLen])
                aLen -= 1
            if bLen >= 0:
                bDigit = int(b[bLen])
                bLen -= 1
                
            digit = aDigit + bDigit
            
            digit += nextOne
                
            result += str(digit % 2)
            nextOne = digit / 2
            
        if nextOne:
            result += str(nextOne)
        
        # print(result)
        result = result[::-1]
                
        return result