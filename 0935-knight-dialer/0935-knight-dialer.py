class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = (10 ** 9 + 7)
        memo = [1 for i in range(10)]
        prev = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [7, 1, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        for col in range(2, n + 1):
            cur = []
            for row in range(10):
                numberOfNumbers = 0
                for num in prev[row]:
                    numberOfNumbers += memo[num]
                    numberOfNumbers %= MOD
                cur.append(numberOfNumbers)
            memo = cur
            
        res = 0
        for entry in memo:
            res += entry
            res %= MOD
        
        return res
        