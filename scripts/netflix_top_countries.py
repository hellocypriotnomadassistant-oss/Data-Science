import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Netflix data
df = pd.read_csv('data/netflix.csv')

# Split countries and explode to count each country separately
df['country'] = df['country'].fillna('')  # Fill NaN with empty string
df['country_list'] = df['country'].str.split(', ')
df_exploded = df.explode('country_list')

# Count the occurrences of each country
country_counts = df_exploded['country_list'].value_counts()

# Get the top 10 countries
top_10_countries = country_counts.head(10)

# Plot using seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_countries.values, y=top_10_countries.index, palette='viridis')
plt.title('Top 10 Countries by Netflix Content Production')
plt.xlabel('Number of Contents')
plt.ylabel('Country')
plt.show()