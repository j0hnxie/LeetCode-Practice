class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceCandy = set(aliceSizes)
        bobCandy = set(bobSizes)
        aliceTot = sum(aliceSizes)
        bobTot = sum(bobSizes)

        if bobTot > aliceTot:
            diff = bobTot - aliceTot
            diff //= 2
            for candy in bobSizes:
                if candy - diff in aliceCandy:
                    return [candy - diff, candy]
        else:
            diff = aliceTot - bobTot
            diff //= 2
            for candy in aliceSizes:
                if candy - diff in bobCandy:
                    return [candy, candy - diff]
        
        