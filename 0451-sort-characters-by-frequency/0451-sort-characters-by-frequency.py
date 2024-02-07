class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        pq = []
        for key, value in counts.items():
            pq.append((value, key))
        
        pq = sorted(pq, reverse=True)
        res = ""
        for i in pq:
            for j in range(i[0]):
                res += i[1]
            
        return res