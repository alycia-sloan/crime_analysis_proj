#data_loader.py

import pandas as pd
import os


def load_data(directory):
    dataframes = {}
    try:
        #list all files in specified directory
        for file_name in os.listdir(directory):
            #only considers .csv files
            if file_name.endswith('.csv'):
                file_path = os.path.join(directory,file_name)
                #append to dictionary
                data = pd.read_csv(file_path)
                dataframes[file_name] = data
                #show which files are loaded
                #print(f'Loaded: {file_name}')
        return dataframes
        
    except Exception as e:
        print(f'Error loading {file_path}: {e}')
        return None
    
def load_file_data(dataframes, file_name):

    #check filename is in csv files
    if file_name not in dataframes:
        print(f"{file_name} not found in loaded data")
        return None
    
    #load individual file into it's own dataframe
    read_file_data = pd.read_csv('VA-2023/data/VA/' + file_name)
    #print(read_file_data.head())

    #find missing values -- **NEED TO DECIDE HOW TO HANDLE IF VALUES ARE MISSING
    print("Missing Values")
    print(read_file_data.isnull().sum())

    #check data types -- **NEED TO DECIDE HOW TO HANDLE IF TYPES ARE WRONG
    print("Checking Data Types")
    print(read_file_data.dtypes)

    

    

