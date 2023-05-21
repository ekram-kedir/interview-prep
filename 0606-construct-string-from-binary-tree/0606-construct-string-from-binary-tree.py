# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root, answer):
        
        if not root:
            return answer
        
        answer += str(root.val)
        
        if not root.left and not root.right:
            return answer
        
        if root.left:
            answer += "("
            answer = self.dfs(root.left , answer)
            answer += ")"
        else:
            answer += "("
            answer += ")"
            
        if root.right:
            
            answer += "("
            answer = self.dfs(root.right , answer)
            answer += ")"
        
            
            
        return answer
            
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if root:
            return self.dfs(root , "")
        return
            
      
        return ""