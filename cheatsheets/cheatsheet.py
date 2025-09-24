# =====================================
# String Manipulation
# =====================================
s = "LeetCode123"

s.isupper()           # Check if all characters are uppercase -> False
s.islower()           # Check if all characters are lowercase -> False
s.lower()             # Convert string to lowercase -> "leetcode123"
s.upper()             # Convert string to uppercase -> "LEETCODE123"
s.isdigit()           # Check if all characters are digits -> False
s.isalpha()           # Check if all characters are alphabets -> False
s.isalnum()           # Check if all characters are alphanumeric -> True
s.isspace()           # Check if string contains only whitespace -> False
s.startswith("Lee")   # Check if string starts with substring -> True
s.endswith("123")     # Check if string ends with substring -> True
s.strip()             # Remove leading and trailing whitespace
s.lstrip()            # Remove leading whitespace
s.rstrip()            # Remove trailing whitespace
s.split()             # Split string by whitespace -> ['LeetCode123']
s.split(',')          # Split string by a specific delimiter
",".join(["a", "b"])  # Join list into a string -> "a,b"
s.find("e")           # Return index of first occurrence -> 1
s.rfind("e")          # Return index of last occurrence -> 2
s.replace("Lee", "L33t")  # Replace substring -> "L33tCode123"

# =====================================
# List Operations
# =====================================
nums = [3, 1, 4, 1, 5]

nums.append(9)        # Add element to end -> [3,1,4,1,5,9]
nums.insert(2, 10)    # Insert at index -> [3,1,10,4,1,5,9]
nums.pop()            # Remove last element -> returns 9
nums.pop(2)           # Remove at index -> returns 10
nums.remove(1)        # Remove first occurrence of 1
nums.sort()           # Sort list in ascending order
nums.sort(reverse=True)  # Sort list in descending order
sorted(nums)          # Return a new sorted list without modifying original
nums.reverse()        # Reverse list in place
nums.index(4)         # Return index of first occurrence of 4
nums.count(1)         # Count occurrences of 1

# =====================================
# Set Operations
# =====================================
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(6)             # Add element to set
s1.update([7, 8])     # Add multiple elements
s1.remove(2)          # Remove element (error if not found)
s1.discard(10)        # Remove element (no error if not found)
s1.union(s2)          # Union -> {1,2,3,4,5,6,7,8}
s1.intersection(s2)   # Intersection -> {3}
s1.difference(s2)     # Difference -> elements in s1 but not in s2
s1.symmetric_difference(s2)  # XOR -> elements in one set but not both

# =====================================
# Dictionary Operations
# =====================================
d = {"a": 1, "b": 2}

d.keys()              # Return all keys
d.values()            # Return all values
d.items()             # Return (key, value) pairs
d.get("a", 0)         # Get value with default if key not found -> 1
d.pop("a")            # Remove key and return value
d.popitem()           # Remove last inserted key-value pair
d.update({"c": 3})    # Update dictionary with another dict

# Dictionary comprehension
squares = {x: x*x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# =====================================
# Math / Numbers
# =====================================
import math

abs(-5)               # Absolute value -> 5
pow(2, 3)             # 2^3 -> 8
round(3.14159, 2)     # Round to 2 decimal places -> 3.14
max(1, 5, 3)          # Maximum -> 5
min(1, 5, 3)          # Minimum -> 1
math.sqrt(16)         # Square root -> 4.0
math.ceil(2.3)        # Ceiling -> 3
math.floor(2.9)       # Floor -> 2

# =====================================
# Useful Built-ins
# =====================================
enumerate(['a', 'b'])    # -> [(0, 'a'), (1, 'b')]
zip([1, 2], ['a', 'b'])  # -> [(1, 'a'), (2, 'b')]
sum([1, 2, 3])           # Sum -> 6
any([False, True, False]) # True if any element is True
all([True, True, True])   # True if all elements are True
sorted([3,1,2])           # -> [1,2,3]
reversed([1,2,3])         # Reverse iterator

# =====================================
# Heap / Priority Queue
# =====================================
import heapq
heap = []
heapq.heappush(heap, 3)   # Add element
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)       # Pop smallest element -> 1
heapq.heapify(heap)       # Turn list into a heap

# =====================================
# Collections
# =====================================
from collections import Counter, deque, defaultdict

Counter("leetcode")       # Count elements -> {'l':1,'e':3,'t':1,'c':1,'o':1,'d':1}

dq = deque([1, 2, 3])
dq.append(4)              # Add to right
dq.appendleft(0)          # Add to left
dq.pop()                  # Remove from right
dq.popleft()              # Remove from left

dd = defaultdict(int)     # Default value = 0
dd["key"] += 1            # Automatically initializes missing key

# =====================================
# Itertools
# =====================================
from itertools import permutations, combinations, product

list(permutations([1, 2, 3]))         # All permutations
list(combinations([1, 2, 3], 2))      # All 2-element combinations
list(product([0, 1], repeat=3))       # Cartesian product