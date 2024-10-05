class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.increments = []
        self.max = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if self.stack:
            inc = self.increments.pop()
            if self.increments:
                self.increments[-1] += inc
            return self.stack.pop() + inc
        
        return -1

    def increment(self, k: int, val: int) -> None:
        if k:
            incIdx = min(k - 1, len(self.increments) - 1)
            if self.increments:
                self.increments[incIdx] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)