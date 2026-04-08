# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        # first move head to n
        tracker = dummy
        count = 0

        while count < n + 1:
            tracker = tracker.next
            count += 1

        current = dummy
        while tracker:
            current = current.next
            tracker = tracker.next
        
        temp = current
        next_val = current.next.next
        temp.next = next_val

        return dummy.next

        