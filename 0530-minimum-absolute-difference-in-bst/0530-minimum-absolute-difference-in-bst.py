# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self , root):
        
        if not root:
            return []
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        return left + [root.val] + right
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        result = self.traverse(root)
        difference = 0
        minResult = max(result)
        
        for idx in range(1 , len(result)):
            
            difference = result[idx] - result[idx - 1]
            minResult = min(difference , minResult)
            
        return minResult
              