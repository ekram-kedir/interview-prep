# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = self.takeOrder(root)
        
        return result[k - 1] 
    
    def takeOrder(self,root):
        
        if not root:
            
            return []
        
        leftcall = self.takeOrder(root.left)
        rightcall = self.takeOrder(root.right)
        
        return leftcall + [root.val] + rightcall
    
        
        
        
        