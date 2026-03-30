# 📌 Pandas GroupBy & Aggregation – Advanced Summary

### 🔑 Core Concept: Group, Calculate, Interpret
In Pandas, `groupby()` and `agg()` are used to split, summarize, and analyze data.

1. **groupby()** → Splits the data into groups.
2. **agg()** → Performs one or more calculations on these groups.

---

### 🧩 1. How groupby() Works
Grouping by a column creates a "GroupBy object". 
* **Note:** It doesn't do much on its own; you must follow it with an operation.
* **Example:** `df.groupby('type')`

---

### 📊 2. Common Aggregation Functions
After grouping, you usually want to see:
* `mean()`: Average
* `sum()`: Total
* `count()` or `size()`: Number of items
* `min()` / `max()`: Minimum and Maximum
* `std()` / `var()`: Standard deviation and Variance

---

### ⚡ 3. The Power of the `.agg()` Method
This is the most flexible way to analyze data. You can perform different operations on different columns at once.

**Example:**
```python
df.groupby('color').agg({
    'price': ['mean', 'max'],
    'mass': 'sum'
})