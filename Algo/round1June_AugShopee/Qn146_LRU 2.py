from typing import *

class Node:
    def __init__(self, key, val):
        self.pre = None
        self.next = None 
        self.key = key
        self.val = val
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # key:node
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.pre = self.head

    def _add(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last 
        node.next = self.tail
        self.tail.pre = node

    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        current_node = self.cache[key]
        self._remove(current_node)
        self._add(current_node)
        return current_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if self.capacity == 0:
                # Evict least recently used
                lru = self.head.next
                self._remove(lru)
                self.cache.pop(lru.key)
            else:
                self.capacity -= 1

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
