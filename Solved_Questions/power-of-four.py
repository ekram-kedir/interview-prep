# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
##########################_Solution_for_power-of-four_#############################
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count=0
        current=0
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while current==0 and n>1:
                current =n%4
                n=n//4
        if current!=0:
            return False
        return True
