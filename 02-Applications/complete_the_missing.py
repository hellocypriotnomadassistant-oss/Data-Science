import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Read Data
df = pd.read_csv("new_data.csv")

# 2. See Unique Products with SET (Example of using Set for missing items)
unique_products = set(df['product'])
print(f"Unique Products Set: {unique_products}")

# 3. Format Names with LIST COMPREHENSION (Example of List Comp.)
df['product'] = [u.upper() for u in df['product']]

# 4. Calculation with NUMPY
df['total'] = df['quantity'] * df['price']

# 5. Grouping with PANDAS
summary = df.groupby('product')['total'].sum()
print("\n--- Sales Summary ---")
print(summary)

# 6. Visualization with MATPLOTLIB (Final Touch)
summary.plot(kind='bar', color='orange')
plt.title("Revenue Report by Product")
plt.show()
    