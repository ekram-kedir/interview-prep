# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# ANSWER

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, s1, s2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node=ListNode()
        tail=node
        while s1 and s2:
            if s1.val<s2.val:
                tail.next=s1
                s1=s1.next
            else:
                tail.next=s2
                s2=s2.next
            tail=tail.next
        if s1:
            tail.next=s1
        elif s2:
            tail.next=s2
        return node.next
