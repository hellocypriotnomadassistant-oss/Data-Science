import pandas as pd

# --- Setup Sample Data ---
df_planets = pd.DataFrame({
    'planet': ['Mars', 'Jupiter', 'Saturn'],
    'temp_c': [-65, -110, -140]
})

df_moons = pd.DataFrame({
    'planet': ['Mars', 'Jupiter', 'Earth'],
    'moon_count': [2, 79, 1]
})

# 1. Using concat() (Vertical)
# Creating a new batch of data
df_new_planets = pd.DataFrame({
    'planet': ['Venus', 'Neptune'],
    'temp_c': [464, -201]
})

vertical_stack = pd.concat([df_planets, df_new_planets], axis=0).reset_index(drop=True)
print("--- Vertical Concat (Adding Rows) ---")
print(vertical_stack, "\n")

# 2. Using merge() (Inner Join)
# Only joins planets that exist in both DataFrames (Mars & Jupiter)
inner_merge = pd.merge(df_planets, df_moons, on='planet', how='inner')
print("--- Inner Merge (Common Planets) ---")
print(inner_merge, "\n")

# 3. Using merge() (Outer Join)
# Keeps all planets, fills missing moon counts with NaN
outer_merge = pd.merge(df_planets, df_moons, on='planet', how='outer')
print("--- Outer Merge (All Planets) ---")
print(outer_merge, "\n")

# 4. Using merge() (Left Join)
# Keeps all rows from df_planets
left_merge = pd.merge(df_planets, df_moons, on='planet', how='left')
print("--- Left Merge (Keep all from Left) ---")
print(left_merge)
