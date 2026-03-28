# 📑 NumPy: Comprehensive Reference Guide
*A deep dive into ndarrays, memory efficiency, and essential methods.*

---

## 🔹 1. Why NumPy?
NumPy is the foundation of Data Science in Python because of the **ndarray**:
* ⚡ **Speed:** Faster mathematical operations.
* 💾 **Memory:** Significant reduction in memory usage.
* **Efficiency:** Especially noticeable when handling Large Datasets.

---

## 🔹 2. Array Creation
### **Basic & Multi-dimensional**
```python
import numpy as np
np.array([1, 2, 3])                # 1D Array
np.array([[1,2,3], [4,5,6]])       # 2D Array (Matrix)
# [1, 2, 3] * [1, 2, 3] results in [1, 4, 9]
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b) # Sonuç: [11, 22, 33]

