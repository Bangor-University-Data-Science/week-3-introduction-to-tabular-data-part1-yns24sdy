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
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            if df[col].nunique() > 10:
                feature_types['numerical']['continuous'].append(col)
            else:
                feature_types['numerical']['discrete'].append(col)
        else:
            if df[col].nunique() > 10:
                feature_types['categorical']['nominal'].append(col)
            else:
                feature_types['categorical']['ordinal'].append(col)

    return feature_types

print(create_feature_type_dict(pd.read_csv('/mnt/titanic.csv')))
