# 🐍 Python Basic Rules & Data Types

### 🔢 1. Numeric Operations
* `17 / 3`  -> `5.66` (Classic division)
* `17 // 3` -> `5` (**Floor division** - discards the fractional part)
* `17 % 3`  -> `2` (**Modulo** - returns the remainder)
* `2 ** 3`  -> `8` (**Exponentiation** - power of)

---

### 📝 2. String Magic
* **Escape Characters:** `'it\'s'` -> Use `\` to include a single quote inside a single-quoted string.
* **Repetition:** `3 * "ha"` -> `"hahaha"`
* **Immutability:** `word[0] = "J"` **RAISES AN ERROR!** Strings cannot be changed after they are created.

---

### ⚠️ 3. The List Copying Trap
* `b = a` -> Both variables point to the **same** list. Changing one affects the other!
* `b = a[:]` -> Creates a **shallow copy** (a real independent copy) of the list. This is the safe way.

---

### 🔄 4. Loops and Indentation
Python does not use curly braces `{}`; it uses **indentation (typically 4 spaces)** to define code blocks.
```python
while a < 10:
    print(a) # This line belongs to the loop because it is indented.