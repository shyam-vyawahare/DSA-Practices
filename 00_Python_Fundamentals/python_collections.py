"""
python_collections.py
Purpose: DSA-focused overview of Python collections with common operations
Author: Your Name
"""

# =========================
# LIST (Dynamic Array)
# =========================
nums = [1, 2, 3, 4]

# Access
first = nums[0]              # O(1)
last = nums[-1]              # O(1)

# Insert / Delete
nums.append(5)               # O(1) amortized
nums.pop()                   # O(1)
nums.insert(1, 10)           # O(n)
nums.remove(3)               # O(n)

# Traversal
for i in range(len(nums)):   # O(n)
    _ = nums[i]

for x in nums:               # O(n)
    _ = x

# Common DSA usage
# - Arrays, sliding window, two pointers


# =========================
# DICTIONARY (Hash Map)
# =========================
freq = {}

# Insert / Update
freq["a"] = 1                # O(1) average
freq["a"] += 1               # O(1) average

# Access
count_a = freq.get("a", 0)   # O(1) average

# Check existence
if "a" in freq:              # O(1) average
    pass

# Traversal
for key, value in freq.items():  # O(n)
    _ = key, value

# Common DSA usage
# - Frequency counting
# - Fast lookups
# - Prefix sums, hashing problems


# =========================
# SET (Unique Elements)
# =========================
unique_nums = set()

# Insert
unique_nums.add(1)           # O(1) average
unique_nums.add(2)

# Check existence
exists = 1 in unique_nums    # O(1) average

# Remove
unique_nums.remove(2)        # O(1) average (KeyError if missing)
unique_nums.discard(3)       # O(1) average (safe)

# Traversal
for x in unique_nums:        # O(n)
    _ = x

# Common DSA usage
# - Removing duplicates
# - Fast membership checks
# - Intersection / union problems


# =========================
# TUPLE (Immutable)
# =========================
point = (2, 3)

x = point[0]                 # O(1)
y = point[1]                 # O(1)

# Tuple unpacking
a, b = point

# Common DSA usage
# - Coordinates
# - Fixed pairs
# - Keys in dictionaries


# =========================
# PYTHONIC HELPERS (DSA GOLD)
# =========================

# enumerate -> index + value
for idx, val in enumerate(nums):  # O(n)
    _ = idx, val

# zip -> parallel traversal
a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):            # O(n)
    _ = x + y

# List comprehension
squares = [x * x for x in nums]   # O(n)

# Dictionary comprehension
square_map = {x: x * x for x in nums}  # O(n)


# =========================
# QUICK COMPLEXITY SUMMARY
# =========================
"""
List:
- Access: O(1)
- Append: O(1) amortized
- Insert/Delete (middle): O(n)

Dict / Set:
- Insert, Delete, Lookup: O(1) average

Tuple:
- Access: O(1)
- Immutable (safe, hashable)
"""
