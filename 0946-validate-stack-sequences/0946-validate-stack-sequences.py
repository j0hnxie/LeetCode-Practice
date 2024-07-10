class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = deque()
        popped = deque(popped)
        
        for num in pushed:
            s.append(num)
            while s and popped and s[-1] == popped[0]:
                s.pop()
                popped.popleft()
        return not s