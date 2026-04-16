# 📌 Datetime Manipulation Cheat Sheet

A comprehensive guide for handling dates and times in Python, NumPy, and Pandas.

---

## 1. Format Codes (Strftime & Strptime)
Used to parse and format datetime strings. Common tokens include:

* **%Y**: Year (e.g., 2026)
* **%m**: Month (01–12)
* **%d**: Day of the month (01–31)
* **%H**: Hour (24-hour clock)
* **%I**: Hour (12-hour clock)
* **%p**: AM/PM indicator
* **%M**: Minute
* **%S**: Second

---

## 2. Core Functions (Python Standard Library)

### 🔹 String → Datetime (Parsing)
```python
from datetime import datetime
dt_object = datetime.strptime("25/11/2022", "%d/%m/%Y")

timestamp = datetime.timestamp(dt_object)
dt_from_ts = datetime.fromtimestamp(timestamp)

# Convert format directly
new_format = datetime.strptime("25/11/2022", "%d/%m/%Y").strftime("%Y-%m-%d")

import pytz
from datetime import datetime

# Convert to a different timezone
tokyo_time = ny_time.astimezone(pytz.timezone('Asia/Tokyo'))

df['date_column'] = pd.to_datetime(df['date_column'])

df['year'] = df['date_column'].dt.year
df['month'] = df['date_column'].dt.month
df['day'] = df['date_column'].dt.day

