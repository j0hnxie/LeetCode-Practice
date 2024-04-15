class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)
        self.pq = []
        
        for i in range(k):
            if nums:
                temp = heapq.heappop(nums)
                heapq.heappush(self.pq, temp * -1)
            else:
                heapq.heappush(self.pq, float('-inf'))
        
        self.cur = heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if val <= self.cur:
            return self.cur
        else:
            res = heapq.heappushpop(self.pq, val)
            self.cur = res
            return res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)