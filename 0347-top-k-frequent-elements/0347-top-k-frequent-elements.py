class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for i in range(n + 1)]
        for key, value in counts.items():
            freqs[value].append(key)
        
        res = []
        counter = 0
        index = n
        while counter < k:
            while not freqs[index]:
                index -= 1
            pop = freqs[index][-1]
            freqs[index].pop()
            res.append(pop)
            counter += 1
        
        return res