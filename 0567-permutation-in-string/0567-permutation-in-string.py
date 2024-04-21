class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if n < m:
            return False
        
        s1_counts = {}
        s2_counts = {}
        for idx in range(m):
            s1_char = s1[idx]
            s2_char = s2[idx]
            s1_counts[s1_char] = s1_counts.get(s1_char, 0) + 1
            s2_counts[s2_char] = s2_counts.get(s2_char, 0) + 1
        
        equals = 0
        for char in range(26):
            cur_char = chr(ord('a') + char)
            if s1_counts.get(cur_char, 0) == s2_counts.get(cur_char, 0):
                equals += 1
        
        if equals == 26:
            return True
            
        for idx in range(n - m):
            s2_start_char = s2[idx]
            s2_end_char = s2[idx + m]
            
            if s2_counts.get(s2_start_char, 0) == s1_counts.get(s2_start_char, 0):
                equals -= 1
            s2_counts[s2_start_char] = s2_counts.get(s2_start_char, 0) - 1
            if s2_counts.get(s2_start_char, 0) == s1_counts.get(s2_start_char, 0):
                equals += 1
                
            if s2_counts.get(s2_end_char, 0) == s1_counts.get(s2_end_char, 0):
                equals -= 1
            s2_counts[s2_end_char] = s2_counts.get(s2_end_char, 0) + 1
            if s2_counts.get(s2_end_char, 0) == s1_counts.get(s2_end_char, 0):
                equals += 1
            
            # print(equals)
            # print(s1_counts)
            # print(s2_counts)
            # print()
            
            if equals == 26:
                return True
            
        return equals == 26
            