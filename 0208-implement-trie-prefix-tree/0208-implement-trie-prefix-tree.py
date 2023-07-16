class Trie(object):
    def __init__(self):
        self.root = {}
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char in cur:
                cur = cur[char]
            else:
                cur[char] = {}
                cur = cur[char]
        cur[0] = {}
            
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char in cur:
                cur = cur[char]
            else:
                return False
            
        return 0 in cur
        
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if char in cur:
                cur = cur[char]
            else:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)