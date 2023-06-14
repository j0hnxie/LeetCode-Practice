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
            newCount = counts.get(s[end], 0) + 1
            counts[s[end]] = newCount
            if counts[s[end]] > 1:
                while s[start] != s[end]:
                    counts[s[start]] -= 1
                    start += 1
                counts[s[start]] -= 1
                start += 1
                length = end - start + 1
                # print(start)
                # print(end)
                # print(length)
            else:
                length += 1
            # print(counts)
            maxLength = max(maxLength, length)
            
        return maxLength