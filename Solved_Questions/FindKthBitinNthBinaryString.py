# Given two positive integers n and k, the binary string Sn is formed as follows:

# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first four strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

# ANSWER

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return '0'
            res = helper(n - 1)
            ans = res[::-1]
            strr = ''
            for i in range(len(ans)):
                if ans[i] == '1':
                    strr += '0'
                else:
                    strr += '1'
            ans = res + '1' + strr
            return ans
        answer = helper(n)
        return answer[k - 1]
