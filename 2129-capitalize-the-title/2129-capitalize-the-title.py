class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        answer = ""
        array = title.split()
        
        for index in range(len(array)):
            if len(array[index]) == 1 or len(array[index]) == 2:
                answer += array[index].lower()
            else:
                answer += array[index].capitalize()
            answer += " "
            
        return answer[:-1]