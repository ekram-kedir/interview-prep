# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        
        if not root:
            return 
        
        queue = deque([root])
        answer = []
        
        while queue:
            
            allow = len(queue)
            ans = []
            while allow > 0:
                
                take = queue.popleft()
                ans.append(take.val)
                
                if take.left:
                    queue.append(take.left)
                if take.right:
                    queue.append(take.right)
                    
                allow-=1
                
            answer.append(ans)
        return answer
                    
        