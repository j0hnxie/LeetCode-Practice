class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        
        pre_sort, pre_non, res = 0, 0, 0
        for a, b in zip(arr, sorted_arr):
            pre_non += a
            pre_sort += b
            res += 1 if pre_non == pre_sort else 0
            
        return res