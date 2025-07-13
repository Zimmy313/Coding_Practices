from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        pointer = head 
        result = []
        
        while pointer:
            result.append(pointer.val)
            pointer = pointer.next
        result.sort()
        
        head1 = ListNode(val = result[0])
        pointer = head1 
        for i in range(1,len(result)):
            next = ListNode(val = result[i])
            pointer.next = next
            pointer = next            
        
        return head1