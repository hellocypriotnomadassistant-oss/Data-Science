# 🌍 Case Study: EPA Air Quality Analysis with NumPy
*Analyzing air quality index (AQI) data using vectorized operations.*

---

## 🔹 1. Project Objectives
* Convert EPA air quality readings into a NumPy `ndarray`.
* Perform statistical analysis (Mean, Median, Std Dev).
* Use **Boolean Masking** to filter and calculate the percentage of "clean air" days (AQI ≤ 5).

---

## 🔹 2. Technical Implementation

### **A. Data Conversion & Inspection**
```python
import numpy as np
# Convert list to ndarray
aqi_array = np.array(aqi_list)

print(len(aqi_array))  # 1725
print(aqi_array[:5])   # [18. 9. 20. 11. 6.]
print('Max =', np.max(aqi_array))        # 93.0
print('Min =', np.min(aqi_array))        # 0.0
print('Median =', np.median(aqi_array))  # 8.0
print('Std =', np.std(aqi_array))        # 10.38
# Create boolean mask
boolean_aqi = (aqi_array <= 5)

# Calculate percentage (True = 1, False = 0)
percent_clean = boolean_aqi.sum() / len(boolean_aqi)
print(percent_clean)  # 0.3194... (Approx 32%)
