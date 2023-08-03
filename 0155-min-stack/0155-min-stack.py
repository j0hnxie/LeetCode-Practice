class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mi = float('inf')
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack:
            self.mi = min(self.stack[-1][1], val)
            self.stack.append([val, self.mi])
        else:
            self.mi = val
            self.stack.append([val, self.mi])
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()