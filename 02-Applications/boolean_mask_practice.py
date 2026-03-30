import pandas as pd

# 1. Step: Prepare the Dataset
# We create a dictionary representing planets, their moons (satellites), and radius
data = {
    "planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"],
    "satellites": [0, 0, 1, 2, 95, 146],
    "radius_km": [2440, 6051, 6371, 3389, 69911, 58232]
}

# Convert dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

print("--- Full Planet Dataset ---")
print(df)

# 2. Step: Simple Boolean Masking
# Filter planets with fewer than 20 satellites
low_moon_mask = df["satellites"] < 20
low_moon_planets = df[low_moon_mask]

print("\n--- Planets with < 20 Satellites ---")
print(low_moon_planets)

# 3. Step: Complex Filtering (Multiple Conditions)
# Condition: Satellites > 0 AND Radius > 5000 km
# Remember: Use parentheses () for each condition and '&' for AND
complex_mask = (df["satellites"] > 0) & (df["radius_km"] > 5000)
large_mooned_planets = df[complex_mask]

print("\n--- Planets with Moons AND Radius > 5000km ---")
print(large_mooned_planets)

# 4. Step: Using the NOT (~) operator
# Filter planets that are NOT Saturn
not_saturn = df[~(df["planet"] == "Saturn")]

print("\n--- All Planets Except Saturn ---")
print(not_saturn)