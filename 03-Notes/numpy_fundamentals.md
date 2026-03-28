# 🔢 NumPy Fundamentals: The ndarray
*The core data structure for efficient numerical computing in Python.*

---

## 🔹 1. What is an ndarray?
`ndarray` stands for **n-dimensional array**. It is the primary building block of NumPy.
* **Think of it as:** An advanced, high-performance version of a Python list.
* **Key Advantages:**
    * **Speed:** Extremely fast ⚡ (written in C).
    * **Memory:** Uses significantly less memory.
    * **Vectorization:** Performs operations on entire arrays at once without loops.

---

## 🔹 2. Creating an ndarray
You can create an array from standard Python objects like lists:

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Convert a 1D array of 8 elements into a 2x4 matrix
arr.reshape(2, 4)
