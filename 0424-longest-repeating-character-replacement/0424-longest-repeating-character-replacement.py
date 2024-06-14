class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        res = 0
        running_max = 0
        chars = {}
        
        while r < n:
            cur_char = s[r]
            chars[cur_char] = chars.get(cur_char, 0) + 1
            running_max = max(running_max, chars[cur_char])
            window_len = r - l + 1
            while window_len - running_max > k:
                l_char = s[l]
                chars[l_char] -= 1
                l += 1
                window_len = r - l + 1
            res = max(res, window_len)
            r += 1
        
        return res