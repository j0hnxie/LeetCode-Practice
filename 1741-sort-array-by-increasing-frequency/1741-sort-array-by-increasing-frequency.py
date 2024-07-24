class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freq_list = [(freq, -num) for num, freq in counter.items()]
        freq_list.sort()
        
        res = []
        for freq in freq_list:
            for _ in range(freq[0]):
                res.append(-freq[1])
        return res