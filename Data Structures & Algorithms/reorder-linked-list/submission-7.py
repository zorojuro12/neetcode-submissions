# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow.next
        prev = None
        slow.next = None
        list1 = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        list2 = prev

        dummy = ListNode()
        while list2:
            tmp1 = list1.next
            tmp2 = list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2
        return



         