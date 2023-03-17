# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        queue = deque([[root,0]])

        maxResult = 0
        
        while queue:
            
            allow = len(queue)
            ans = []
            
            while allow > 0:
              
                [take,col]= queue.popleft()
                ans.append([take.val,col])
                
                if take.left:
                    queue.append([take.left , col * 2 + 1])
                if take.right:
                    queue.append([take.right , col * 2 + 2])
                    
                allow-=1
            maxResult = max((ans[-1][1] - ans[0][1]) + 1,maxResult)
        return maxResult