import datetime as dt
from datetime import timezone, timedelta

# --- 1. Timedelta Calculations ---
today = dt.date.today()
ten_days_later = today + timedelta(days=10)

print(f"Today: {today}")
print(f"10 Days Later: {ten_days_later}")
print("-" * 30)

# --- 2. Naive vs. Aware Objects ---
# Naive: Has no timezone information
naive_now = dt.datetime.now()

# Aware: Specifically set to UTC timezone
aware_now = dt.datetime.now(timezone.utc)

print(f"Naive (Timezone Info): {naive_now.tzinfo}")  # Returns: None
print(f"Aware (Timezone Info): {aware_now.tzinfo}")  # Returns: UTC
print("-" * 30)

# --- 3. Formatting (strftime) ---
# Formatting the aware datetime into a human-readable string
readable_format = aware_now.strftime('%d %B %Y, %A, %H:%M')
print(f"Readable Format (UTC): {readable_format}")

# --- 4. Total Seconds Example ---
duration = timedelta(hours=5, minutes=30)
print(f"Duration: {duration}")
print(f"Total Seconds: {duration.total_seconds()}s")