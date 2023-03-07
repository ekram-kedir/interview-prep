# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.minDepth(root.left) 
        rightDepth = self.minDepth(root.right) 
        
        if leftDepth != 0 and rightDepth != 0:
              return min(leftDepth,rightDepth) + 1
            
        return leftDepth + rightDepth + 1
        
        