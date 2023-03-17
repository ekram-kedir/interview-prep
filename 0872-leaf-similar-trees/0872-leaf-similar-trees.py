# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self , root , path):
        if not root:
            return 
        
        if not root.left and not root.right:
            path.append(root.val)
            
        else:
            self.path(root.left , path)
            self.path(root.right , path)
            
        return path
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        result1 = self.path(root1 , [])
        result2 = self.path(root2 , [])
        
        return result1 == result2        