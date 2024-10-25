import pandas as pd

# Load data
df = pd.read_csv('/mnt/titanic.csv')

print('Basic information of data:')
df.info()
print('The first few rows of data:')
print(df.head())

# Define an empty dictionary to store feature types
feature_types = {}

# Traverse each column
for col in df.columns:
    # Determine whether the data type is numeric
    if df[col].dtype in ['int64', 'float64']:
        # Determine whether it is continuous (if the number of unique values is large, it is considered continuous)
        if df[col].nunique() > 10:
            feature_types[col] = 'numerical_continuous'
        else:
            feature_types[col] = 'numerical_discrete'
    else:
        # Determine whether it is nominal (if the number of unique values is large, it is considered nominal)
        if df[col].nunique() > 10:
            feature_types[col] = 'categorical_nominal'
        else:
            feature_types[col] = 'categorical_ordinal'

# Show feature type dictionary
print('Feature type dictionary:')
print(feature_types)
