# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        back = dummy
        front = dummy
        counter = 1
        while counter <= n:
            back = back.next
            counter += 1
        while back.next:
            back = back.next
            front = front.next
        front.next = front.next.next
        return dummy.next