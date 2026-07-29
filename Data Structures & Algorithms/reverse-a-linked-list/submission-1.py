# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revhead = None
        temphead = head
        while temphead != None:
            next_node = temphead.next
            temphead.next = revhead
            revhead = temphead
            temphead = next_node
        return revhead