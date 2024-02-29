class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            counts = [0 for i in range(26)]
            for char in s:
                counts[ord(char) - 97] += 1
            
            code = ""
            for i in range(26):
                if counts[i] != 0:
                    code += chr(i + 97)
                    code += str(counts[i])
            if code in groups:
                groups[code].append(s)
            else:
                groups[code] = [s]
        
        res = [value for key, value in groups.items()]
        return res