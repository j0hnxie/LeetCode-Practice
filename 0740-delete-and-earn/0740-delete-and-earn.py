class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # freqs = Counter(nums)
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        keys = sorted(list(freqs.keys()))

        n = len(keys)
        memo = [0] * n
        memo[0] = keys[0] * freqs[keys[0]]

        # if len(keys) > 1:
        #     memo[1] = keys[1] * freqs[keys[1]]
        #     memo[1] += 0 if keys[1] == keys[0] - 1 else memo[0]
        
        for idx in range(1, n):
            memo[idx] = memo[idx - 1]

            if keys[idx - 1] == keys[idx] - 1:
                if idx < 2:
                    memo[idx] = max(memo[idx], keys[idx] * freqs[keys[idx]])
                else:
                    memo[idx] = max(memo[idx], keys[idx] * freqs[keys[idx]] + memo[idx - 2])
            else:
                memo[idx] += keys[idx] * freqs[keys[idx]]
        
        print(memo)
        return memo[-1]

