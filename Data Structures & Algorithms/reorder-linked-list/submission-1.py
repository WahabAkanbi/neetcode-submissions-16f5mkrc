# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #split the link list in half

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slows end up in the middle
        new_head = slow.next
        slow.next = None

        #reverse the second half
        previous = None
        current = new_head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp


        #previous has the second half head
        new_head = previous
        #remerge

        dummy = ListNode()
        new = dummy
        toggle = False

        while head and new_head:
            if not toggle:
                new.next = head
                head = head.next
                toggle = True
            else:
                new.next = new_head
                new_head = new_head.next
                toggle = False
            new = new.next

        if head:
            new.next = head
        if new_head:
            new.next = new_head



        