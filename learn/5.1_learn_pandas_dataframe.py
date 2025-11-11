# =============================================================
#   PANDAS DATAFRAME — CREATION, INDEXING, AND NUMPY OPERATIONS
# =============================================================
# This script demonstrates creation of DataFrames, access by index
# and label, and applying NumPy universal functions to the data.

import numpy as np
import pandas as pd

# =============================================================
#   Create DataFrame from Dictionary
# =============================================================
data = {
    "A": [4, 7, np.nan, -5, 3],
    "B": [10, 21, 13, np.nan, -8]
}
df = pd.DataFrame(data, index=["c", "a", "b", "d", "e"])
print(df)
print(df.values)
print(df.index)
print(df.columns)

# =============================================================
#   Element Access and Comparison
# =============================================================
print(f"{df.loc['c', 'A'] = }")      # access element by label
print(f"{df.iloc[0, 0] = }")         # access element by position
print(f"{df.loc[['c', 'b'], ['A', 'B']] = }")  # multiple selection

# =============================================================
#   Apply NumPy Function to DataFrame
# =============================================================
edf = np.exp(df)
print(f"\nExponential of DataFrame values:\n{edf}")