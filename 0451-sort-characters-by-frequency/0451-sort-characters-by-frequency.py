class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        
        # pq = []
        # for key, value in counts.items():
        #     pq.append((value, key))
        
        pq = sorted(counts.items(), key=lambda item: item[1],reverse=True)
        res = ""
        for i in pq:
            res += i[0] * i[1]
            
        return res