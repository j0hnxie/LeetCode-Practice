class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = stone * -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            large = heapq.heappop(stones)
            small = heapq.heappop(stones)
            if large != small:
                heapq.heappush(stones, large - small)
            
        return -1 * stones.pop() if stones else 0
        

#         # Make all the stones negative. We want to do this *in place*, to keep the
#         # space complexity of this algorithm at O(1). :-)
#         for i in range(len(stones)):
#             stones[i] *= -1

#         # Heapify all the stones.
#         heapq.heapify(stones)

#         # While there is more than one stone left, remove the two
#         # largest, smash them together, and insert the result
#         # back into the heap if it is non-zero.
#         while len(stones) > 1:
#             stone_1 = heapq.heappop(stones)
#             stone_2 = heapq.heappop(stones)
#             if stone_1 != stone_2:
#                 heapq.heappush(stones, stone_1 - stone_2)

#         # Check if there is a stone left to return. Convert it back
#         # to positive.
#         return -heapq.heappop(stones) if stones else 0