from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()
        
        for i in range(len(s)):
            current = s[i]
            if current == "(" or current == "[" or current == "{":
                stack.append(current)
            if current == ")" or current == "]" or current == "}":
                if len(stack) == 0:
                    return False
                elif current == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif current == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                
        