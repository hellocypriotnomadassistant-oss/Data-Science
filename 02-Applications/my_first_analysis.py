import pandas as pd
import numpy as np

# 1. Generate random sales data using NumPy
sales = np.array([4500, 7800, 3200, 9100, 5600])

# 2. Convert this data into a table (DataFrame) using Pandas
data = {
    'Store_ID': ['M01', 'M02', 'M03', 'M04', 'M05'],
    'Daily_Sales': sales,
    'Region': ['North', 'South', 'North', 'West', 'East']
}

df = pd.DataFrame(data)

# 3. Analysis: Filter stores with sales greater than 5000
successful_stores = df[df['Daily_Sales'] > 5000]

print("--- Full Store List ---")
print(df)
print("\n--- Stores That Exceeded the Target ---")
print(successful_stores)

# 4. Calculate average sales using NumPy
average_sales = np.mean(df['Daily_Sales'])
print(f"\nAverage sales of all stores: {average_sales} USD")
