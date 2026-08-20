# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKListsBruteForce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head

        visited = set()
        k = len(lists)
        counter = len(lists)
        
        while counter > 0:

            # chose a node among k
            chosen = ListNode(float("inf"))
            index = None

            for i in range(k):
                if i in visited:
                    continue
                elif lists[i] is None:
                    visited.add(i)
                    counter -= 1
                elif lists[i].val < chosen.val:
                    chosen = lists[i]
                    index = i

            # update dummy to point to the next one
            if index is None:
                continue

            dummy.next = chosen
            dummy = dummy.next
            lists[index] = lists[index].next

            # reduce counter if chosen list is empty
            if lists[index] is None:
                counter -= 1
                visited.add(index)
        
        return head.next

    # Fastest, time = O(Nlogk)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        head = ListNode()
        dummy = head

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            _, i , nextNode = heapq.heappop(heap)
            
            dummy.next = nextNode
            dummy = dummy.next

            if nextNode.next is not None:
                heapq.heappush(heap, (nextNode.next.val, i, nextNode.next))
        
        return head.next
    
    # space == O(1), time == O(Nk)
    def mergeKListsInPlace(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(
                    lists[i],
                    lists[i + interval]
                )
            interval *= 2

        # # or 
        # while interval < len(lists):

        #     i = 0
        #     while i + interval < len(lists):
        #         lists[i] = mergeTwoLists(
        #             lists[i],
        #             lists[i + interval]
        #         )
        #         i += 2 * interval
        #         interval *= 2
                    
        #         return lists[0]


    def mergeTwoLists(l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next



        






