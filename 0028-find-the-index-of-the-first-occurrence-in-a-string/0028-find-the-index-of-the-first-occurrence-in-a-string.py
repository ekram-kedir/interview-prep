class Solution:
    def calculate(self , alphabets , length):
        
        offset = 96
        result = 0
        for index in range(len(alphabets)):
            result += (ord(alphabets[index]) - offset) * (27**(length - index - 1))
        return result
        
    def pollFirst(self, alphabet , result , length):
        
        offset = 96
        return result - ((ord(alphabet) - offset) * (27**(length - 1)))
      
        
    def addLast(self, currentAlphabet, result, length):
                           
        offset = 96 
        return result * (27) + (ord(currentAlphabet) - offset)
                           
        
    def strStr(self, haystack: str, needle: str) -> int:
                           
        length = len(needle)          
        hash_code_needle = self.calculate(needle , length)
        hash_code_haystack = self.calculate(haystack[:length] , length)
        left = 0
                                            
        if hash_code_needle ==  hash_code_haystack:
                return 0
            
        for left in range(len(haystack) - length):
                                            
            hash_code_haystack = self.pollFirst(haystack[left] ,hash_code_haystack , length )
            hash_code_haystack = self.addLast( haystack[left + length] ,hash_code_haystack , length)
            
            if hash_code_needle == hash_code_haystack:
                    return left + 1
        return -1
            

                                 