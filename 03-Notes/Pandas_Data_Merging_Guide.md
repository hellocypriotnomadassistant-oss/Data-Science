# Pandas Data Merging Guide: concat() vs merge()

This guide explains the core logic of combining datasets in Pandas using two primary functions: `concat()` and `merge()`.

---

## 📌 1. Core Concept
In data analysis, we often need to:
1. **Append** new data (Rows or Columns).
2. **Join** different datasets based on a common key.

## 🔗 2. Vertical and Horizontal Stacking: `concat()`
`concat()` is used for simple "gluing" of DataFrames along an axis.



- **axis=0 (Default):** Appends rows (Vertical).
- **axis=1:** Appends columns (Horizontal).

### 🛠️ Example Usage:
```python
# Vertical concatenation
combined_df = pd.concat([df1, df2], axis=0).reset_index(drop=True)
# Merging on a specific column
result = pd.merge(df1, df2, on='planet_id', how='inner')
