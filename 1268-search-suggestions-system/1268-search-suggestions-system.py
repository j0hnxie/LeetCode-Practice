class Trie:
    class Node:
        def __init__(self):
            self.done = False
            self.children = [None for i in range(26)]
        
    
    def __init__(self):
        self.res = []
        self.root = self.Node()
    
    def insert(self, word):
        cur = self.root
        for char in word:
            index = ord(char) - 97
            if not cur.children[index]:
                cur.children[index] = self.Node()
            cur = cur.children[index]
        cur.done = True
        
    def dfs(self, cur, word):
        if not cur:
            return
        if len(self.res) == 3:
            return
        
        if cur.done:
            self.res.append(word)
        
        for i in range(26):
            word += chr(i + 97)
            self.dfs(cur.children[i], word)
            word = word[:-1]
    
    def genPre(self, pre):
        self.res = []
        
        cur = self.root
        for char in pre:
            index = ord(char) - 97
            if not cur.children[index]:
                return []
            cur = cur.children[index]
        
        self.dfs(cur, pre)
        return self.res
    


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        
        for product in products:
            t.insert(product)
        
        res = []
        pre = ""
        for char in searchWord:
            pre += char
            res.append(t.genPre(pre))
        
        return res