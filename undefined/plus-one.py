class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        numbers = ""
        for d in digits:
            numbers += str(d) 
            
        answer = []
        for n in str(int(numbers) + 1):
            answer.append(int(n))
            
        return answer