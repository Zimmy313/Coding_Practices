from typing import *

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        pointer = head
        pre = None
        table = {}
        
        while pointer: # first pass, setting next
            copy = Node(x = pointer.val)
            
            if pre:
                pre.next = copy
            
            # updating
            pre = copy 
            table[pointer] = copy 
            pointer = pointer.next 
        
        pointer = head 
        
        while pointer: # second pass, setting random
            current = table[pointer]
            current.random = table.get(pointer.random) # get() avoids getting None

            pointer = pointer.next
        return table[head]
        
        