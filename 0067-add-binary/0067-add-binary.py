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
        result = bin(resultInt).replace("0b", "")
        return result
        
#         aLen = len(a)
#         bLen = len(b)
#         result = []
#         nextOne = 0
        
#         while aLen >= 0 and bLen >= 0:
#             aDigit = int(a[aLen])
#             bDigit = int(b[bLen])
#             digit = aDigit + bDigit
            
#             if nextOne:
#                 digit += nextOne
                
#             if digit > 1:
                
            
#             result.append(digit % 2)
#             aLen -= 1
#             bLen -= 1