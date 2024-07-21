class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = 0
        vowels = set(["a", "e", "i", "o", "u"])
        for char in s:
            if char in vowels:
                vowel_count += 1
        
        if vowel_count != 0:
            return True
        else:
            return False