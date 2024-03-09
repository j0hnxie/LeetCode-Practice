class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        counter = 0
        for i in range(m):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                counter += 1
        return counter >= n