def display_unique_values(df, categorical_features):
    unique_values = {}
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique()
    return unique_values

categorical_features = ['Survived', 'Pclass', 'Sex', 'Embarked']
unique_values = display_unique_values(df, categorical_features)
for feature, values in unique_values.items():
    print(f'The unique values of {feature}: {values}')
