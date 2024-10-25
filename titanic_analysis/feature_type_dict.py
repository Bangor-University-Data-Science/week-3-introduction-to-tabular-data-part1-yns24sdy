import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }
    
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            if df[col].nunique() > 10:
                feature_types['numerical']['continuous'].append(col)
            else:
                feature_types['numerical']['discrete'].append(col)
        elif pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == 'object':
            if col in ['Pclass', 'AgeGroup']: 
                feature_types['categorical']['ordinal'].append(col)
            else:
                feature_types['categorical']['nominal'].append(col)
    
    return feature_types
