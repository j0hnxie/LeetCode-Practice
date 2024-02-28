class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(l, r):
            if l == r:
                return strs[l]
            
            
            mid = l + (r - l) // 2
            left = lcp(l, mid)
            right = lcp(mid + 1, r)
            
            pre = ""
            for i in range(min(len(left), len(right))):
                if left[i] != right[i]:
                    break
                else:
                    pre += left[i]
            return pre
            
            
        n = len(strs)
        return lcp(0, n - 1)