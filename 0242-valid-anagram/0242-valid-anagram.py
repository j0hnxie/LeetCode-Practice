class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sSorted = sorted(s)
        tSorted = sorted(t)
        
        if sSorted != tSorted:
            return False
        else:
            return True
        
#         sDict = {}
#         tDict = {}
        
#         for i in range(128):
#             sDict[chr(i)] = 0
#             tDict[chr(i)] = 0
        
#         for i in s:
#             sDict[i] = sDict[i] + 1
        
#         for i in t:
#             tDict[i] = tDict[i] + 1
            
#         for key, item in sDict.items():
#             if item != 0:
#                 print(key + " " + str(item))
            
#         for key, item in tDict.items():
#             if item != 0:
#                 print(key + " " + str(item))
        
#         for key, item in sDict.items():
#             # if item != 0 or tDict[key] != 0:
#                 # print(key + " " + str(item) + " " + str(tDict[key]))
#             if item != tDict[key]:
#                 return False
        
#         return True
