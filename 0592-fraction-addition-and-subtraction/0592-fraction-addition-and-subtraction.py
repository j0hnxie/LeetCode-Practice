class Solution:
    def fractionAddition(self, expression: str) -> str:

        # Function to calculate the LCM of two numbers
        def lcm(x, y):
            # Calculate the product of the numbers
            product = x * y
            # Calculate the GCD (Greatest Common Divisor) of the numbers
            gcd_result = gcd(x, y)
            # Calculate the LCM using the formula: LCM = (x * y) / GCD(x, y)
            lcm_result = product // gcd_result
            return lcm_result

        numbers = []
        operations = []
        operators = set(["+", "-"])

        if expression[0] == "-":
            numbers.append("0/1")
        else:
            numbers.append("")

        for char in expression:
            if char in operators:
                operations.append(char)
                numbers.append("")
            else:
                numbers[-1] += char

        n = len(numbers)

        numerator, denominator = numbers[0].split("/")
        numerator, denominator = int(numerator), int(denominator)
        for idx in range(1, n):
            current_numerator, current_denominator = numbers[idx].split("/")
            current_numerator, current_denominator = int(current_numerator), int(current_denominator)
            current_operator = operations[idx - 1]

            new_denominator = lcm(denominator, current_denominator)
            factor = new_denominator // denominator
            new_numerator = numerator * factor
            current_factor = new_denominator // current_denominator
            current_numerator *= current_factor

            if current_operator == "+":
                numerator = new_numerator + current_numerator
            else:
                numerator = new_numerator - current_numerator

            denominator = new_denominator

        gcf = gcd(numerator, denominator)
        numerator //= gcf
        denominator //= gcf
        
        return str(numerator) + "/" + str(denominator)