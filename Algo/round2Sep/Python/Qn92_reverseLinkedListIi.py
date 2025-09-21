from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        
        # setting pre to the node beore left'th node
        for _ in range(left-1):
            pre = pre.next 
        
        # swapping. pre and current do not change, only their .next and temp change
        curr = pre.next
        for _ in range(right - left):
            temp = curr.next 
            curr.next = temp.next 
            temp.next = pre.next 
            pre.next = temp
        
        return dummy.next
                
            
        