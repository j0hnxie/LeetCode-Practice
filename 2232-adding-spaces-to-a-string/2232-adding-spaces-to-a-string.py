class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        space_idx = len(spaces) - 1

        for idx in range(len(s) - 1, -1, -1):
            res += s[idx]
            if idx == spaces[space_idx]:
                res += " "
                space_idx -= 1

        return res[::-1]