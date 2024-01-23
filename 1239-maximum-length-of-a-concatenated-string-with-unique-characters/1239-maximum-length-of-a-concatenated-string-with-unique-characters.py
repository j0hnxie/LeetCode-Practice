class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
#         unique = []
#         for s in arr:
#             u = set(s)
#             if len(u) == len(s): unique.append(u)
        
#         # [2] now start with an empty concatenation and iteratively
#         #    increase its length by trying to add more strings
#         concat = [set()]
#         for u in unique:
#             for c in concat:
#                 print(type(u))
#                 print(type(c))
#                 if not c & u:
#                     concat.append(c | u)
#         return max(len(cc) for cc in concat)
        noRepeats = []
        for i in arr:
            if len(i) == len(set(i)):
                noRepeats.append(i)
        
        dp = [set()]
        for i in noRepeats:
            for j in dp:
                if not set(i) & j:
                    dp.append(set(i) | j)
        return max(len(perm) for perm in dp)
                    