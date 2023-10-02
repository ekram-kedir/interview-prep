class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        answer = ""
        
        for alphabet in s:
            if stack:
                if alphabet == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                elif alphabet != stack[-1][0]:
                    stack.append([alphabet , 1])
            else:
                stack.append([alphabet, 1])
                
        for a,b in stack:
            answer += a * b
            
        return answer