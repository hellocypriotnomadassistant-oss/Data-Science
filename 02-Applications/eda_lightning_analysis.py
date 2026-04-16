import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Setup & Data Creation (Simulating the NOAA Dataset)
# In a real scenario, you would use: df = pd.read_csv('lightning_data.csv')
data = {
    'date': pd.date_range(start='2018-01-01', end='2018-12-31', freq='D'),
    'number_of_strikes': np.random.randint(100, 5000, size=365),
    'center_point_geom': ['Point(25.1 -80.2)'] * 365
}
df = pd.DataFrame(data)

# 2. Data Cleaning
df['date'] = pd.to_datetime(df['date'])
df = df.drop_duplicates()

# 3. Feature Engineering (Creating new time columns)
df['month'] = df['date'].dt.month_name()
df['weekday'] = df['date'].dt.day_name()
df['week_number'] = df['date'].dt.isocalendar().week

# 4. Sorting - Finding the top 5 days with most strikes
top_days = df.sort_values(by='number_of_strikes', ascending=False).head(5)
print("--- Top 5 Strike Days ---")
print(top_days)

# 5. Analysis: Grouping by Weekday
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_weekday = df.groupby('weekday')['number_of_strikes'].mean().reindex(weekday_order)

# 6. Visualization: Distribution by Weekday
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='weekday', y='number_of_strikes', order=weekday_order)
plt.title('Lightning Strike Distribution by Weekday (2018)')
plt.savefig('weekday_distribution.png') # Saves the result for your GitHub
plt.show()

# 7. Percentage Calculation (August Surge Example)
monthly_totals = df.groupby('month')['number_of_strikes'].sum()
yearly_total = df['number_of_strikes'].sum()
august_pct = (monthly_totals['August'] / yearly_total) * 100

print(f"\nAugust represents {august_pct:.2f}% of the yearly total strikes.")

# Save the figure immediately after plotting (MUST be before plt.show()!)
plt.savefig('lightning_distribution.png') 
plt.show()