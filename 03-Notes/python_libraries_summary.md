# 📚 Python Ecosystem: Libraries, Packages, and Modules
*A comprehensive guide to the essential tools for Data Science.*

---

## 1. Core Definitions
- **Library:** A collection of reusable code modules and documentation.
- **Package:** An organized, distributable form of libraries.
- **Module:** A sub-component of libraries; contains functions, classes, and variables.
*Note: A library can contain multiple modules.*

## 2. Importing Libraries
If a feature is not in the Python Standard Library, it must be installed first (usually via `pip`) and then imported into your script.

**Basic Syntax:**
```python
import numpy
numpy.array([2,4,6])
import numpy as np
np.array([2,4,6])
from sklearn.metrics import precision_score, recall_score
from numpy import array
