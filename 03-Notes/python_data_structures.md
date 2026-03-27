# 🧠 String, List, and Tuple – Quick Summary

## 🔹 1. Common Features
These three data structures are:
* **Ordered:** Elements are accessed by index (e.g., `[0]`, `[1]`).
* **Iterable:** Can be looped through using a `for` loop.
* **Collection:** Used to store multiple items together.

---

## 🔤 2. String (Text Data)
* **Example:** `name = "Alice"`
* ❌ **Immutable:** Cannot be changed after creation.
* ✔️ Stores only characters (text).
* 💡 **Key Fact:** Even if it looks like you are changing a string, Python actually creates a brand-new one in memory.

---

## 📦 3. List (The Flexible One)
* **Example:** `my_list = ["apple", 5, 3.14]`
* ✔️ **Mutable:** You can change, add, or remove elements.
* ✔️ Can store different data types together.
* 🚀 **Usage:** Data storage, sorting, searching, and dynamic collections.

---

## 🔒 4. Tuple (The Secure One)
* **Example:** `my_tuple = (10, 20)`
* ❌ **Immutable:** Cannot be changed once defined.
* ✔️ Can store different data types.
* 🛡️ **Usage:** Fixed data, returning multiple values from functions, or as dictionary keys.

---

## ⚖️ Summary Comparison Table

| Feature | String | List | Tuple |
| :--- | :--- | :--- | :--- |
| **Mutable?** | ❌ No | ✅ Yes | ❌ No |
| **Data Type** | Text Only | Any Type | Any Type |
| **Speed/Security** | Medium | Low | High |

---
> **Logic:** If the data will change → **List**. If it stays constant → **Tuple**. For text → **String**.