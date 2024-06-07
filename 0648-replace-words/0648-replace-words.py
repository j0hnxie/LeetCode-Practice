class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        dict_set = set(dictionary)
        
        sentence = sentence.split(" ")
        res = ""
        for word in sentence:
            found = False
            for root in dictionary:
                if root == word[:len(root)]:
                    # print("Found " + root + " in " + word)
                    res += root + " "
                    found = True
                if found:
                    break
            if not found:
                res += word + " "
        return res[:-1]