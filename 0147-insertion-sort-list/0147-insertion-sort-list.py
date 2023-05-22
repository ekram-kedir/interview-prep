# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=ListNode(0,head)
        l,r=head,head.next
        while r:
            if r.val>=l.val:
                l,r=r,r.next
                continue
            curr=tmp
            while r.val>curr.next.val:
                curr=curr.next
            l.next=r.next
            r.next=curr.next
            curr.next=r
            r=l.next
        return tmp.next