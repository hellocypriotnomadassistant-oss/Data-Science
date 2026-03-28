# 📚 Python Ecosystem: Libraries, Packages, and Modules
*A comprehensive guide to the essential tools for Data Science.*

---

## 🔹 1. Core Definitions

* **Library:** A large collection of reusable code (functions, classes) and documentation.
* **Package:** An organized, distributable form of libraries.
* **Module:** Smaller, individual code files within a library; contains functions, classes, and variables.

> **👉 Hierarchy:** Library > Package > Module > Function

---

## 🔹 2. Importing Libraries
If a feature is not in the Python Standard Library, it must be installed first (usually via `pip`) and then imported into your script.

### **✔️ Basic Syntax**
```python
import numpy
numpy.array([2, 4, 6])
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.array([2, 4, 6])
from sklearn.metrics import precision_score, recall_score
from numpy import array
