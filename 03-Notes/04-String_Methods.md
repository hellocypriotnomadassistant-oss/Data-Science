# 🔤 Python String Methods & Slicing

## 🔹 String Indexing and Slicing
Strings are sequences of characters, and we can access specific parts using indexes.

```python
text = "Python Programming"

# Indexing
print(text[0])   # Output: 'P'
print(text[-1])  # Output: 'g' (Last character)

# Slicing [start:stop:step]
print(text[0:6])   # Output: 'Python'
print(text[7:14])  # Output: 'Program'
print(text[::-1])  # Output: 'gnimmargorP nohtyP' (Reverse)