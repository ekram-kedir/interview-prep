class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        value = []
        for i in range(n):
            value.append(start + 2 * i)
            
        XOR = value[0]
        for i in range(1,len(value)):
            XOR = XOR ^ value[i]
        
        return XOR