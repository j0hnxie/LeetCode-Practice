class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)

        for idx in range(n):
            asteroid = asteroids[idx]
            add = True
            while stack and stack[-1] >= 0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) < stack[-1]:
                    add = False
                    break
                else:
                    stack.pop()
                    add = False
                    break

            if add:
                stack.append(asteroid)
                
        return stack