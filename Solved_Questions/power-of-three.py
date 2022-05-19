# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Example 2:

# Input: n = 0
# Output: false
#######################_Soltion_for_power-of-three_#############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        count=0
        current=0
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while current==0 and n>1:
                current =n%3
                n=n//3
        if current!=0:
            return False
        return True
