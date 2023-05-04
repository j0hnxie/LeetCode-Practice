from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = deque()
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i == ")":
                    if stack[-1] != "(":
                        return False
                    stack.pop()
                elif i == "]":
                    if stack[-1] != "[":
                        return False
                    stack.pop()
                elif i == "}":
                    if stack[-1] != "{":
                        return False
                    stack.pop()
                else:
                    stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False
                
        