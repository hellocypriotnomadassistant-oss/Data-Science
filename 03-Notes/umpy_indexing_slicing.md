# 🔪 NumPy: Indexing and Slicing
*Mastering how to access and extract specific data from arrays.*

---

## 🔹 1. Basic Indexing (1D Arrays)
NumPy uses zero-based indexing, just like Python lists.
* `arr[0]` -> Access the **first** element.
* `arr[-1]` -> Access the **last** element.
* `arr[3] = 10` -> **Update** the value at index 3.

---

## 🔹 2. Slicing (Extracting Subsets)
**Syntax:** `array[start : stop : step]`
* `arr[1:5]` -> Elements from index 1 to 4 (stop is exclusive).
* `arr[:3]` -> Everything from the start up to index 2.
* `arr[::2]` -> Every second element (jumps by 2).

---

## 🔹 3. 2D Array Indexing (Rows & Columns) ⭐
This is the most important part for Data Science. Use a comma to separate dimensions:
**Syntax:** `array[row_index, column_index]`

* `arr[0, 0]` -> Top-left element (First row, first column).
* `arr[1, :]` -> Get the **entire second row**.
* `arr[:, 2]` -> Get the **entire third column**.
* `arr[0:2, 1:3]` -> A "sub-matrix" of the first two rows and columns 1-2.



---

## 🔹 4. Advanced: Boolean Indexing (Filtering) 🔍
You can select elements based on conditions:
```python
# Select all elements greater than 5
filtered_arr = arr[arr > 5]