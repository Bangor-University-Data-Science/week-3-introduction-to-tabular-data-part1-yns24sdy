data_type = df.dtypes

unique_value_count = df.nunique()

missing_value = df.isnull().sum()

summary_table = pd.DataFrame({
    'Data type': data_type,
    'Number of unique values': unique_value_count,
    'Number of missing values': missing_value
})

summary_table
