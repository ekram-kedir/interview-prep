# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

 

# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"

# ANSWER
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        l=len(heights)
        heap=[]
        for i in range(l-1):
            dif=heights[i+1]-heights[i]
            if dif<=0:
                continue
            heappush(heap,dif)
            if len(heap)>ladders:
                mind=heappop(heap)
                bricks-=mind
            if bricks<0:
                return i
        return l-1

