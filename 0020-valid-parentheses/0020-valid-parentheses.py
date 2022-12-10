from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()
        check = {")":"(", "]":"[","}":"{"}
        
        for i in range(len(s)):
            current = s[i]
            # print(current)
            if current == "(" or current == "[" or current == "{":
                stack.append(current)
            if current == ")" or current == "]" or current == "}":
                if len(stack) != 0:
                    if check[current] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        # print("pass")
        if len(stack) == 0:
            return True
        else:
            return False
                
        