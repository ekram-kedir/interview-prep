# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def helper(root1,root2):
            
            if root1 is None and root2 is None:
                return True
            
            elif root1 is None or root2 is None:
                return False
            
            if (root1.val == root2.val):
                
                res = helper(root1.left , root2.right) and helper(root1.right , root2.left) 
                result = helper(root1.left , root2.left) and helper(root1.right , root2.right)
                return res or result
        return helper(root1,root2)