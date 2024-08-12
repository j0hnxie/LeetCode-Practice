class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        n = len(nums)
        nums.sort()
        
        self.min_heap = []
        idx = 0
        while idx < k and idx < n:
            self.min_heap.append(nums[n - 1 - idx])
            idx += 1
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)