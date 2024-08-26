class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqs = defaultdict(int)

        for damage in power:
            freqs[damage] += 1
        
        n = len(freqs)

        damages = sorted(list(freqs.keys()))

        memo = [0] * n
        memo[0] = freqs[damages[0]] * damages[0]

        for idx in range(1, n):
            memo[idx] = freqs[damages[idx]] * damages[idx]
            
            add = 0
            lower_limit = damages[idx] - 2

            if damages[idx - 1] < lower_limit:
                add = max(add, memo[idx - 1])
            
            if idx >= 2 and damages[idx - 2] < lower_limit:
                add = max(add, memo[idx - 2])
            
            if idx >= 3 and damages[idx - 3] < lower_limit:
                add = max(add, memo[idx - 3])
            
            if idx >= 4 and damages[idx - 4] < lower_limit:
                add = max(add, memo[idx - 4])
            
            if idx >= 5:
                add = max(add, memo[idx - 5])
            
            memo[idx] += add
        
        print(memo)
        return max(memo)

        