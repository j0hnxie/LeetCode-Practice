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
            prev_idx = idx - 1
            while prev_idx >= 0 and (damages[prev_idx] == damages[idx] - 1 or damages[prev_idx] == damages[idx] - 2):
                prev_idx -= 1
            
            if prev_idx >= 0:
                memo[idx] = max(memo[idx - 1], memo[prev_idx] + freqs[damages[idx]] * damages[idx])
            else:
                memo[idx] = max(memo[idx - 1], freqs[damages[idx]] * damages[idx])
        
        return max(memo)

        