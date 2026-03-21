from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # O(nlogn) 
        def list_to_linkedlist(lst):
            dummy = ListNode(0)     # dummy node 
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next       # return head 
        
        result = []
        for i in lists:
            while i:
                result.append(i.val)
                i = i.next
        result.sort()

        head = list_to_linkedlist(result)
        
        return(head)
        
        
        
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # using heap but not efficient enough
        import heapq
        
        h = []
        n = len(lists)
        skip = set()
        
        for i in range(n):
            if lists[i] is None:
                skip.add(i)
            
            elif i in skip:
                continue 
            
            else:
                current = lists[i]
                next_node = current.next 
                
                # updating param
                heapq.heappush(h, current.val)
                lists[i] = next_node
                
        if len(h) == 0: 
            return 

        pointer = None
        
        while h:
            val = heapq.heappop(h)
            node = ListNode(val = val)
            
            if pointer is None:
                head = node
                pointer = head 
            
            else:
                pointer.next = node 
                pointer = node 
            
            # repopulate h
            for i in range(n):
                if lists[i] is None:
                    skip.add(i)
                
                elif i in skip:
                    continue 
                
                else:
                    current = lists[i]
                    next_node = current.next 
                    
                    # updating param
                    heapq.heappush(h, current.val)
                    lists[i] = next_node
        
        return head 
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # O(nlogk) best among the 3
        import heapq

        h = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, idx, node))  # val first for comparison. Using tuple so no need to recreate nodes later

        dummy = ListNode(0)
        pointer = dummy

        while h:
            val, idx, node = heapq.heappop(h)
            pointer.next = node
            pointer = pointer.next

            if node.next:
                heapq.heappush(h, (node.next.val, idx, node.next))

        return dummy.next

            
            
            
            
        