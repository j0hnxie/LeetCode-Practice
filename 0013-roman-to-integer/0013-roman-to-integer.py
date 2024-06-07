class Solution:
    def romanToInt(self, s: str) -> int:
        possibles = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        res = 0
        idx = 0
        while idx < len(s):
            if s[idx:idx + 2] in possibles:
                res += possibles[s[idx:idx+2]]
                idx += 1
            else:
                res += possibles[s[idx]]
            idx += 1
        return res