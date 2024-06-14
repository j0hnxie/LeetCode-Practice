class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        correct = sorted(arr)
        # print(correct)
        
        partitions = 0
        idx = 0
        cur = []
        while idx < n:
            cur.append(arr[idx])
            
            same = True
            cur.sort()
            # print(cur)
            for j in range(len(cur)):
                if cur[-(j + 1)] != correct[idx - j]:
                    same = False
                    break
                
            if same:
                partitions += 1
                cur = []
            
            idx += 1
        
        if len(cur) > 0:
            partitions += 1
        
        return partitions