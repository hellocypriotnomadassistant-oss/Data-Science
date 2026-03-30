
import pandas as pd

# 1. Creating a sample dataset
data = {
    'planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'type': ['Terrestrial', 'Terrestrial', 'Terrestrial', 'Terrestrial', 'Gas Giant', 'Gas Giant', 'Ice Giant', 'Ice Giant'],
    'moons': [0, 0, 1, 2, 95, 146, 27, 14],
    'radius_km': [2440, 6051, 6371, 3389, 69911, 58232, 25362, 24622]
}

df = pd.DataFrame(data)

print("--- Original Planet Data ---")
print(df)

# 2. Simple GroupBy: Total moons by planet type
moons_by_type = df.groupby("type")[["moons"]].sum()
print("\n--- Total Moons per Type ---")
print(moons_by_type)

# 3. Using .agg() for multiple statistics
# Calculate average and max radius for each type
stats = df.groupby("type")["radius_km"].agg(["mean", "max"])
print("\n--- Radius Statistics by Type ---")
print(stats)

# 4. Custom Function Example (The Q90 example from your notes)
def q90(x):
    return x.quantile(0.9)

custom_analysis = df.groupby("type")["moons"].agg(["mean", q90])
print("\n--- Custom Aggregation (Mean & 90th Percentile) ---")
print(custom_analysis)