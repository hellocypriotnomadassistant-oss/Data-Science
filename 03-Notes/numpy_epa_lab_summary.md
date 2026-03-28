# 🌿 Case Study: EPA Air Quality Analysis with NumPy
*Applying NumPy for real-world environmental data analysis.*

---

## 🔹 1. Project Overview
Analysis of Air Quality Index (AQI) data from the US and Mexico to identify pollution levels and health concerns.
* **AQI 0-50:** Good Quality
* **AQI > 300:** Hazardous

---

## 🔹 2. Key Technical Implementations

### **A. List to Array Conversion**
Converting standard Python lists to NumPy `ndarray` for performance:
```python
import numpy as np
aqi_array = np.array(aqi_list)
print(len(aqi_array))  # Result: 1725
# Create a boolean mask for values <= 5
boolean_aqi = aqi_array <= 5

# Calculate percentage (True = 1, False = 0)
percent_clean = np.sum(boolean_aqi) / len(aqi_array)
# Result: ~31.94%
