import pandas as pd
import os

def load_titanic_data(filepath="data/titanic.csv"):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_directory, filepath)
    try:
        return pd.read_csv(full_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {full_path}")
