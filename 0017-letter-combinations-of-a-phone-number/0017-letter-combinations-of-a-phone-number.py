class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        result = []
        def helper(idx, cur):
            n = len(digits)
            if idx == n:
                nonlocal result
                result.append(cur)
                return
            
            string = mapping[int(digits[idx])]
            for char in string:
                helper(idx + 1, cur + char)
        
        helper(0, "")
        return result if result != [""] else []