from data_load_clean import *

directory = 'VA-2023/data/VA'

csv_data = load_data(directory)

csv_clean = load_file_data(csv_data, "NIBRS_AGE.csv")