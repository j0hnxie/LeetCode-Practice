class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        i = 0
        while i < len(s):
            print(result)
            if s[i] == "I":
                if i != len(s) - 1:
                    if s[i + 1] == "V":
                        result += 4
                        i += 2
                        continue
                    elif s[i + 1] == "X":
                        result += 9
                        i += 2
                        continue
                result += 1
            elif s[i] == "X":
                if i != len(s) - 1:
                    if s[i + 1] == "L":
                        result += 40
                        i += 2
                        continue
                    elif s[i + 1] == "C":
                        result += 90
                        i += 2
                        continue
                result += 10
            elif s[i] == "C":
                if i != len(s) - 1:
                    if s[i + 1] == "D":
                        result += 400
                        i += 2
                        continue
                    elif s[i + 1] == "M":
                        result += 900
                        i += 2
                        continue
                result += 100
            else:
                # print(values[s[i]])
                result += values[s[i]]
            i += 1
                
        return result