class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        sDict = collections.defaultdict(int)
        
        for i in s:
            sDict[i] += 1
        
        for i in t:
            sDict[i] -= 1
            
        for keys, values in sDict.items():
            if sDict[keys] != 0:
                return False
            
        return True
        
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
