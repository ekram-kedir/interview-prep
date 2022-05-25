# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
######################_Solution_For_ReverseLinkedlist_##################################
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
