class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = s1.split(), s2.split()
        dict1, dict2 = Counter(words1), Counter(words2)

        res = []
        for word, freq in dict1.items():
            if freq == 1 and word not in dict2:
                res.append(word)
        
        for word, freq in dict2.items():
            if freq == 1 and word not in dict1:
                res.append(word)
        
        return res