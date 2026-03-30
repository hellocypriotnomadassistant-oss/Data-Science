# Lab: EPA Air Quality Index (AQI) Data Analysis

This project analyzes air quality data from the U.S. and Mexico using **Pandas**. The goal is to examine metadata, compute summary statistics, and perform advanced data manipulation like Boolean masking and concatenation.

## 📌 Project Overview
The Air Quality Index (AQI) ranges from 0 to 500:
- **0 - 50:** Good
- **51 - 100:** Moderate
- **> 300:** Hazardous

## 📊 Key Tasks Performed

### 1. Data Loading & Inspection
- Loaded `epa_ca_tx_pa.csv` (Top 3 states: CA, TX, PA).
- Investigated metadata using `.info()` and summary statistics with `.describe()`.

### 2. Data Exploration
- **Sorting:** Ranked observations by AQI in descending order.
- **Indexing:** Used `.iloc` to select specific high-pollution rows.
- **Value Counts:** Identified that California has the most observations (342 rows).

### 3. Targeted Analysis (California & LA)
- Created a subset for California using Boolean masking.
- Analyzed Los Angeles county specifically, calculating a mean AQI of **13.4**.

### 4. Data Integration (Concatenation)
- Loaded a second dataset `epa_others.csv`.
- Used `pd.concat(axis=0)` to combine all states into a single `combined_df`.

### 5. Advanced Filtering
- Performed complex Boolean masking (Multi-condition) to find high-pollution days in **Washington** state (AQI >= 51).

---
*Environment: Python 3.x | Library: Pandas, Numpy*