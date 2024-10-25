def create_summary_table(df):
    if df.empty:
        print("The input data box is empty")
        return

    summary_df = pd.DataFrame(columns=['Feature Name', 'Data Type', 'Number of Unique Values', 'Has Missing Values'])

    for column in df.columns:
        feature_name = column
        data_type = df[column].dtype
        num_unique_values = df[column].nunique()
        has_missing_values = df[column].isnull().any()

        summary_df = pd.concat([summary_df, pd.DataFrame([{'Feature Name': feature_name, 'Data Type': data_type, 'Number of Unique Values': num_unique_values, 'Has Missing Values': has_missing_values}])], ignore_index=True)

    return summary_df

create_summary_table(df)
