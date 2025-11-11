# =============================================================
#   PANDAS SERIES — CREATION, INDEXING, AND NUMPY INTEGRATION
# =============================================================
# Demonstrates Series creation, label-based access,
# element comparison, and NumPy vectorized operations.

import numpy as np
import pandas as pd

# =============================================================
#   Create a Basic Series
# =============================================================
s = pd.Series([4, 7, np.nan, -5, 3])
print(s)
print(s.array)     # underlying array of values
print(s.index)     # index labels of the Series

# =============================================================
#   Create Series with Custom Index
# =============================================================
s2 = pd.Series([4, 7, np.nan, -5, 3], index=["c", "a", "b", "d", "e"])

# =============================================================
#   Element Access and Logical Comparison
# =============================================================
print(f"{s[0] == s2['c'] = }")     # access by position vs. label
print(f"{s2[['c', 'b']] = }")      # select multiple elements by labels

# =============================================================
#   Apply NumPy Function to the Series
# =============================================================
es = np.exp(s)
print(f"{es}")     # exponential transformation of Series elements
