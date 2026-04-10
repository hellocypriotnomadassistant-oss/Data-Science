# Data Importing with Python: Files and Databases

This guide explains how to import data from various sources using Python.

---

## 1. Importing CSV Files (Python Standard Library)
The most basic way to open a CSV file in Python is using the `with open` statement:

```python
with open('file_path/file_name', mode='r') as file:
    data = file.read()

    import pandas as pd

# Importing from a local path
df = pd.read_csv('file_path/file_name.csv')

# Importing directly from a URL
df = pd.read_csv('[https://example.com/data.csv](https://example.com/data.csv)')

SELECT tree_id, plant_type, species
FROM `san_francisco.street_trees`
LIMIT 5000;