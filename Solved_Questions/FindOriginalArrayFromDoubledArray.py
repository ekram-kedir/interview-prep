# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        l=len(changed)
        if l%2:
            return []
        changed.sort()
        k=Counter(changed)
        ans=[]
        for i in changed:
            if i==0 and k[i]>=2:
                k[i]-=2
                ans.append(i)
            elif i>0 and k[i] and k[i*2]:
                k[i]-=1
                k[i*2]-=1
                ans.append(i)
        if len(ans)==l/2:
            return ans
        return []
