class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        answer = []
        
        if num % 3 == 0:
            result = int(num / 3) 
            answer.append(result - 1)
            answer.append(result)
            answer.append(result + 1)
            return answer
        else:
            return answer