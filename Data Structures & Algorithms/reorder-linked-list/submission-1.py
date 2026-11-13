# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # after this loop, slow will be the middle of the list
        second = slow.next
        slow.next = None

        # Reverse the linked list
        prev = None
        while second:
            after = second.next
            second.next = prev
            prev = second
            second = after

        # this will reverse the linked list
        # second will None
        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return

            
        