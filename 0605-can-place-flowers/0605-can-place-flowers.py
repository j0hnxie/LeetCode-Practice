class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for idx, flower in enumerate(flowerbed):
            if flower == 0 and (flowerbed[idx - 1] != 1 or idx == 0) and (idx == len(flowerbed) - 1 or flowerbed[idx + 1] != 1):
                flowerbed[idx] = 1
                n -= 1
                if n == 0:
                    break

        return n <= 0