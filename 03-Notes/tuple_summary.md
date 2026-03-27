# 🔒 Python Tuple Summary

### 🔹 1. What is a Tuple?
A Tuple is an **immutable** data structure that can hold different data types. It is similar to lists, but its content cannot be modified after it is created.

### 🔑 Most Critical Features
* **Immutability:** Elements cannot be added, deleted, or updated.
* **Fixed Index:** The data structure is more reliable and memory-efficient.
* **Definition:** Created using parentheses `()` or the `tuple()` function.

### 🔄 2. Creating and Converting Tuples
```python
# Direct definition
names = ("Ali", "V", "Yilmaz")

# Converting a List to a Tuple
my_list = ["Apple", "Pear"]
my_tuple = tuple(my_list)

price_info = (6, 55)
dollar, cent = price_info
# Now 'dollar' is 6 and 'cent' is 55 as independent variables.

def get_coordinates():
    return 40.7128, 74.0060  # Actually returns a tuple