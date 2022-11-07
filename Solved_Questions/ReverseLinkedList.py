# Given the head of a singly linked list, reverse the list, and return the reversed list.

# ANSWER

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                self.head=head;
                p1=None;
                while(head!=None):
                    p2=head.next
                    head.next=p1
                    p1=head
                    head=p2

                head=p1
                return head
