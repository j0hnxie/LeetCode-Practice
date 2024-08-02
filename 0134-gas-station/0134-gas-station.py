class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        cur = 0
        n = len(gas)
        start = 0

        for idx in range(n):
            cur_diff = gas[idx] - cost[idx]
            total += cur_diff
            cur += cur_diff
            if cur < 0:
                cur = 0
                start = (idx + 1) % n
        
        return -1 if total < 0 else start
        