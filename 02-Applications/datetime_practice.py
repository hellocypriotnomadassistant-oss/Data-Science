from datetime import datetime
import numpy as np
import pandas as pd

# --- 1. Basic Python Datetime Module ---
# Example: Converting String to Datetime (Parsing)
date_str = "25/11/2022"
date_dt = datetime.strptime(date_str, "%d/%m/%Y")
print(f"Converted Datetime Object: {date_dt}")

# Example: Converting Datetime back to String (Formatting)
formatted_date = date_dt.strftime("%B %d, %Y")
print(f"Formatted Date String: {formatted_date}")


# --- 2. NumPy Datetime Operations ---
# Example: Creating a NumPy datetime64 array
numpy_date = np.array(['2022-11-25'], dtype='datetime64[D]')
print(f"NumPy Date Array: {numpy_date}")

# Example: Date Arithmetic with NumPy
tomorrow = numpy_date + np.timedelta64(1, 'D')
print(f"NumPy Arithmetic (Tomorrow): {tomorrow}")


# --- 3. Pandas Datetime Operations ---
# Example: Creating a Pandas Series and converting to datetime
data = {'date_strings': ['2022-01-01', '2022-06-15', '2022-12-31']}
df = pd.DataFrame(data)
df['date_dt'] = pd.to_datetime(df['date_strings'])

# Example: Using the .dt accessor to extract year and month
df['year'] = df['date_dt'].dt.year
df['month_name'] = df['date_dt'].dt.month_name()

print("\nPandas DataFrame Output:")
print(df)