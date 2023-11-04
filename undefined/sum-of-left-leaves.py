# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            
            if not root:
                return 0
            total = 0
                   
            if root.left and not root.left.right and not root.left.left:
                    total = root.left.val 
                
            return total + helper(root.left) + helper(root.right)
        
        return helper(root)