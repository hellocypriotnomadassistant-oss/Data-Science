import numpy as np

print("--- NumPy Datetime & Time Series Analysis ---")

# 1. Creating Datetime64 objects with different precisions
# NumPy stores dates as 64-bit integers for high performance
date_day = np.datetime64('2026-04-15')
date_min = np.datetime64('2026-04-15T15:30')

print(f"Day Precision: {date_day}")
print(f"Minute Precision: {date_min}")

# 2. Generating Date Ranges using arange (Vectorized approach)
# Automatically creates an array of all days in April 2026
april_days = np.arange('2026-04-01', '2026-05-01', dtype='datetime64[D]')

print(f"\nFirst 5 days of April 2026:\n{april_days[:5]}")
print(f"Total number of days in the array: {len(april_days)}")

# 3. Arithmetic Operations with timedelta64
# Adding 10 days to a specific date point
future_date = date_day + np.timedelta64(10, 'D')
print(f"\nCalculated date (10 days after April 15): {future_date}")

# 4. Working with Business Days (Financial Analysis)
# Checks if the given date is a business day (Monday to Friday)
is_work_day = np.is_busday(date_day)
print(f"\nIs {date_day} a business day? {is_work_day}")

# Calculating the total count of business days between two dates
# (Useful for calculating working days in a month)
bus_day_count = np.busday_count('2026-04-01', '2026-05-01')
print(f"Total business days in April 2026: {bus_day_count}")

# 5. Handling Missing Values (NaT - Not a Time)
invalid_entry = np.datetime64('NaT')
print(f"\nExample of a missing time value: {invalid_entry}")