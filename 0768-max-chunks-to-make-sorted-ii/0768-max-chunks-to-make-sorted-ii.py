class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # monotonic stack O(n ^ 2)
        s = []
        
        for num in arr:
            cur = num
            while s and s[-1] > num:
                cur = max(cur, s.pop())
            s.append(cur)
        
        # print(s)
        
        return len(s)