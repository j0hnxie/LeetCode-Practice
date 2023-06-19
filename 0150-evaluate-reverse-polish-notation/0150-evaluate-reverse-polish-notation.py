class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        operators = set()
        operators.add('+')
        operators.add('-')
        operators.add('*')
        operators.add('/')
        stack = []
        
        for i in tokens:
            stack.append(i)
            # print(stack)
            
            if i in operators:
                operation = stack.pop()
                second = int(stack.pop())
                first = int(stack.pop())
                if operation == '+':
                    result = first + second
                elif operation == '-':
                    result = first - second
                elif operation == '*':
                    result = first * second
                elif operation == "/":
                    result = int(float(first) / float(second))
                else:
                    print("invalid operation")
                stack.append(result)
            
        return int(stack[0])