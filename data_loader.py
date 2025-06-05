import os
import pandas as pd

def load_adult_dataset():
    """
    Load the Adult Income dataset from the data directory.
    Returns:
        pandas.DataFrame: The loaded dataset
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct path to the dataset
    data_path = os.path.join(current_dir, 'data', 'adult.csv')
    
    # Check if file exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Please run download_data.py first.")
    
    # Load the dataset
    df = pd.read_csv(data_path)
    
    return df
