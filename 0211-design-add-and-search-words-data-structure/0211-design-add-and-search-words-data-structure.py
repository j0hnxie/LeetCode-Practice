class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        self.tracker = set()

    def addWord(self, word: str) -> None:
        if word in self.tracker:
            return
        else:
            self.tracker.add(word)

        cur_node = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not cur_node.children[idx]:
                cur_node.children[idx] = Node()

            cur_node = cur_node.children[idx]
        
        cur_node.word = True
            
    def search(self, word: str) -> bool:
        if word in self.tracker:
            return True
        
        def dfs(cur_node, cur_string):
            if not cur_node:
                return False

            if not cur_string:
                return cur_node.word

            cur_char = cur_string[0]
            if cur_char == ".":
                return any([dfs(cur_node.children[idx], cur_string[1:]) for idx in range(26)])
            else:
                idx = ord(cur_char) - ord('a')
                return dfs(cur_node.children[idx], cur_string[1:])
        
        return dfs(self.root, word)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)