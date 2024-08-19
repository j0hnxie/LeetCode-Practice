class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        n = len(s)

        order = ""
        for idx, char in enumerate(s):
            if char in vowels:
                order += char
        
        order = order[::-1]
        vowel_idx = 0

        res = ""
        for char in s:
            if char in vowels:
                res += order[vowel_idx]
                vowel_idx += 1
            else:
                res += char

        return res