class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counts = {}
        length = 0
        maxLength = 0
        start = 0
        for end in range(len(s)):
            if s[end] in counts:
                start = max(counts[s[end]] + 1, start)
                length = end - start + 1
                counts[s[end]] = end
                # print(start)
                # print(end)
                # print(length)
            else:
                length += 1
                counts[s[end]] = end
            # print(length)
            maxLength = max(maxLength, length)
            
        return maxLength