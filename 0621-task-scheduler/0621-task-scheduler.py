class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
        counts = [0] * 26

        for task in tasks:
            idx = ord(task) - ord('A')
            counts[idx] += 1

        maxCount = 0
        numOfMax = 0
        for count in counts:
            if count > maxCount:
                maxCount = count
                numOfMax = 1
            elif count == maxCount:
                numOfMax += 1
                
        # print(maxCount)
        # print(numOfMax)

        return max((maxCount - 1) * (n + 1) + numOfMax, len(tasks))
