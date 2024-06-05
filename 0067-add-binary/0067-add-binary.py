class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        counter = 0
        carry = False
        res = ""
        while counter < min(len(a), len(b)):
            cur_a = int(a[counter])
            cur_b = int(b[counter])
            
            carry_dig = 1 if carry else 0
            cur_dig = cur_a + cur_b + carry_dig
            carry = True if cur_dig >= 2 else False
            cur_dig = cur_dig % 2
            
            res = str(cur_dig) + res
            counter += 1
        
        longer_str = a if len(a) > len(b) else b
        
        while counter < len(longer_str):
            cur_dig = int(longer_str[counter])
            
            carry_dig = 1 if carry else 0
            cur_dig += carry_dig
            carry = True if cur_dig >= 2 else False
            cur_dig = cur_dig % 2
            
            res = str(cur_dig) + res
            counter += 1
        
        if carry:
            res = "1" + res
        
        return res