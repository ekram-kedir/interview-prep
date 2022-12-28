class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        compare = {}
        for idx,val in enumerate(order):
            compare[val] = idx
        find = []
        for w in words:
            check = []
            for alpha in w:
                check.append(compare[alpha])
            find.append(check)
        for letter in range(len(find)-1):
            if find[letter + 1] < find[letter]:return False
            
        return True
        
        
       
        
             