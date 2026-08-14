# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head.next
        if slow is not None:
            fast = slow.next

        while slow is not None and fast is not None:

            if fast == slow:
                return True
            
            slow = slow.next
            
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False

        return False
