class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}

        def numTreesFromLowToHigh(low, high):
            if low >= high:
                return 1

            if (low, high) in self.memo:
                return self.memo[(low, high)]

            count = 0
            for root in range(low, high + 1):
                left_subtrees = numTreesFromLowToHigh(low, root - 1)
                right_subtrees = numTreesFromLowToHigh(root + 1, high)
                count += left_subtrees * right_subtrees

            self.memo[(low, high)] = count    
            return count
        return numTreesFromLowToHigh(1, n)