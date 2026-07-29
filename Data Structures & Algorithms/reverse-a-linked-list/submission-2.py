# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revhead = None
        temp = head
        while temp != None:
            next_node = temp.next
            temp.next = revhead
            revhead = temp
            temp = next_node
        return revhead