def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.

    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.

    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_table = pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes,
        'Number of Unique Values': df.nunique(),
        'Has Missing Values': df.isnull().any()
    })

    return summary_table
