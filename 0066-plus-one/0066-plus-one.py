class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            if carry and digits[i] == 9:
                digits[i] = 0
            elif carry:
                digits[i] = digits[i] + 1
                return digits
        
        if carry:
            return [1] + digits
        else:
            return digits
            
