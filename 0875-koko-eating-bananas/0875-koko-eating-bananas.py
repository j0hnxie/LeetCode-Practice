class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursEating(k: int) -> int:
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total
            
        
        
        l = 1
        r = max(piles)
        
        while l < r:
            m = int(l + (r - l) / 2)
            # print(str(m) + " " + str(hoursEating(m)))
            if hoursEating(m) <= h:
                r = m
            else:
                l = m + 1
        return r