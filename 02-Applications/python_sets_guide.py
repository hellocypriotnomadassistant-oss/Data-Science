"""
PYTHON SETS: THE ULTIMATE GUIDE
-------------------------------
A comprehensive reference for creating and managing Sets in Python.
Sets are unordered collections of unique, immutable elements.
"""

# 1. CREATING SETS
# Method 1: Using the set() function (Essential for creating empty sets)
empty_set = set() # Note: {} creates an empty dictionary, NOT a set!

# Method 2: Using curly braces with elements
fruits = {"apple", "banana", "cherry"}

# Method 3: Converting other iterables (Automatically removes duplicates)
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"Original List: {numbers_list}")
print(f"Unique Set: {unique_numbers}") # Output: {1, 2, 3, 4, 5}


# 2. KEY CHARACTERISTICS & CONSTRAINTS
# - Unordered: No indexing or slicing! fruits[0] will raise a TypeError.
# - Unique: Duplicate elements are automatically discarded.
# - Elements must be IMMUTABLE: You can put strings/tuples in a set, but NOT lists.

word_set = set("mississippi")
print(f"Unique characters in 'mississippi': {word_set}")


# 3. SET OPERATIONS (THE POWER TOOLS)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"\nSet A: {set_a} | Set B: {set_b}")

# Intersection (Common elements) -> A & B
print(f"Intersection (A & B): {set_a.intersection(set_b)}")

# Union (All elements combined) -> A | B
print(f"Union (A | B): {set_a.union(set_b)}")

# Difference (In A but NOT in B) -> A - B
# Note: A - B is NOT the same as B - A
print(f"Difference (A - B): {set_a - set_b}") # {1, 2}
print(f"Difference (B - A): {set_b - set_a}") # {5, 6}

# Symmetric Difference (Elements in either A or B, but NOT both) -> A ^ B
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}") # {1, 2, 5, 6}


# 4. WHY USE SETS IN DATA SCIENCE?
"""
- Data Cleaning: Quickly remove duplicates from large datasets.
- Membership Testing: Checking 'if x in set' is much faster than 'if x in list'.
- Comparison: Finding common or unique values between two different data sources.
"""

print("\nSet operations guide executed successfully.")