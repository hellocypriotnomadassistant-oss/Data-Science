# 📌 Pandas Core Structures: DataFrame & Series

### 🔑 1. Basic Structures
Pandas has two primary data structures:

* **📊 DataFrame:** 2-dimensional (rows + columns). Like an Excel or SQL table.
* **📈 Series:** 1-dimensional array. Usually a single column or a single row.
**Summary:** A DataFrame is essentially a collection of Series.

### 📂 2. Creating DataFrames
* **From Dictionary:** `pd.DataFrame({"name": ["Ali", "Ayşe"]})`
* **From CSV (Most Common):** `df = pd.read_csv("data.csv")`

### ⚙️ 3. Attributes vs. Methods
* **Attributes (Properties):** No parentheses. Examples: `df.shape`, `df.columns`.
* **Methods (Functions):** Requires parentheses. Example: `df.info()`.

### 🔍 4. Selection & Indexing
* **Single Column:** `df["Age"]` or `df.Age`
* **Multiple Columns:** `df[["Age", "Name"]]`
* **📍 iloc (Integer-based):** Selection by position (index number).
    * `df.iloc[0]` (First row)
* **📍 loc (Label-based):** Selection by name (column/row names).
    * `df.loc[0:3, "Name"]`

### ⚠️ 5. Critical Concepts
* **NaN:** Missing data (Not a Number). 
* **Object:** Mixed data types usually appear as 'object' in Pandas.

---
**🎯 Summary:** Pandas is a powerful library that allows you to manage, analyze, and manipulate data in a tabular format easily.