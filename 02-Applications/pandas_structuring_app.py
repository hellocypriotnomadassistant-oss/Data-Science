import pandas as pd

# 1. Create a Sample Dataset
data = {
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'salary': [70000, 50000, 80000, 60000, 52000],
    'experience_years': [5, 2, 8, 4, 3]
}

df = pd.DataFrame(data)

# --- 2. Practice: Selecting ---
# Select only Name and Salary
selection = df[['name', 'salary']]

# --- 3. Practice: Filtering ---
# Find employees with more than 3 years of experience
experienced = df[df['experience_years'] > 3]

# --- 4. Practice: Sorting ---
# Sort by Salary from highest to lowest
sorted_df = df.sort_values(by='salary', ascending=False)

# --- 5. Practice: Slicing ---
# Get the first 3 rows using iloc
top_three = df.iloc[0:3]

# --- 6. Practice: Merging (Bonus) ---
# New data to merge
dept_info = pd.DataFrame({
    'department': ['IT', 'HR', 'Sales'],
    'location': ['Floor 1', 'Floor 2', 'Floor 3']
})

final_df = df.merge(dept_info, on='department')

print("--- Final Structured Data ---")
print(final_df)