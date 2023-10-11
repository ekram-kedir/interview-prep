class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        dic = {}
        offset = 96
        calculate = 0
        answer = []
        c  = 0
        j  = len(s)- 1
        
        while j  >= len(s) - k:
            
            c+=1
            calculate += (ord(s[j]) - offset) * (pow(power, k-c,modulo))
            j-=1
            
        calculate %= (modulo)
        if (calculate % modulo) == hashValue: 
            answer.append((len(s)- k, len(s)))
            
        for ptr in range(len(s) - 1,-1,-1):
            calculate  -= ((ord(s[ptr]) - offset)) * pow(power , k - 1,modulo)
            calculate *= power
            calculate += (ord(s[ptr - k]) - offset)
            if ptr - k < 0:
                break
                
            if (calculate % modulo) == hashValue: 
                answer.append((ptr- k ,ptr ))
            calculate %= (modulo)
        index1 = answer[-1][0]
        index2 = answer[-1][1]
        return s[index1:index2]
