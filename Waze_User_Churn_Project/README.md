# 📊 My Data Analysis Journey

This repository contains the projects and analyses I have conducted on my path to becoming a Data Analyst.

## 📁 Project Structure
- **data/**: Raw data files used for analysis (.csv, .xlsx).
- **notebooks/**: Jupyter notebooks containing analysis steps, code, and visualizations.
- **scripts/**: Reusable Python scripts and utility functions.
- **archive/**: Earlier drafts and practice codes.

## 🚀 Key Achievements & Projects
- **Titanic Survival Analysis**: Performed exploratory data analysis (EDA) and visualized survival rates using Seaborn and Matplotlib.
- **Local Sales Data Processing**: Cleaned and manipulated custom sales datasets using the Pandas library to calculate business metrics.
- **Environment Setup**: Configured a professional development environment using VS Code, Jupyter, and Python 3.14.
- **Version Control**: Managed the entire project lifecycle using Git and GitHub for professional collaboration.

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn
- **Tools**: VS Code, Jupyter Notebook, Git/GitHub
# Waze User Churn Analysis 🚗
## Project Overview
This project analyzes Waze user data to understand factors leading to churn...

# Waze User Churn Analysis 🚗

This project is an **Exploratory Data Analysis (EDA)** aimed at understanding the underlying reasons for user churn within the Waze application.

---

## 📌 Key Findings

* **Missing Data:** Analysis confirmed that the 700 missing values in the `label` column are distributed randomly.
* **User Profiling:** Churned users exhibited an average daily mileage of **~700 km**, suggesting they may belong to a **professional driver** segment.
* **Device Impact:** There is no significant difference in churn rates between **iPhone (64%)** and **Android (36%)** users; both segments show a churn rate of approximately **18%**.

---

## 📊 Summary Comparison

| Feature | Churned | Retained |
| :--- | :--- | :--- |
| **Days of Usage** | Lower | Higher |
| **Daily KM** | High (~700km) | Low |
| **Driving Frequency** | Intense / Short-term | Sporadic / Long-term |

---

## 🚀 Recommendations

1.  **Segment Optimization:** Develop specialized features and loyalty programs tailored for the **professional driver** segment.
2.  **Data Enrichment:** Integrate **qualitative data** (such as user exit surveys) into the dataset to better understand the "why" behind uninstalls.
3.  **Performance Tracking:** Monitor technical app performance (crashes, latency) to differentiate between behavioral churn and technical churn.

---

> **Note:** This analysis was conducted as part of the data science workflow to ensure data-driven decision-making for user retention strategies.