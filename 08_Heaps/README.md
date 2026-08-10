# Unit 08: Heaps

## Overview

This unit focuses on **Heaps** and **Priority Queues**, essential data structures for efficiently managing elements based on priority.

Heaps are particularly useful in problems involving **Kth largest/smallest elements, Top K elements, scheduling, priority-based processing, and streaming data**.

---

## Objectives

By the end of this unit, you will be able to:

- Understand Min Heap and Max Heap structures.
- Understand heap properties and operations.
- Use Python's `heapq` module effectively.
- Implement and work with Priority Queues.
- Recognize when a heap provides an optimal solution.
- Solve common heap-based interview problems.

---

## Topics Covered

- Heap Fundamentals
- Min Heap
- Max Heap
- Heapify
- Heap Push & Pop
- Priority Queue
- Kth Largest Element
- Kth Smallest Element
- Top K Frequent Elements
- Merge K Sorted Lists
- Median from Data Stream

---

## Key Patterns

- Min Heap
- Max Heap
- Top K Pattern
- Kth Element Pattern
- Priority Queue
- Two Heaps
- Heap-based Selection

---

## Folder Structure

```text
08_Heaps/
├── heap_basics.py
├── priority_queue.py
├── kth_largest_element.py
├── kth_smallest_element.py
├── top_k_frequent_elements.py
├── merge_k_sorted_lists.py
├── find_median_from_data_stream.py
└── README.md
```

---

## Problems Included

| File | Concept |
|------|---------|
| `heap_basics.py` | Min Heap, Max Heap & heap operations |
| `priority_queue.py` | Priority Queue using `heapq` |
| `kth_largest_element.py` | Kth largest element using Min Heap |
| `kth_smallest_element.py` | Kth smallest element using Max Heap |
| `top_k_frequent_elements.py` | Top K pattern with frequency counting |
| `merge_k_sorted_lists.py` | Heap-based merging |
| `find_median_from_data_stream.py` | Two Heap technique |

---

## Common Complexities

| Operation | Complexity |
|-----------|------------|
| Peek | O(1) |
| Push | O(log n) |
| Pop | O(log n) |
| Heapify | O(n) |
| Search | O(n) |

Space Complexity is generally **O(n)** for storing the heap.

---

## Python Implementation

Python provides the `heapq` module for heap operations.

```python
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

smallest = heapq.heappop(heap)
```

> `heapq` implements a **Min Heap** by default.

A Max Heap can be simulated by storing negative values.

---

## Learning Outcome

After completing this unit, you will be able to:

- Implement and manipulate heaps confidently.
- Use `heapq` for efficient priority-based operations.
- Identify Top K and Kth element patterns.
- Apply heaps to real interview problems.
- Understand when to choose a heap over sorting.
- Explain heap-based solutions and their complexity during interviews.

---

## Prerequisites

Before starting this unit, you should be comfortable with:

- Arrays & Strings
- Hashing
- Stacks & Queues
- Recursion
- Trees
- Time & Space Complexity

---

## Next Unit

➡ **Unit 09: Graphs**
