
import pandas as pd

# Creating a sample dataset based on your image
data = {
    'planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'],
    'satellites': [0, 0, 1, 2, 95, 146],
    'radius_km': [2440, 6051, 6371, 3389, 69911, 58232]
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

# 1. Simple Masking (Planets with more than 10 satellites)
mask1 = df["satellites"] > 10
print("\n--- Planets with > 10 Satellites ---")
print(df[mask1])

# 2. Complex Masking (More than 20 satellites AND radius > 60,000 km)
mask2 = (df["satellites"] > 20) & (df["radius_km"] > 60000)
print("\n--- Massive Planets (Jupiter) ---")
print(df[mask2])

# 3. Using .loc to filter and select specific columns
# Filter by mask, but only show 'planet' and 'radius_km'
result = df.loc[df["satellites"] > 0, ["planet", "radius_km"]]
print("\n--- Planets with at least one moon (Name & Radius only) ---")
print(result)