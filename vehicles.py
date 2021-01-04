import numpy as np
import pandas as pd

# --- Main ---
    
# Shape
df = pd.read_csv('data/vehicles.csv', low_memory=False)
df.shape
print(df.shape)
