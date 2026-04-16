import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a synthetic dataset
# We generate random data to demonstrate different distributions
np.random.seed(42)
normal_data = np.random.normal(loc=50, scale=10, size=1000) # Symmetric
right_skewed_data = np.random.exponential(scale=10, size=1000) # Right-Skewed

df = pd.DataFrame({
    'Normal': normal_data,
    'Skewed': right_skewed_data
})

# 2. Plotting a Symmetric (Normal) Histogram
plt.figure(figsize=(10, 5))
sns.histplot(df['Normal'], bins=30, kde=True, color='skyblue')
plt.title('Symmetric (Normal) Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Save the plot before showing
plt.savefig('normal_histogram.png')
plt.show()

# 3. Plotting a Skewed Histogram
plt.figure(figsize=(10, 5))
sns.histplot(df['Skewed'], bins=30, kde=True, color='salmon')
plt.title('Right-Skewed Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Save the plot
plt.savefig('skewed_histogram.png')
plt.show()

print("Histograms have been generated and saved successfully!")