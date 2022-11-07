# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=[]
        cur=head
        while cur is not None:
            ans.append(cur.val)
            cur=cur.next
        t=0
        for i in range(len(ans)):
            t=max(t,ans[i]+ans[len(ans)-i-1])
        return t