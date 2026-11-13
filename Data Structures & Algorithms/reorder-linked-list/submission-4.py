# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # after loop is done the slow pointer is in the mmiddle of the list
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # now the the staring point of first part of list is head
        # the starting point of second part of list is prev

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

