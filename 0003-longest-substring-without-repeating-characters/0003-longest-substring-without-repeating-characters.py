class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counts = set()
        length = 0
        maxLength = 0
        start = 0
        for end in range(len(s)):
            if s[end] in counts:
                while s[start] != s[end]:
                    counts.remove(s[start])
                    start += 1
                start += 1
                length = end - start + 1
                # print(start)
                # print(end)
                # print(length)
            else:
                length += 1
                counts.add(s[end])
            # print(counts)
            maxLength = max(maxLength, length)
            
        return maxLength