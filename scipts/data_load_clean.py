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
    
def clean_data(dataframes, file_name):

    #check filename is in csv files
    #***Note working
    if file_name not in dataframes:
        print(f"{file_name} not found in loaded data")
        return None
    
    #look for missing values
    #missing = file_name.isna().sum()
    #print(missing)
