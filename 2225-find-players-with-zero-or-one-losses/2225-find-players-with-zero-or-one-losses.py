class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        noLoss = set()
        oneLoss = set()
        moreThanOneLoss = set()
        for match in matches:
            if match[1] in oneLoss:
                oneLoss.remove(match[1])
                moreThanOneLoss.add(match[1])
            elif match[1] not in moreThanOneLoss:
                noLoss.discard(match[1])
                oneLoss.add(match[1])
                
            if match[0] not in oneLoss and match[0] not in moreThanOneLoss:
                noLoss.add(match[0])
            
        oneLoss = list(oneLoss)
        noLoss = list(noLoss)
        noLoss.sort()
        oneLoss.sort()
                
#         for key, value in losses.items():
#             if value == 0:
#                 curWins = wins.get(key, 0)
#                 heapq.heappush(noLoss, (curWins, key))
#             if value == 1:
#                 curWins = wins.get(key, 0)
#                 heapq.heappush(oneLoss, (curWins, key))
        
#         noLossFinal = []
#         oneLossFinal = []
        
#         while noLoss:
#             cur = heapq.heappop(noLoss)
#             noLossFinal.append(cur[1])
            
#         while oneLoss:
#             cur = heapq.heappop(oneLoss)
#             oneLossFinal.append(cur[1])
        
        ans = [noLoss, oneLoss]
        return ans
            