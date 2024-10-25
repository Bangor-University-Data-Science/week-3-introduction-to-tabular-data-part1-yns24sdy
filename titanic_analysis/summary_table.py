import pandas as pd


def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.

    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.

    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary = pd.DataFrame(columns=['Feature', 'Data Type', 'Number of Unique Values', 'Has Missing Values'])

    for col in df.columns:
        feature = col

        data_type = df[col].dtype

        num_unique_values = df[col].nunique()

        has_missing_values = df[col].isnull().any()

        summary = pd.concat([summary, pd.DataFrame({
            'Feature': [feature],
            'Data Type': [data_type],
            'Number of Unique Values': [num_unique_values],
            'Has Missing Values': [has_missing_values]
        })], ignore_index=True)

    return summary


file_path = '/mnt/titanic.csv'
df = pd.read_csv(file_path)

summary_table = create_summary_table(df)

print('The summary table is:')
print(summary_table)
