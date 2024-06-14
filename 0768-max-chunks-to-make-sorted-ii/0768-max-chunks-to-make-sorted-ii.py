class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # preprocessing max and min
        s = []
        running_min = []
        
        cur_min = float('inf')
        for num in reversed(arr):
            cur_min = min(num, cur_min)
            running_min.append(cur_min)
        
        running_min.reverse()
        
        chunks, cur_max = 1, 0
        for idx in range(len(arr) - 1):
            num = arr[idx]
            cur_max = max(num, cur_max)
            if cur_max <= running_min[idx + 1]:
                chunks += 1
        
        return chunks