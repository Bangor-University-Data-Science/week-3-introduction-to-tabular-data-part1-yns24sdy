import pandas as pd
import os

def load_titanic_data(filepath: str = "data/titanic.csv") -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    # Use the provided filepath or a relative path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(current_dir, filepath)

    if not os.path.isfile(absolute_path):
        raise FileNotFoundError(f"File not found: {absolute_path}")

    return pd.read_csv(absolute_path)
