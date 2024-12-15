import pandas as pd


### Initialize the function
# ---------------------------
# import os
# import sys

# # 確保項目根目錄在模組路徑中
# project_root = os.path.abspath("COVID-19-TIME-SERIES-PREDICT") 
# if project_root not in sys.path:
#     sys.path.append(project_root)

# # 導入模組
# from utils.common_tools import *
# ---------------------------


def read_covid_data() -> pd.DataFrame:

    # This function import the specified data and return it as a pandas DataFrame

    data = pd.read_csv('data\owid-covid-data.csv')
    print(data['iso_code'].unique())
    location = input('Enter the location you need:')
    data = data[data['iso_code'] == location]

    return data

### How to use the function
# ---------------------------
# data = read_covid_data()

def extract_target_dataa(data: pd.DataFrame) -> pd.DataFrame:
    """
    Extract the target data from the specified DataFrame.

    Args:
        data: pd.DataFrame: The DataFrame that contains the target data.

    Returns:
        pd.DataFrame: A DataFrame containing the 'date' column and the selected target columns.
    """
    print("Available columns:", list(data.columns))
    target_columns = ['date']  # Always include 'date'
    
    while True:
        target = input("Enter a column you need (or type 'done' to finish): ").strip()
        if target.lower() == 'done':
            break
        elif target in data.columns:
            target_columns.append(target)
        else:
            print(f"Column '{target}' not found in the DataFrame. Please try again.")
    
    print("Selected columns:", target_columns)
    return data[target_columns]


### How to use the function
# ---------------------------
# date, target_data = extract_target_data(data)

def extract_SIR_target_data(data: pd.DataFrame) -> pd.DataFrame:
    
    # This function extract the target data from the specified DataFrame
    # Args:
    #     data: pd.DataFrame: The DataFrame that contains the target data
    # Returns:
    #     date: pd.Series: The date column of the DataFrame
    #     target_data: pd.Series: The target data column of the DataFrame

    data = data[['date', 'total_cases', 'new_cases', 'new_deaths', 'population']]
 
    return data
