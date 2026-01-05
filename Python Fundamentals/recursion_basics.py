"""
recursion_basics.py
Purpose: Understand recursion fundamentals for DSA
Author: Your Name
"""

# =========================
# WHAT IS RECURSION?
# =========================
# A function calling itself to solve a smaller subproblem.
# Every recursive function MUST have:
# 1. Base case -> stops recursion
# 2. Recursive case -> reduces problem size


# =========================
# EXAMPLE 1: PRINT NUMBERS
# =========================
def print_numbers(n):
    if n == 0:          # Base case
        return
    print(n)
    print_numbers(n - 1)  # Recursive call


# =========================
# EXAMPLE 2: FACTORIAL
# =========================
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)


# =========================
# EXAMPLE 3: SUM OF ARRAY
# =========================
def array_sum(arr, index=0):
    if index == len(arr):     # Base case
        return 0
    return arr[index] + array_sum(arr, index + 1)


# =========================
# EXAMPLE 4: FIBONACCI (RECURSIVE)
# =========================
def fibonacci(n):
    if n <= 1:               # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# =========================
# EXAMPLE 5: REVERSE STRING
# =========================
def reverse_string(s):
    if s == "":              # Base case
        return s
    return reverse_string(s[1:]) + s[0]


# =========================
# RECURSION CALL STACK (IMPORTANT)
# =========================
"""
Example: factorial(3)

factorial(3)
 -> 3 * factorial(2)
     -> 2 * factorial(1)
         -> 1
     -> 2
 -> 6
"""


# =========================
# COMMON MISTAKES
# =========================
# ❌ Missing base case
# ❌ Not reducing problem size
# ❌ Excessive recursion depth
# ❌ Using recursion where iteration is better


# =========================
# TIME & SPACE COMPLEXITY
# =========================
"""
Factorial:
- Time: O(n)
- Space: O(n)  (call stack)

Fibonacci (naive):
- Time: O(2^n)
- Space: O(n)
"""


# =========================
# WHEN TO USE RECURSION
# =========================
# ✔ Tree problems
# ✔ Backtracking
# ✔ Divide and conquer
# ✔ Problems with natural recursive structure


# =========================
# INTERVIEW TIP
# =========================
# Always explain:
# 1. Base case
# 2. Recursive transition
# 3. Time & space complexity
