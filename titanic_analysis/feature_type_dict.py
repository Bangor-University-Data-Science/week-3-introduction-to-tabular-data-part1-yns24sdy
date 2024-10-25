import pandas as pd

def create_feature_type_dict(df):
    feature_types = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            feature_types[column] = 'numerical'
        else:
            feature_types[column] = 'categorical'
    return feature_types
