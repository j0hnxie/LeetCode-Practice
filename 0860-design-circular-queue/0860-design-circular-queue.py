class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.back = 0
        self.size = 0
        self.queue = [0] * k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.back %= self.k
        self.back += 1
        
        self.queue[self.back - 1] = value

        self.size += 1
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front += 1
        self.front %= self.k

        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.back - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()