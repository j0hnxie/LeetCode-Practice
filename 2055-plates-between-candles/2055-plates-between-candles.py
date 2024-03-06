class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        answer = []
        n = len(s)
        
        nextC = [float('inf') for i in range(n)]
        prevC = [-1 for i in range(n)]
        plates = [0 for i in range(n)]
            
        if s[0] == "*":
            plates[0] = 1
        else:
            prevC[0] = 0
        
        if s[-1] == "|":
            nextC[-1] = n - 1
        
        for i in range(1, n):
            if s[i] == "*":
                plates[i] = plates[i - 1] + 1
                prevC[i] = prevC[i - 1]
            else:
                plates[i] = plates[i - 1]
                prevC[i] = i
        
        for i in range(n - 2, -1, -1):
            if s[i] == "|":
                nextC[i] = i
            else:
                nextC[i] = nextC[i + 1]
                
        for start, end in queries:
            firstCandle = nextC[start]
            lastCandle = prevC[end]
            
            if firstCandle == -1 or lastCandle == float('inf'):
                answer.append(0)
                continue
            
            if firstCandle > end or lastCandle < start or firstCandle > lastCandle:
                answer.append(0)
                continue
            
            plate = plates[lastCandle] - plates[firstCandle]
            answer.append(plate)
        return answer
        