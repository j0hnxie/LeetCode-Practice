class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)

        for num in arr:
            freq[((num % k) + k ) % k] += 1
        # print(freq)
        for num, fre in freq.items():
            cur_num = (k - num) % k
            if cur_num == num:
                if fre % 2:
                    return False
            else:
                cur_fre = freq[cur_num]
                if fre != cur_fre:
                    return False
        return True 

