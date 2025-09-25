from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2 
        carry = 0 # either 0 or 1
        dummy = ListNode(0)
        pointer = dummy 
        
        while p1 or p2 or carry : # continue as long as any of this is not 0 
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            cur_sum = val1 + val2 + carry 
            
            if cur_sum >= 10:
                x = cur_sum % 10 
                carry = 1
                
                temp = ListNode(x)
                pointer.next = temp 
                pointer = temp
            
            else:
                carry = 0
                temp = ListNode(cur_sum)
                pointer.next = temp 
                pointer = temp 
            
            if p1: p1 = p1.next 
            if p2: p2 = p2.next 
            
        
        return dummy.next 
    
                
            
            
                
                
                
    
                
            
            
                
                
                