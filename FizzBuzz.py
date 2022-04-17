# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz",

# This is the answer for the first question in the progress sheet!
# The question is also described above yet you can refer leetcode for deep observation.
         
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range (1,n+1): 
            if (i%3==0 and i%5==0):
                 answer.append("FizzBuzz")
            elif (i%3==0):
                 answer.append("Fizz")
            elif(i%5==0):
                 answer.append("Buzz")
            else:
                 answer.append(str(i))
      
        return answer
