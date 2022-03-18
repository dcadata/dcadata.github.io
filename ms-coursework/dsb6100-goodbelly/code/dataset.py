"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### IMPORTS AND TRANSFORMS DATASET FOR USE THROUGHOUT PROJECT ###

### IMPORTS ###

# Import GB dataset filepath
from goodbelly.variables import dataset
# Import pandas, the module that handles dataframes
from pandas import read_csv
# Import numpy, the module that handles arrays, log, and exp
from numpy import log

### SET UP DATASET ###

# Read dataset into a pandas dataframe w/ appropriate columns
df = read_csv(dataset, sep='\t')
# Dataset needs to be imported twice because otherwise df_log becomes an alias for df, but we want it to be a separate object
df_log = read_csv(dataset, sep='\t')

# Transform all columns (all Xs and Y) to their natural logarithm
# Only want to transform the following numeric columns
numeric_cols = ['sales_volume',
                'arp', 'sales_rep', 'endcap',
                'demo', 'demo13', 'demo45',
                'natural', 'fitness']
for col in df_log.columns:
    if col in numeric_cols:
        # Only transform numeric columns
        df_log[col] = df_log[col].apply(lambda i: log(i+0.001)) # Numpy's log function is actually ln
    else:
        # If a column is not a numeric column, drop it
        df_log = df_log.drop(columns=col)