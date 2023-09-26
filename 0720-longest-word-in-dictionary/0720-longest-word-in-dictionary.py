class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        for w in word:
            index = ord(w) - ord("a")
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        
        root = self.root
        for w in word:
            index = ord(w) - ord("a")
            if not root.children[index]:
                return False
            root = root.children[index]
        return root.is_end_of_word
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
         
        longest = ""
        mTrie = Trie()
        words.sort()
        
        for word in words:
            if len(word) == 1 or mTrie.search(word[:-1]):
                mTrie.insert(word)
                if len(word) > len(longest):
                    longest = word
                
        return longest
            
        





        
