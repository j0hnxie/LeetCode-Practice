class MyQueue(object):

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        
        self.stack2.clear()
        size = len(self.stack1)
        for i in range(size):
            self.stack2.append(self.stack1.pop())
            
        result = self.stack2.pop()
        for i in range(size - 1):
            self.stack1.append(self.stack2.pop())
            
        return result
        

    def peek(self):
        """
        :rtype: int
        """
        
        return self.stack1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()