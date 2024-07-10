class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = deque()
        pushed = deque(pushed)
        popped = deque(popped)
        
        while pushed or popped:
            if s and popped[0] == s[-1]:
                popped.popleft()
                s.pop()
            else:
                if pushed:
                    s.append(pushed.popleft())
                else:
                    return False
            # print(s)
        return True if not s else False