class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        total = 0
        res = ""
        
        for idx in range(n - 1, -1, -1):
            total += shifts[idx]
            char_val = ord(s[idx]) - 97
            new_val = (char_val + total) % 26
            new_char = chr(new_val + 97)
            res += new_char
        
        res = res[::-1]
        
        return res