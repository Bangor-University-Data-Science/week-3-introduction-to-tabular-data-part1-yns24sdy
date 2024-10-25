import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return pd.DataFrame() 
    except ValueError as ve:
        print(f"Error: {ve}")
        return pd.DataFrame() 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()  
