class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        res, cur = 0, 0
        
        for idx in range(minutes):
            if grumpy[idx]:
                cur += customers[idx]
            else:
                res += customers[idx]
        
        max_unsatisfied = cur
        for end in range(minutes, n):
            if grumpy[end - minutes]:
                cur -= customers[end - minutes]
            if grumpy[end]:
                cur += customers[end]
            else:
                res += customers[end]
            # print(cur)
            max_unsatisfied = max(max_unsatisfied, cur)
        
        # print(res)
        # print(max_unsatisfied)
        return res + max_unsatisfied