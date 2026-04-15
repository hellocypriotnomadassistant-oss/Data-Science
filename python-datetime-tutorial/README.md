# 🐍 Python Datetime Module Guide

This repository contains comprehensive notes and practical examples for working with the Python `datetime` module.

---

## 📦 Core Data Types
* **date**: Represents date only (Year, Month, Day).
* **time**: Represents time only (Hour, Minute, Second, Microsecond).
* **datetime**: A combination of date and time.
* **timedelta**: Represents the difference (duration) between two dates or times.
* **timezone**: A class that implements the `tzinfo` abstract base class as a fixed offset from the UTC.

---

## 🌍 Naive vs. Aware Objects
* **Naive**: Objects that do not have enough information to unambiguously locate themselves relative to other date/time objects (no timezone).
* **Aware**: Objects that have timezone information (`tzinfo`) and can represent a specific moment in time.

---

## ⏱️ timedelta logic
* Internal storage: Only `days`, `seconds`, and `microseconds` are stored.
* Other units (hours, minutes, weeks) are automatically converted.
* **Pro Tip**: Always use `.total_seconds()` instead of `.seconds` to get the full duration.

---

## 📅 Formatting (strftime & strptime)
* **strftime()**: Convert `datetime` object → `string` (Output).
* **strptime()**: Convert `string` → `datetime` object (Input/Parsing).