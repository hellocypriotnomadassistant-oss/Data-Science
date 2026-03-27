# 🚦 Python Control Flow Summary

### 🧠 1. Decision Structures (if / elif / else)
In Python, conditions start with `if`, continue with `elif` (else if), and end with `else`.
* **Important:** Indentation (4 spaces) is vital for the code to run.

---

### 🔁 2. Loops (for & while)
* **for:** Iterates over a list, tuple, or string.
* **range(5):** Generates numbers from 0 to 4 (5 is **not** included!).
* **break:** Terminates the loop entirely.
* **continue:** Skips the current iteration and moves to the next step.



[Image of Python for loop flowchart]


---

### 🔄 3. Using `else` with Loops
If a loop finishes normally **without** being interrupted by a `break`, the `else` block executes.
> It basically means: "Run this if no break occurred."

---

### 🔧 4. Functions (def)
Functions are defined using the `def` keyword.
* **return:** Returns a value. If not specified, the function returns `None`.
* **args & kwargs:** * `*args`: Unlimited positional arguments (passed as a **Tuple**).
    * `**kwargs`: Unlimited keyword arguments (passed as a **Dictionary**).

---

### ⚠️ 5. The Critical Trap (Mutable Default Arguments)
Never use an empty list `[]` as a default argument in a function definition! The list is created only once and "persists" (grows) across multiple calls.
* **The Right Way:** Use `L=None` and initialize inside the function: `if L is None: L = []`.

---

### ⚡ 6. Lambda and Unpacking
* **Lambda:** `add = lambda x, y: x + y` (Anonymous, single-line functions).
* **Unpacking:** Using `*` to unpack a list or `**` to unpack a dictionary when passing them into a function.

---

### 🎨 7. Coding Style (PEP 8)
1. Use **4-space** indentation.
2. Use `snake_case` for functions and variables.
3. Use `CamelCase` (PascalCase) for classes.
4. Keep line length to a maximum of **79 characters**.