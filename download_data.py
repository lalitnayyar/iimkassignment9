import os
import pandas as pd
import urllib.request
import zipfile
import ssl

def download_adult_dataset():
    """
    Downloads the Adult Income Dataset from UCI Machine Learning Repository
    Returns the path to the downloaded CSV file
    """
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Define URLs
    data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    test_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
    
    # Column names for the dataset
    columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
    ]
    
    try:
        # Download training data
        print("Downloading training data...")
        train_data = pd.read_csv(data_url, names=columns, skipinitialspace=True)
        
        # Download test data
        print("Downloading test data...")
        test_data = pd.read_csv(test_url, names=columns, skipinitialspace=True, skiprows=1)
        
        # Clean the income column (remove dots from test data)
        test_data['income'] = test_data['income'].str.replace('.', '')
        
        # Combine the datasets
        full_data = pd.concat([train_data, test_data], ignore_index=True)
        
        # Save to CSV
        output_path = os.path.join('data', 'adult.csv')
        full_data.to_csv(output_path, index=False)
        print(f"Dataset saved to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        return None

if __name__ == "__main__":
    download_adult_dataset()
