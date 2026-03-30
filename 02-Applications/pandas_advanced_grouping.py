import pandas as pd

# 1. Creating a sample dataset (Shirts & Colors example)
data = {
    'color': ['blue', 'blue', 'red', 'red', 'blue', 'red'],
    'type': ['shirt', 'pants', 'shirt', 'pants', 'shirt', 'shirt'],
    'price_usd': [20, 45, 22, 50, 18, 25],
    'mass_g': [150, 400, 160, 420, 145, 155]
}

df = pd.DataFrame(data)

print("--- Original Inventory ---")
print(df)

# 2. Basic Grouping (Average price by color)
print("\n--- Average Price by Color ---")
print(df.groupby('color')['price_usd'].mean())

# 3. Multi-Column Grouping with size()
print("\n--- Count of Items (Color & Type) ---")
print(df.groupby(['color', 'type']).size())

# 4. Advanced Aggregation (The most powerful way)
# Different operations for different columns
advanced_analysis = df.groupby('color').agg({
    'price_usd': ['mean', 'max'],
    'mass_g': ['sum', 'std']
})

print("\n--- Advanced Aggregation Result ---")
print(advanced_analysis)

# 5. Removing MultiIndex for a simpler look
simple_df = df.groupby(['color', 'type'], as_index=False).mean()
print("\n--- Simplified (Flat) DataFrame ---")
print(simple_df)
