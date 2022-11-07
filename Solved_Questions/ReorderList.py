# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# ANSWER

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l,r=head,head.next
        while r and r.next:
            l=l.next
            r=r.next.next
        curr=l.next
        prev=l.next=None
        while curr:
            ans=curr.next
            curr.next=prev
            prev=curr
            curr=ans
        i,j=head,prev
        while j:
            res1,res2=i.next,j.next
            i.next=j
            j.next=res1
            i,j=res1,res2
