class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count = Counter(deck)
        val = [v for k,v in count.items()]
        
        if len(deck) == 1:
            return False
        
        for i in range(1,len(val)):
            if self.gcd(val[i - 1],val[i]) < 2:
                return False
        return True
    
        
    def gcd(self,a , b):
            if b == 0 :
                return a

            return self.gcd(b , a % b)
        
        
        