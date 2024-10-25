import pandas as pd


def load_titanic_data(filepath: str) -> pd.DataFrame:
    # Load the data
    data = pd.read_csv(filepath)

    return data


# Load the dataset
titanic_data = load_titanic_data('/mnt/titanic.csv')

print("Basic information of the dataset:")
titanic_data.info()
print("The first few rows of the dataset:")
print(titanic_data.head())
