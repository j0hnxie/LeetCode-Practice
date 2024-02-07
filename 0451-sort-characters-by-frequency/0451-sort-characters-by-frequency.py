class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        pq = []
        for key, value in counts.items():
            heapq.heappush(pq, (-1 * value, key))
        
        res = ""
        while pq:
            cur = heapq.heappop(pq)
            for i in range(cur[0] * -1):
                res += cur[1]
        return res