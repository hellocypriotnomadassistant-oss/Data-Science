# 📌 Pandas GroupBy & Aggregation – Summary

### 🔑 1. What is GroupBy? (The Core Definition)
`groupby()` is a method used to group data based on specific columns. After grouping, you perform calculations on these groups.

> **Summary:** GroupBy = "Bring the identical ones together."

---

### 🧠 2. How Does It Work? (Split-Apply-Combine)
1. **Split:** Groups the data based on a key.
2. **Apply:** Performs an operation (sum, mean, etc.) on each group.
3. **Combine:** Merges the results into a new structure.



---

### ⚙️ 3. Basic Usage & Functions
* **Syntax:** `df.groupby("column_name").function()`
* **Common Functions:**
  * `sum()`: Total
  * `mean()`: Average
  * `count()`: Number of items
  * `min()` / `max()`: Minimum and Maximum values

---

### 🧩 4. The Power of `.agg()` (Aggregation)
The `agg()` method allows you to perform **multiple operations** at once.
```python
# Calculate both mean and median for each group
df.groupby("type").agg(["mean", "median"])