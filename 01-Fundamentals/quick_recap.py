import numpy as np
import pandas as pd

# 1. Quick Data Structures Recap
my_list = [1, 2, 2, 3]
my_set = set(my_list)  # {1, 2, 3} - unique elements
my_dict = {"tool": "Pandas", "type": "Analysis"}

print(f"Set (Unique): {my_set}")
print(f"Dictionary Value: {my_dict['tool']}\n")

# 2. NumPy Speed
np_array = np.array([1, 2, 3])
print(f"NumPy Array: {np_array * 2} (Vectorized operation)\n")

# 3. Pandas Power
data = {'Name': ['Alice', 'Bob'], 'Score': [85, 92]}
df = pd.DataFrame(data)
print("--- Pandas DataFrame ---")
print(df)