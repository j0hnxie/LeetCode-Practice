class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def validPalindrome(palindromic_string):
            return palindromic_string == palindromic_string[::-1]
        
        n = len(s)
        result = []

        def backtrack(prev_split, idx, strings):
            if idx == n:
                if prev_split == n:
                    result.append(strings.copy())
                    return
                else:
                    return
            
            backtrack(prev_split, idx + 1, strings)

            substr = s[prev_split:idx + 1]
            if validPalindrome(substr):
                strings.append(substr)
                backtrack(idx + 1, idx + 1, strings)
                strings.pop()
        
        backtrack(0, 0, [])
        return result
