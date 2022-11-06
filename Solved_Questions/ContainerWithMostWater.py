# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# ANSWER

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        ans=0
        while l<r:
            if height[l]<height[r]:
                area=(r-l)*(height[l])
                l+=1
            else:
                area=(r-l)*(height[r])
                r-=1
            ans=max(ans,area)
        return ans
            
            
