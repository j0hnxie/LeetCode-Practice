class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        n = len(expression)
        results = []
        for idx in range(n):
            char = expression[idx]
            if char == "-" or char == "*" or char == "+":
                left_exp = expression[:idx]
                right_exp = expression[idx + 1:]
            
                left_results = self.diffWaysToCompute(left_exp)
                right_results = self.diffWaysToCompute(right_exp)

                for left in left_results:
                    for right in right_results:
                        if char == "-":
                            results.append(left - right)
                        elif char == "*":
                            results.append(left * right)
                        elif char == "+":
                            results.append(left + right)

        return results