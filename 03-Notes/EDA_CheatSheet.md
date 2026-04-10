# Exploratory Data Analysis (EDA) - Essential Pandas Tools

The first step in any data project is understanding your dataset. Here are the 4 fundamental Pandas tools for initial exploration.

## 1. head() → Viewing the Data
Displays the first few rows of the dataset.
- **Usage:** `df.head()` or `df.head(10)`
- **Purpose:** To check if data loaded correctly and verify column names.

## 2. info() → Data Identity
Provides a comprehensive summary of the dataset's structure.
- **Usage:** `df.info()`
- **Displays:** Total rows/columns, data types (int, float, object), non-null counts, and memory usage.

## 3. describe() → Statistical Summary
Generates descriptive statistics for numerical columns.
- **Usage:** `df.describe()`
- **Metrics:** Count, mean, standard deviation (std), min, max, and quartiles (25%, 50%, 75%).

## 4. shape → Data Dimensions
Returns the number of rows and columns.
- **Usage:** `df.shape`
- **Example Output:** `(1000, 4)` means 1000 rows and 4 columns.

---

### 🧠 Quick Reference Table
| Function | Description |
| :--- | :--- |
| **head()** | Shows the first rows |
| **info()** | Summarizes data structure |
| **describe()** | Provides statistical summary |
| **shape** | Returns (rows, columns) |