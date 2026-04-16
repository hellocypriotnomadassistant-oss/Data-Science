import pandas as pd
import numpy as np

# Scenario: Creating a synthetic dataset for "Marsupials"
data = {
    'animal_id': range(1, 11),
    'species': ['Kangaroo', 'Koala', 'Wombat', 'Kangaroo', 'Koala', 'Wombat', 'Wallaby', 'Kangaroo', 'Wallaby', 'Koala'],
    'tail_length_m': [1.2, 0.1, 0.15, 1.1, 0.08, 0.12, 0.8, 1.3, 0.75, 0.05],
    'pouch_volume_cm3': [500, 50, 80, 450, 45, 75, 300, 550, 280, 40],
    'weight_kg': [85, 12, 25, 70, 10, 22, 18, 90, 15, 9]
}

df = pd.DataFrame(data)

print("--- Original Data ---")
print(df.head())

# 1. SORTING - Sorting by weight in descending order
df_sorted = df.sort_values(by='weight_kg', ascending=False)

# 2. EXTRACTING - Selecting only specific columns of interest
df_extracted = df[['species', 'tail_length_m', 'pouch_volume_cm3']]

# 3. FILTERING - Selecting animals with tail length greater than 1.0 meter
df_filtered = df[df['tail_length_m'] > 1.0]

# 4. SLICING - Getting species and weight for the first 5 rows
df_sliced = df.loc[0:4, ['species', 'weight_kg']]

# 5. GROUPING / BINNING - Categorizing based on tail length
# Defining the range for bins and their corresponding labels
bins = [0, 0.2, 0.9, 1.5]
labels = ['Short', 'Medium', 'Long']
df['tail_category'] = pd.cut(df['tail_length_m'], bins=bins, labels=labels)

# 6. MERGING - Simulating a merge with a diet information dataset
diet_info = {
    'species': ['Kangaroo', 'Koala', 'Wombat', 'Wallaby'],
    'diet': ['Herbivore', 'Herbivore', 'Herbivore', 'Herbivore']
}
df_diet = pd.DataFrame(diet_info)
df_final = pd.merge(df, df_diet, on='species')

print("\n--- Final Structured Data (Sorted by Tail Length) ---")
print(df_final.sort_values(by='tail_length_m'))

# Optional: Exporting the final result as a CSV for GitHub
# df_final.to_csv('structured_marsupial_data.csv', index=False)