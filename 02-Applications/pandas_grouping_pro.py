import pandas as pd

# ---------------------------------------------------------
# 1. Dataset Creation
# ---------------------------------------------------------
# We create a sample dictionary to simulate inventory data
data = {
    'item_type': ['shirt', 'shirt', 'pants', 'pants', 'shirt', 'pants'],
    'color': ['red', 'blue', 'red', 'blue', 'red', 'green'],
    'price_usd': [20, 25, 50, 55, 22, 48],
    'mass_g': [150, 160, 400, 420, 155, 390]
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df, "\n")

# ---------------------------------------------------------
# 2. Basic Grouping
# ---------------------------------------------------------
# Finding the average price for each item type
avg_price_by_type = df.groupby('item_type')['price_usd'].mean()

print("--- Average Price by Item Type ---")
print(avg_price_by_type, "\n")

# ---------------------------------------------------------
# 3. Advanced Aggregation (The Power of agg)
# ---------------------------------------------------------
# We can apply different functions to different columns simultaneously
summary_stats = df.groupby('color').agg({
    'price_usd': ['mean', 'max'],
    'mass_g': ['mean', 'std']
})

print("--- Multiple Statistics per Color ---")
print(summary_stats, "\n")

# ---------------------------------------------------------
# 4. Flattening the Result (Best Practice for Exporting)
# ---------------------------------------------------------
# Using as_index=False prevents the grouped column from becoming the index
flat_analysis = df.groupby(['item_type', 'color'], as_index=False).sum()

print("--- Flattened Grouping (Standard DataFrame) ---")
print(flat_analysis)

# ---------------------------------------------------------
# 5. Quick Insight: Group Sizes
# ---------------------------------------------------------
print("\n--- Count of Items in Each Category ---")
print(df.groupby(['item_type', 'color']).size())
