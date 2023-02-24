class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decStack = []
        answer = [0] * len(temperatures)
        
        for temp in range(len(temperatures)):
            
            while decStack and temperatures[decStack[-1]] < temperatures[temp]:
                day = decStack.pop()
                answer[day] = temp - day
            decStack.append(temp)
                
        return answer