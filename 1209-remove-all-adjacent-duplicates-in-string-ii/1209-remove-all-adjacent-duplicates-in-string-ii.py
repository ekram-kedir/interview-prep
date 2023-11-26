class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [[s[0] , 1]]
        
        for idx in range(1,len(s)):
            if stack and  stack[-1][0] == s[idx] and stack[-1][1] < k - 1:
                stack[-1][1] += 1
            elif  stack and stack[-1][0] == s[idx] and stack[-1][1] == k - 1:
                stack.pop()
            elif  stack and stack[-1][0] != s[idx]:
                stack.append([s[idx] , 1])
            else:
                stack.append([s[idx] , 1])
        
        answer = ""
        for element, count in stack:
            answer += element * count
        return answer
            
                
                