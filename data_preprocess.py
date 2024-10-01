import pandas as pd

def preprocess_data(file_path):
    """
    Load financial data, handle missing values, and normalize.
    
    :param file_path: Path to financial data file.
    :return: Cleaned and normalized DataFrame.
    """
    data = pd.read_csv(file_path)
    
    # Fill missing values with 0 or other appropriate methods
    data.fillna(0, inplace=True)
    
    # Normalize columns (optional, depending on model)
    data['normalized_revenue'] = (data['revenue'] - data['revenue'].mean()) / data['revenue'].std()
    
    return data

