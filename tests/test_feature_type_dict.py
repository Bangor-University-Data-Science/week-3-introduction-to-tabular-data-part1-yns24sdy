import pandas as pd

def create_feature_type_dict(df):
    feature_type_dict = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            feature_type_dict[column] = 'numerical'
        else:
            feature_type_dict[column] = 'categorical'
    return feature_type_dict
