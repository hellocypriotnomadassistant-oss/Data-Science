"""
TOPIC: Python Dictionaries (Fundamentals)
DESCRIPTION: Key-Value pairs, rules, and common methods.
"""

# 1. Initialization
# Using curly braces
zoo_1 = {1: "lion", 2: "zebra"}
# Using dict function
zoo_2 = dict(one="lion", two="zebra")

print(f"Zoo 1: {zoo_1}")

# 2. Accessing Data
# You search by KEY to get the VALUE
print(f"Key 2 belongs to: {zoo_1[2]}")

# 3. Adding/Updating Elements
zoo_1[4] = "crocodile"  # Adds a new entry
zoo_1[1] = "king lion"  # Updates existing entry
print(f"Updated Zoo: {zoo_1}")

# 4. Critical Rules
# - Keys must be IMMUTABLE (int, float, string, tuple)
# - No indexing (zoo[0] will raise an error unless 0 is a key)
# - 'in' keyword checks KEYS only
if 2 in zoo_1:
    print("Key 2 is present in the zoo.")

# 5. Handling Missing Keys
# Using .get() prevents KeyError crashes
print(zoo_1.get(99, "Animal not found"))