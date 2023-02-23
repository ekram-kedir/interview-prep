class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = len(s)
        prefixSum = [0] *(l + 1)
        for begin , end , direction in shifts:
            if direction == 0:
                add = -1
            else:
                add = 1
            prefixSum[begin] += add
            prefixSum[end + 1] -= add
        for num in range(1,len(prefixSum)):
            
            prefixSum[num] += prefixSum[num - 1]
        result = []
        offset = ord('a')

        for shift in range(l):
            shifted = (ord(s[shift]) - offset + prefixSum[shift]) % 26
            
            result.append(chr(shifted+offset))
        return "".join(result)
            
      
        
            
            
                