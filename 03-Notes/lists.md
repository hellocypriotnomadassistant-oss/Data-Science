# 📌 Python Lists – Summary

### 🔹 1. Lists are Mutable
Lists are a mutable data type. You can add, delete, or modify elements.
👉 **The list remains the same object; only its content changes.**

---

### 🔹 2. Adding Elements
* **append():** Adds an element to the end of the list.
    `fruits.append("kiwi")`
* **insert():** Adds an element at a specific index.
    `fruits.insert(1, "orange")` (Takes index and value)

---

### 🔹 3. Removing Elements
* **remove():** Deletes by value. `fruits.remove("banana")`
* **pop():** Deletes by index. `fruits.pop(2)`

---

### 🔹 4. Modifying Elements
`fruits[1] = "mango"`
✔ New value is assigned directly via the index.

---

### 🔹 5. String vs List (Important ⚠️)
* ❌ **String (Immutable):** `name[0] = "V"` -> **ERROR!**
* ✅ **List (Mutable):** `my_list[0] = "V"` -> **WORKS.**

---

### 🚀 Quick Cheat Sheet
* **append()** -> to the end
* **insert()** -> in between
* **remove()** -> delete by value (name)
* **pop()** -> delete by index (order)

---

### 🔹 6. Slicing
`list[start:stop]` -> The stop index is **not** included!
* `fruits[0:2]` -> Returns elements at index 0 and 1.
* `fruits[:3]` -> Starts from the beginning and goes up to index 3.

---

### 🔹 7. List Mathematical Operations
* **Concatenation (+):** Merges two lists. `[1,2] + [3,4]` -> `[1,2,3,4]`
* **Repetition (*):** Repeats the list. `['a'] * 3` -> `['a', 'a', 'a']`

---

### 🔹 8. Other Important Methods
* **in:** Is the element in the list? `"apple" in fruits` -> `True/False`
* **count():** How many times does the element appear? `my_list.count("apple")`
* **sort():** Sorts the list alphabetically or from smallest to largest.
* **clear():** Completely empties the list.