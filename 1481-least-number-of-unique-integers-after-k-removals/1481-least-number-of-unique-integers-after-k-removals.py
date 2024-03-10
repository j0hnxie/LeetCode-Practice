class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        
        pq = []
        elements = len(counter)
        for num, freq in counter.items():
            heapq.heappush(pq, (freq, num))
        
        # 5: 2
        # 4: 1
        
        # (1,4), (2, 5)
        
        while pq:
            freq, num = heapq.heappop(pq)
            if freq > k:
                return elements
            else:
                k -= freq
                elements -= 1
        
        return elements