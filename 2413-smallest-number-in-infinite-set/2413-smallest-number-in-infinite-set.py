class SmallestInfiniteSet:

    def __init__(self):
        self.pq = [num for num in range(1, 1001)]
        self.set = set(self.pq.copy())
        heapq.heapify(self.pq)

    def popSmallest(self) -> int:
        popped = heapq.heappop(self.pq)
        self.set.discard(popped)
        return popped

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.pq, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)