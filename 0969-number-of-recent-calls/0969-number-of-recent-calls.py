class RecentCounter:

    def __init__(self):
        self.requests = 0
        self.pings = deque()

    def ping(self, t: int) -> int:
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()
    
        self.pings.append(t)
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)