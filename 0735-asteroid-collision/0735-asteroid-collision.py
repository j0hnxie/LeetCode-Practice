class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) >= 2:
                first = stack.pop()
                second = stack.pop()
                
                if (first < 0 and second > 0):
                    if abs(first) > abs(second):
                        stack.append(first)
                    elif abs(first) < abs(second):
                        stack.append(second)
                else:
                    stack.append(second)
                    stack.append(first)
                    break
                    
        return list(stack)
                