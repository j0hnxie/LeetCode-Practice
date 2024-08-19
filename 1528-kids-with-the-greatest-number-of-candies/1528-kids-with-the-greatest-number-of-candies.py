class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        n = len(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= largest:
                res.append(True)
            else:
                res.append(False)
        
        return res