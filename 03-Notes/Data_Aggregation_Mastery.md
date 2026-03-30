# Comprehensive Guide to Pandas GroupBy & Aggregation

This guide provides a structured overview of data transformation techniques using the **Split-Apply-Combine** strategy in Python.

---

## 🏗️ 1. The Core Logic: GroupBy
The `groupby()` function is the foundation of data analysis in Pandas. It follows a three-step process:

1.  **Split:** Breaking the data into groups based on specific keys.
2.  **Apply:** Computing a function (like average or sum) for each group.
3.  **Combine:** Merging the results into a new data structure.



## 📊 2. Essential Operations
Basic aggregations allow you to quickly understand your categories:

* **Mean Calculation:** `df.groupby('category').mean()`
* **Multi-Column Groups:** `df.groupby(['type', 'color']).min()`
* **Frequency Count:** `df.groupby('type').size()`

## ⚙️ 3. Advanced Aggregation with agg()
While `mean()` or `sum()` are great, the `agg()` function offers professional-level flexibility by allowing different operations for different columns.

```python
# Custom aggregation dictionary
df.agg({
    'price_usd': 'sum',
    'mass_g': ['mean', 'median', 'std']
})
