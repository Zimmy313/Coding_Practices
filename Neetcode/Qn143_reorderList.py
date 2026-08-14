# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
            
        # reverting the second half
        second = slow.next
        
        # imporatant line to avoid loop
        slow.next = None
        
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            
            prev = second 
            second = nxt 
            
        second = prev
        first = head 
        
        # merging the 2
        while second:
            
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next
        
        
        
        
        
        
        
    
    # own attempt. space complexity == O(N). can be reduced to O(1)
    def reorderList_self(self, head: Optional[ListNode]) -> None:
        pointers = []
        dummy = head

        # populating a list of pointers
        while dummy is not None:
            pointers.append(dummy)
            dummy = dummy.next 
        
        
        n = len(pointers)
        turn = 0
        dummy = head
        counter = 0

        for i in range(n):

            if turn == 0:
                dummy.next = pointers[counter]
                dummy = dummy.next
                turn = 1
                counter += 1
            else:
                dummy.next = pointers[n - counter]
                dummy = dummy.next
                turn = 0
        
        # important step to remove self loops. old link still exist otherwise
        dummy.next = None
        
        
        return