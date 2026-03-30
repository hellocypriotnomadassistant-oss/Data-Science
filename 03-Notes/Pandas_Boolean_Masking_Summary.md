# 📌 Pandas Boolean Masking – Summary

### 🔑 1. What is Boolean Masking?
It is a method of filtering data in Pandas based on specific conditions.

For every row:
* ✅ **True** → The data stays.
* ❌ **False** → The data is removed.

> **Summary:** Boolean mask = A filtering system for your dataset.

---

### 🧠 2. How Does It Work?
1. **Write the condition:** `df["moons"] < 20`
2. **Result:** This creates a Series of **True / False** values.
3. **Apply to DataFrame:** `df[df["moons"] < 20]`

---

### ⚙️ 3. Syntax & Best Practices
* **Assign to Variable:** ```python
  mask = df["moons"] < 20
  df[mask]
  