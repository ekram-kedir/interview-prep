# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root,answer):
        
        if not root:
            return 
        
        answer += str(root.val)
        
        if not root.left and not root.right:
            self.result += int(answer)
        
        if root.left:
           
             self.dfs(root.left , answer)
            
            
        if root.right:
            
            self.dfs(root.right , answer)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        if root:
            self.dfs(root,"")

        return self.result