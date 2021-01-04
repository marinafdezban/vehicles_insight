import numpy as np
import pandas as pd

# --- Main ---
    
# Shape
df = pd.read_csv('data/vehicles.csv', low_memory=False)
shape = df.shape
size = df.size
df_columns = df.columns
df_type = df.dtypes
nulls = df.isnull().sum(axis=1)
df_min = df.min()
df_max = df.max()

print('Data Frame shape is: ' + str(shape))
print('Data Frame length is: ' + str(size))
print('Data Frame columns are: ' + str(df_columns))
print('Data Frame type is: ' + str(df_type))
print('Data Frame nulls: ' + str(nulls))
print('Data Frame min value is: ' + str(df_min))
print('Data Frame max value is: ' + str(df_max))
