# 📌 Pandas Data Structuring – 

### 🎯 Core Philosophy
* You don't need to memorize every function.
* Using references (documentation/cheat sheets) is a standard part of a data analyst's daily workflow.

---

## 🔑 1. Combining Data
* **`df.merge()`**: Joins DataFrames based on a common column (similar to SQL Joins).
  * *Example:* `df1.merge(df2, on='id')`
* **`pd.concat()`**: Concatenates (stacks) DataFrames along rows or columns.
  * *Example:* `pd.concat([df1, df2])`
* **`df.join()`**: Joins DataFrames based on their index or a specific key.

## 🔑 2. Selecting & Extracting
* **Column Selection**: Select specific columns by name.
  * *Example:* `df[['column_a', 'column_b']]`
* **`df.select_dtypes()`**: Filter columns based on data types (e.g., only numbers).
  * *Example:* `df.select_dtypes(include=['number'])`

## 🔑 3. Filtering
* **Boolean Masking**: Select rows that meet a specific condition.
  * *Example:* `df[df['age'] > 30]`

## 🔑 4. Sorting
* **`df.sort_values()`**: Reorder the data based on values in a column.
  * *Example:* `df.sort_values(by='price', ascending=False)`

## 🔑 5. Slicing
* **`df.iloc[]`**: Selection by integer-based index (position).
  * *Example:* `df.iloc[0:10, 0:2]` (First 10 rows, first 2 columns).
* **`df.loc[]`**: Selection by labels (names).
  * *Example:* `df.loc[:, ['name', 'city']]`

---

## 🧠 The Logic
These tools allow you to:
**Select → Filter → Sort → Slice → Merge**
The goal is to transform **raw data** into **analyzable data**.

> **💡 Key Takeaway:** There is often more than one way to achieve the same result in Pandas. This is normal; choose the one that is most readable for your project.