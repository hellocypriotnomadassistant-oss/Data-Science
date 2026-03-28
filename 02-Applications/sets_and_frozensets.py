"""
PYTHON SETS AND FROZENSETS
--------------------------
Comprehensive guide on unique collections, hashability, 
and the difference between mutable and immutable sets.
"""

# 1. CREATING SETS (Reminder)
# Sets automatically remove duplicates
numbers = {5, 10, 10, 20}
print(f"Unique Set: {numbers}") # Output: {5, 10, 20}

# Crucial Detail: 2 is equal to 2.0 in a set
mixed_set = {2, 2.0}
print(f"Mixed Set (2 == 2.0): {mixed_set}") # Output: {2} or {2.0}


# 2. HASHABILITY RULE (CRITICAL ⚠️)
# Elements inside a set MUST be immutable (hashable).
# Allowed: int, str, float, tuple, frozenset
# NOT Allowed: list, set, dict

try:
    invalid_set = {1, [2, 3]} # This will raise a TypeError
except TypeError as e:
    print(f"\nError check: Sets cannot contain lists! ({e})")


# 3. SET vs. FROZENSET
# set: Mutable (can add/remove elements)
# frozenset: Immutable (cannot be changed after creation)

normal_set = set([1, 2, 3])
normal_set.add(4) # Works fine

frozen = frozenset([1, 2, 3])
# frozen.add(4) -> This would cause an AttributeError

# Why use frozenset? 
# It can be used as a Dictionary Key or an element of another Set!
locations = {
    frozenset(["New York", "London"]): "Global Offices"
}
print(f"Frozenset as a Key: {locations}")


# 4. ESSENTIAL SET OPERATIONS
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (|): All elements from both
print(f"\nUnion: {set_a | set_b}")

# Intersection (&): Only common elements
print(f"Intersection: {set_a & set_b}")

# Difference (-): Only in A, not in B (Not commutative!)
print(f"Difference (A-B): {set_a - set_b}") 
print(f"Difference (B-A): {set_b - set_a}")

# Symmetric Difference (^): Elements in either A or B, but not both
print(f"Symmetric Difference: {set_a ^ set_b}")


# 5. SUMMARY TABLE (Conceptual)
"""
Feature          | Set          | Frozenset
-------------------------------------------
Mutable          | Yes          | No
Add/Remove       | Yes          | No
Hashable         | No           | Yes
Can be Dict Key  | No           | Yes
"""

print("\nSets and Frozensets guide completed.")