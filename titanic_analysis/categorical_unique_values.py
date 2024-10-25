import pandas as pd

def display_unique_values(df, categorical_features):
    unique_dict = {}
    for feature in categorical_features:
        unique_dict[feature] = df[feature].unique()
    return unique_dict
