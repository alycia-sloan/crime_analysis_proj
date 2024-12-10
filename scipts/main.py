from data_load_clean import *

directory = 'VA-2023/data/VA'

csv_files = load_data(directory)

csv_clean = clean_data(directory, "NIBRS_AGE.csv")