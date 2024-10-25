# Create module
import pandas as pd

def create_feature_type_dict(df):
    # Define an empty dictionary to store feature types
    feature_types = {'numerical': [], 'categorical': []}

    # Traverse each column
    for col in df.columns:
        # Determine whether the data type is numeric
        if df[col].dtype in ['int64', 'float64']:
            # Determine whether it is continuous (if the number of unique values is large, it is considered continuous)
            if df[col].nunique() > 10:
                feature_types['numerical'].append(col)
            else:
                feature_types['numerical'].append(col)
        else:
            # Determine whether it is nominal (if the number of unique values is large, it is considered nominal)
            if df[col].nunique() > 10:
                feature_types['categorical'].append(col)
            else:
                feature_types['categorical'].append(col)

    # Show feature type dictionary
    return feature_types
