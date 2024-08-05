class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        
        counter = 0
        for num in arr:
            if counts[num] == 1:
                counter += 1
                if counter == k:
                    return num
        return ""
