class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        s_len, a_len, b_len = len(s), len(a), len(b)

        b_indices = []
        for idx in range(s_len - b_len + 1):
            if s[idx:idx + b_len] == b:
                b_indices.append(idx)
        
        n = len(b_indices)
        if n == 0:
            return []

        res = []

        for idx in range(s_len - a_len + 1):
            if s[idx:idx + a_len] == a:
                left, right = 0, n - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if b_indices[mid] < idx:
                        left = mid + 1
                    else:
                        right = mid
                
                # print(b_indices)
                # print(len(b_indices))
                # print(left)
                cur_b = b_indices[left]
                if abs(cur_b - idx) <= k:
                    res.append(idx)
                    continue

                if left > 0 and abs(abs(b_indices[left - 1] - idx)) <= k:
                    res.append(idx)

                # if abs(b_indices[left] - idx) <= k:
                #     res.append(idx)
                #     continue
        return res
