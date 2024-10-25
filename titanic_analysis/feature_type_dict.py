def create_feature_type_dict(df):
    feature_types = {}

    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            if df[column].nunique() > 20:
                feature_types[column] = 'numerical_continuous'
            else:
                feature_types[column] = 'numerical_discrete'
        else:
            if df[column].nunique() > 10:
                feature_types[column] = 'categorical_nominal'
            else:
                feature_types[column] = 'categorical_ordinal'

    return feature_types

# Use functions for classification
feature_types = create_feature_type_dict(df)

# Output classification result
feature_types
