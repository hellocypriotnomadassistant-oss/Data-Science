# 📌 Date String Manipulation & Visualization

A comprehensive guide on transforming string dates, grouping time data, and creating insightful visualizations using Pandas, Matplotlib, and Seaborn.

---

## 1. Core Objectives
* Convert **String** date formats into **Datetime** objects.
* Extract time components (Week, Month, Quarter, Year).
* Perform time-based aggregations (Grouping).
* Create professional visualizations to tell a story with data.

---

## 2. Environment Setup
Essential libraries for data manipulation and visualization:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df['date'] = pd.to_datetime(df['date'])

sns.barplot(x='quarter_number', y='strikes', hue='year', data=df)

