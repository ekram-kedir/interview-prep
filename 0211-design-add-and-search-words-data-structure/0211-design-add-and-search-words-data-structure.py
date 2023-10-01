class WordNode:
    def __init__(self):
        
        self.children = {}
        self.is_end_of_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        
        root = self.root
        
        for w in word:
            if w not in root.children:
                root.children[w] = WordNode()
            root = root.children[w]
            
        root.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        
        def dfs(index , root):
            
            for w in range(index ,len(word)):
                alphabet = word[w]
                
                if alphabet == ".":
                    for child in root.children.values():
                        if dfs(w + 1 , child):
                            return True
                    return False
                
                else:
                    if alphabet not in root.children:
                        return False
                    root = root.children[alphabet]
                    
            return root.is_end_of_word
        return dfs(0 , self.root)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)