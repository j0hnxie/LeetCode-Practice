class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.upper) == len(self.lower):
            move = heapq.heappushpop(self.lower, -num)
            move = heapq.heappushpop(self.upper, -move)
            heapq.heappush(self.lower, -move)
        else:
            move = heapq.heappushpop(self.lower, -num)
            heapq.heappush(self.upper, -move)

    def findMedian(self) -> float:
        # print(self.lower)
        # print(self.upper)
        if len(self.upper) == len(self.lower):
            upperH = -self.lower[0]
            lowerH = self.upper[0]
            return (upperH + lowerH) / 2
        else:
            return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()