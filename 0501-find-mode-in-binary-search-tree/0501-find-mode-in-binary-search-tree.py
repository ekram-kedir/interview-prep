# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count  = Counter(self.inOrder(root))
        mode = max(count.values())
        ans = []  
        
        for k,v in count.items():
            if v == mode:
                ans.append(k)
        return ans
                                                                          
        
    def inOrder(self,root):
        if not root:
            return []
        
        leftcall = self.inOrder(root.left)
        rightcall = self.inOrder(root.right)
        
        return leftcall + [root.val] + rightcall 
        