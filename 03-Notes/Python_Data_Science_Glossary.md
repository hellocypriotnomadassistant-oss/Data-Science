# 📘 Python Data Science Glossary (Modules 1-4)

This document serves as a comprehensive reference guide for core Python concepts, including the Pandas and NumPy libraries.

---

## 🚀 Module 4: Data Analysis (Pandas & NumPy)

### 📊 Pandas & Tabular Operations
| Term | Definition |
| :--- | :--- |
| **agg()** | A groupby method that allows applying multiple calculations (mean, sum, etc.) to data groups. |
| **Alias** | An operation that allows a user to assign an alternative name or nickname to something (e.g., `import pandas as pd`). |
| **Boolean Masking** | A filtering technique that overlays a boolean grid on a dataframe to select only values aligned with `True`. |
| **concat()** | A function that combines dataframes by appending rows vertically or columns horizontally. |
| **CSV File** | A plain text file that uses commas to separate values (Comma Separated Values). |
| **DataFrame** | A two-dimensional, labeled data structure with rows and columns. |
| **groupby()** | A method that groups rows based on values in one or more columns for further analysis. |
| **iloc[]** | Integer-location based indexing used to select rows and columns by their numerical position. |
| **loc[]** | Label-based indexing used to select rows and columns by their names. |
| **Inner Join** | A join method that includes only the keys present in both dataframes. |
| **Left Join** | A join method that includes all keys from the left dataframe, even if they aren't in the right one. |
| **merge()** | A function used to join two dataframes horizontally along an axis. |
| **NaN** | "Not a Number"; used to represent null or missing values in pandas. |
| **Outer Join** | A join method that includes all keys from both dataframes. |
| **Right Join** | A join method that includes all keys from the right dataframe, even if they aren't in the left one. |
| **Series** | A one-dimensional, labeled array where all data must be of the same type. |

### 🔢 NumPy & Arrays
| Term | Definition |
| :--- | :--- |
| **dtype** | A NumPy attribute used to check the data type of an array's contents. |
| **N-dimensional array** | NumPy's core data object, also called an `ndarray`. |
| **ndim** | An attribute that checks the number of dimensions of an array. |
| **reshape()** | A method used to change the shape or dimensions of an array. |
| **shape** | An attribute that returns the dimensions (rows, columns) of an array. |
| **Vectorization** | Performing operations on all elements of a data object simultaneously without explicit loops. |

---

## 🐍 Core Python Concepts (Modules 1-3)

### 🏗️ Data Structures
- **List:** An ordered and mutable collection of items.
- **Tuple:** An ordered but **immutable** sequence of elements.
- **Dictionary (dict):** A collection of key-value pairs.
- **Set:** An unordered collection of unique elements only