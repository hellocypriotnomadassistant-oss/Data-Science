
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Create Sample Data (Simulating Lightning Strike Data)
data = {
    'date': pd.date_range(start='2016-01-01', end='2018-12-31', freq='D'),
    'number_of_strikes': np.random.randint(1000, 50000, size=1096)
}
df = pd.DataFrame(data)

# 2. Datetime Transformation (CRITICAL STEP)
df['date'] = pd.to_datetime(df['date'])

# 3. Feature Engineering (Extracting Time Units)
df['week'] = df['date'].dt.strftime('%Y-W%V')
df['month'] = df['date'].dt.strftime('%Y-%m')
df['quarter'] = df['date'].dt.to_period('Q').astype(str) # Converting to string for plotting
df['year'] = df['date'].dt.strftime('%Y')

# 4. Weekly Analysis for 2018
df_2018 = df[df['year'] == '2018'].groupby('week')['number_of_strikes'].sum().reset_index()

# 5. Visualization - Weekly Strikes in 2018
plt.savefig('weekly_strikes_2018.png') # Grafiği dosya olarak kaydeder
plt.show()
plt.figure(figsize=(15, 6))
sns.barplot(data=df_2018, x='week', y='number_of_strikes')
plt.xticks(rotation=45, fontsize=8)
plt.title('Total Lightning Strikes per Week (2018)')
plt.ylabel('Number of Strikes')
plt.tight_layout()
plt.show()

# 6. Grouped Bar Chart (Year-over-Year Comparison)
# Formatting Quarter for easier grouping
df['quarter_num'] = df['quarter'].str[-2:] # Extracts Q1, Q2 etc.

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='quarter_num', y='number_of_strikes', hue='year', estimator=sum)
plt.title('Comparison of Strikes by Quarter (2016-2018)')
plt.ylabel('Total Strikes (Millions)')
plt.show()

print("Analysis and Visualizations completed successfully!")