class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            cur = int(digit)
            while k and stack and int(stack[-1]) > cur:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        stack = stack[:-k] if k else stack
        ans = ''.join(stack)
        ans = ans.lstrip("0")
        ans = ans if ans else "0"
        return ans