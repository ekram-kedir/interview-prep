# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# ANSWER

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=set()
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in res:
                res.remove(s[l])
                l+=1
            res.add(s[i])
            ans=max(i-l+1,ans)
        return ans
