# 📊 EDA & Data Structuring: NOAA Lightning Analysis

### 🎯 Project Objective
Analyze the NOAA lightning strike dataset (2016-2018) to identify patterns: 
*"On which days and months do lightning strikes occur most frequently?"*

---

## 🔑 1. Data Preparation & Cleaning
* **Library Imports**: Use `pandas`, `numpy`, `seaborn`, and `matplotlib`.
* **Datetime Conversion**: Convert the `date` column to a `datetime` object for time-series analysis.
* **Duplicates**: Check for and remove duplicate entries using `df.drop_duplicates()`.

## 🔑 2. Exploration & Feature Engineering
* **Sorting**: Use `sort_values()` to find peak strike days (often in August).
* **Extraction**: Create new columns for `week`, `month`, and `weekday`.
* **Geographic Check**: Use `value_counts()` to ensure locations (lat/long) are distributed reasonably.

## 🔑 3. Grouping & Aggregation
* **Weekly Patterns**: Group data by `weekday` to calculate the mean number of strikes.
* **Yearly Comparison**: Use `pd.concat()` to combine data from 2016, 2017, and 2018.

## 🔑 4. Visualization & Insights
* **Boxplots**: Used to see the distribution across days. 
  * *Insight:* Strikes might appear lower on weekends—is this a reporting bias or a natural pattern?
* **Barplots**: Used to see the percentage of strikes per month.
  * *Insight:* August often accounts for over 33% of yearly strikes due to storm seasons.

---

> **🧠 Final Conclusion:** Data structuring allows us to uncover hidden patterns, such as the extreme surge of activity in August, which can then be cross-referenced with hurricane/storm data.

### 📊 Visualization Results
Here is the result of the exploratory data analysis on NOAA lightning data:

![Lightning Distribution](lightning_distribution.png)