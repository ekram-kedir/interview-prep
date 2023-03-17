# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
       
        return self.traverse(root , 0 , targetSum )
    
    def traverse(self , root , val , targetSum):
        if not root:
            return
        
        result= 0
        val += root.val
        
       
        if val == targetSum and not root.left and not root.right:
            return True
        
        else:
       
            if root.left:
                result = result or self.traverse(root.left , val , targetSum)
                
            if root.right:
                result = result or self.traverse(root.right , val , targetSum)
                
        return result