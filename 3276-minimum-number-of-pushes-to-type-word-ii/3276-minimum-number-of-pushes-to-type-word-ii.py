class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = defaultdict(int)

        for char in word:
            counts[char] += 1
        
        counts_list = [(value, key) for key, value in counts.items()]
        counts_list.sort(reverse=True)
        
        res = 0
        for idx, (count, char) in enumerate(counts_list):
            res += math.ceil((idx + 1) / 8) * count

        return res