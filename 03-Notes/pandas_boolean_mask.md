# 📌 Pandas: Boolean Masking (Conditional Filtering)

### 🔑 1. What is a Boolean?
A Boolean is a data type that has only two values: **True** or **False**. 
In Pandas, we use this to keep (`True`) or discard (`False`) specific rows.

### 🧠 2. How Boolean Mask Works
A "mask" is a series of True/False values applied to a DataFrame.


### ⚙️ 3. Basic Filtering Syntax
```python
# Returns only the rows where 'satellites' is less than 20
df[df["satellites"] < 20]
