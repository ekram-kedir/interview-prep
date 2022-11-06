# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# ANSWER
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def helper(x,n):
                if x==0:
                    return 0
                elif x==1 or n==0:
                    return 1
                ans=helper(x,n//2)
                ans=ans*ans
                return x*ans if n%2 else ans
            
        ans=helper(x,abs(n))
        return ans if n>=0 else 1/ans
