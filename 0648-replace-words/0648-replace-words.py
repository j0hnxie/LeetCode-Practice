class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        dict_set = set(dictionary)
        
        sentence = sentence.split(" ")
        res = ""
        for word in sentence:
            found = False
            for idx in range(len(word)):
                if word[:idx] in dict_set:
                    res += word[:idx] + " "
                    found = True
                    break
            if not found:
                res += word + " "
            
        return res[:-1]