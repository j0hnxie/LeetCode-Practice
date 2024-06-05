class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_to_char = {}
        char_to_word = {}
        
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                if word != char_to_word[char]:
                    return False
            else:
                char_to_word[char] = word
            
            if word in word_to_char:
                if char != word_to_char[word]:
                    return False
            else:
                word_to_char[word] = char
            
        return True