# 📌 Pandas Fundamentals: Comprehensive Summary

### 🔑 1. What is Pandas?
It is the most essential library for **data analysis** in Python. It makes working with **tabular data** (rows and columns) incredibly efficient.

### 🧱 2. Core Data Structures
* **Series:** 1-dimensional (a single column). Every element has an **index**.
* **DataFrame:** 2-dimensional (table). It is a collection of Series sharing the same index.



### ⚙️ 3. Creating a DataFrame
The most common way is reading from a CSV file:
```python
import pandas as pd
df = pd.read_csv("data.csv")
df["Age"]          # Returns a Series
df[["Age", "Name"]] # Returns a DataFrame