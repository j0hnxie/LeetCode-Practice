class StockSpanner:

    def __init__(self):
        self.counter = 0
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if self.stack:
            result = self.counter - self.stack[-1][1]
        else:
            result = self.counter + 1

        self.stack.append((price, self.counter))
        self.counter += 1
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)