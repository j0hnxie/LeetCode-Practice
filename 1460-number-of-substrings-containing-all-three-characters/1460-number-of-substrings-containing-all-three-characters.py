class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        a_idx = [float('inf')] * n
        b_idx = [float('inf')] * n
        c_idx = [float('inf')] * n

        if s[-1] == 'a':
            a_idx[-1] = n - 1
        elif s[-1] == 'b':
            b_idx[-1] = n - 1
        elif s[-1] == 'c':
            c_idx[-1] = n - 1

        for idx in range(n - 2, -1, -1):
            a_idx[idx] = a_idx[idx + 1]
            b_idx[idx] = b_idx[idx + 1]
            c_idx[idx] = c_idx[idx + 1]

            cur_char = s[idx]
            if cur_char == 'a':
                a_idx[idx] = idx
            elif cur_char == 'b':
                b_idx[idx] = idx
            elif cur_char == 'c':
                c_idx[idx] = idx
        
        result = 0
        for idx in range(n):
            max_so_far = max((a_idx[idx], b_idx[idx], c_idx[idx]))
            if max_so_far != float('inf'):
                result += n - max_so_far

        return result