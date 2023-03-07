# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValid(root.left , root.right)
        
    def isValid(self ,leftNode , rightNode):
        if not leftNode and not rightNode:
            return True
        
        if (not leftNode) or (not rightNode) or (leftNode.val != rightNode.val):
            return False
        
        evaluate_leftNode = self.isValid(leftNode.left , rightNode.right)
        evaluate_rightNode = self.isValid(leftNode.right , rightNode.left) 
        
        return evaluate_leftNode and evaluate_rightNode        
        
            
            
            
     