# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        counter = 0

        pointer = None

        while dummy.next:
            counter += 1
            dummy = dummy.next

            if counter <= n:
                continue

            if pointer is None:
                pointer = head
            else:
                pointer = pointer.next
        
        if pointer is None:
            return head.next
        else:
            temp = pointer.next
            pointer.next = temp.next
            temp.next = None
            return head

        
        

