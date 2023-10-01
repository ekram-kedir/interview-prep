class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

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
            node.count += 1
        
    def search(self, word: str) -> bool:
        
        answer = 0
        root = self.root
        for w in word:
            index = ord(w) - ord("a")
            if not root.children[index]:
                return answer
            root = root.children[index]
            answer += root.count
        return answer
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for w in words:
            trie.insert(w)
        return [trie.search(w) for w in words]