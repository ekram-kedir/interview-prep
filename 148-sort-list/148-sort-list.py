# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l=head
        r=self.middle(head)
        curr=r.next
        r.next=None
        r=curr
        l=self.sortList(l)
        r=self.sortList(r)
        return self.merge(l,r)
    def middle(self,head):
        l,r=head,head.next
        while r and r.next:
            l=l.next
            r=r.next.next
        return l
    def merge(self,ans,res):
        tail=tmp=ListNode()
        while ans and res:
            if ans.val<res.val:
                tail.next=ans
                ans=ans.next
            else:
                tail.next=res
                res=res.next
            tail=tail.next
        if ans:
            tail.next=ans
        if res:
            tail.next=res
        return tmp.next