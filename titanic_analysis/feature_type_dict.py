import pandas as pd

def create_feature_type_dict(df: pd.DataFrame) -> dict:
    """Classifies features into numerical and categorical types."""
    feature_types = {}
    numerical_columns = []
    categorical_columns = []
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            numerical_columns.append(column)
        else:
            categorical_columns.append(column)
    if numerical_columns:
        feature_types['numerical'] = numerical_columns
    if categorical_columns:
        feature_types['categorical'] = categorical_columns
    return feature_types
