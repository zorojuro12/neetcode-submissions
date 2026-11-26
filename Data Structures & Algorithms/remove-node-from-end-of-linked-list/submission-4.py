# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        tail = curr.next

        while n != 0:
            tail = tail.next
            n -= 1

        while tail:
            curr = curr.next
            tail = tail.next

        tmp = curr.next.next
        curr.next = tmp
        return dummy.next