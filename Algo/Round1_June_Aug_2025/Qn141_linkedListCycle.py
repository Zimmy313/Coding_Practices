from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        fast, slow = head, head 
        
        while True:
            fast = fast.next
            if fast == None:
                return False 
            fast = fast.next
            slow = slow.next
            
            if fast == slow:
                return True 
            
            elif fast == None or slow == None:
                return False 
        


if __name__ == "__main__":
    s = Solution()

    print(s)