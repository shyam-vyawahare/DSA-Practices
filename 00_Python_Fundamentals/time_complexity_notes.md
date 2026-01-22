# Time & Space Complexity Notes (DSA Fundamentals)

## Purpose
These notes provide a foundational understanding of **time complexity** and **space complexity** for Data Structures and Algorithms (DSA). The goal is to build the ability to **analyze, compare, and optimize algorithms** based on efficiency — a critical interview and real-world engineering skill.

---

## What is Time Complexity?
Time complexity describes **how the runtime of an algorithm grows** with respect to input size `n`.

It does not measure actual time in seconds — it measures **growth rate**.

---

## Big-O Notation (Core Focus)

| Notation | Meaning | Example |
|------|------|------|
| O(1) | Constant time | Accessing array index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutations |

---

## Common Python Examples

### O(1) – Constant
``python 
x = arr[0]
O(n) – Linear
for x in arr:
    print(x)

O(n²) – Quadratic
for i in arr:
    for j in arr:
        print(i, j)

Loop Analysis
Structure	Complexity
One loop	O(n)
Nested loop	O(n²)
Loop inside loop with different sizes	O(n × m)
Two separate loops	O(n + n) → O(n)
Recursive Complexity
Factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


Time: O(n)
Space: O(n) (call stack)

Fibonacci (Naive Recursion)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


Time: O(2ⁿ)
Space: O(n)

Space Complexity

Space complexity measures extra memory usage (not input size).

Examples:

List of size n → O(n)

Dictionary of size n → O(n)

Recursion depth n → O(n) stack space

Constant variables → O(1)

Python Data Structures (Average Case)
Structure	Insert	Delete	Lookup
List	O(1)*	O(n)	O(n)
Dict	O(1)	O(1)	O(1)
Set	O(1)	O(1)	O(1)

* append is O(1) amortized

Interview Rules for Complexity Analysis

Always state:

Time Complexity

Space Complexity

Worst-case scenario

Why this approach is optimal

Optimization Mindset
Convert:

Nested loops → Hashing

Recursion → Memoization / DP

Brute force → Sliding window / Two pointers

Recalculation → Prefix sum

Key Principles

Faster code ≠ better algorithm

Readability + efficiency > clever tricks

Clarity beats complexity

Optimization without logic = failure

Golden Rule

“First make it work, then make it right, then make it fast.”

DSA Interview Focus

Interviewers care about:

How you analyze complexity

How you optimize

How you explain trade-offs

How you choose data structures

Not memorization — reasoning.

Unit Connection

These concepts apply to every upcoming unit:

Arrays

Hashing

Trees

Graphs

DP

Greedy

Backtracking

Mastery here multiplies performance everywhere else.


---

## ✅ Unit 00 Status
Now officially complete:
- python_collections.py ✅  
- recursion_basics.py ✅  
- time_complexity_notes.md ✅  
- README.md ✅  

---

You’ve built **Unit 00** like a real engineering foundation layer — clean, structured, and scalable.
When ready, we continue with:
➡ **Unit 01 execution**
➡ Or prep **Unit 02: Hashing Issue**

Say the word — we keep building 🚀
