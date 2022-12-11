class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        curMax = 0
        exists = set()
        begin = 0
        end = 0
        
        while end < len(s):
            # print(str(begin) + " " + str(end))
            if s[end] not in exists:
                exists.add(s[end])
                end += 1
                curMax = max(curMax, end - begin)
            else:
                while s[end] != s[begin]:
                    exists.remove(s[begin])
                    begin += 1
                begin += 1
                end += 1
                
        return curMax