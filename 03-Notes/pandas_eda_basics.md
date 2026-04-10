# Exploring Datasets with Pandas – Summary

This document covers the essential Pandas tools used during the initial phase of Exploratory Data Analysis (EDA).

## 1. df.head(n)
Displays the first `n` rows of the DataFrame.
* **Default:** First 5 rows.
* **Purpose:** To quickly see the general structure of the data.
* **Example:**
  ```python
  ## 1. df.head(n)
Displays the first `n` rows of the DataFrame.
* **Default:** First 5 rows.
* **Purpose:** To quickly see the general structure of the data.
* **Example:**
```python
df.head(10)

Provides a summary of the dataset.

Purpose: To identify missing values and data types.

Example:

Python
df.info()

Generates descriptive statistics for numerical columns.

Example:

Python
df.describe()

Returns the dimensions of the dataset.

Example:

Python
df.shape # Output example: (1000, 12)

