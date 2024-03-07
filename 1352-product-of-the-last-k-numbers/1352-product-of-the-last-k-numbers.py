class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = []
        self.lastZero = -1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if num == 0:
          self.lastZero = 0
          return
        elif self.lastZero != -1:
          self.lastZero += 1
        
        if len(self.prefix):
          self.prefix.append(self.prefix[-1] * num)
        else:
          self.prefix.append(num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        print(self.lastZero)
        
        if self.lastZero != -1 and self.lastZero < k:
            return 0
        
        n = len(self.prefix)
        
        earlierIndex = n - (k + 1)
        # print(earlierIndex)
        if earlierIndex < 0:
          return self.prefix[n - 1]
        
        res = self.prefix[n - 1] / self.prefix[earlierIndex]
        return int(res)