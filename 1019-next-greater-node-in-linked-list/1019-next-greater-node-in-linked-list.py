# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        currind=0
        res=[]
        stack=[]
        while head:
            res.append(0)
            while stack and stack[-1][1]<head.val:
                newind,nodeval=stack.pop()
                res[newind]=head.val
            stack.append((currind, head.val))
            currind+=1
            head=head.next
        return res