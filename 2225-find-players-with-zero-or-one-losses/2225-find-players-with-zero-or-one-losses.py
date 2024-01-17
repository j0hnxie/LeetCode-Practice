class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        wins = {}
        losses = {}
        for match in matches:
            curLoss = losses.get(match[0], 0)
            curLoss += 0
            losses[match[0]] = curLoss
            curLoss = losses.get(match[1], 0)
            curLoss += 1
            losses[match[1]] = curLoss
            
        noLoss = []
        oneLoss = []
        
        for key, value in losses.items():
            if value == 0:
                noLoss.append(key)
            if value == 1:
                oneLoss.append(key)
                
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
            