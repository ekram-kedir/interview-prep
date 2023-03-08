# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root , row, col):
        if not root:
            return 
        self.take[col].append((row,root.val))
        
        self.helper(root.left , row + 1, col - 1)
        self.helper(root.right ,row + 1 , col + 1)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.take = defaultdict(list)
        self.helper(root , 0 , 0)
        
        answer = []
        
        for key in sorted(self.take.keys()):
            
            self.take[key].sort()
            answer.append(j for (i,j) in self.take[key])
            
        return answer