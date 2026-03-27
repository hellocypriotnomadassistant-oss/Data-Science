# ⚙️ Using the Python Interpreter

### 🔹 1. How to Start Python?
* **Windows:** `python` or `py`
* **Linux / Mac:** `python3`
* **Exit:** `quit()` or `Ctrl + Z` (Windows) / `Ctrl + D` (Mac/Linux)

---

### 🔹 2. Execution Modes
1. **Interactive Mode:** The `>>>` prompt appears. You type code line by line and get instant results.
2. **Script Mode:** Run the entire file at once using the `python file.py` command.

---

### 🔹 3. Advanced Execution Commands
* **Single Line Code:** `python -c "print(5+5)"`
* **Running a Module:** `python -m module_name`
* **Interactive Mode After Script:** `python -i file.py` (The script finishes but the terminal stays open, allowing you to inspect variables).

---

### 🔹 4. Passing Arguments (sys.argv) ⚠️
Used to send external data to a file:
`python file.py data1 data2`

**Accessing Within Code:**
```python
import sys
print(sys.argv) # Output: ['file.py', 'data1', 'data2']