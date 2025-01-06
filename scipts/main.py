from data_load_clean import *

directory = 'VA-2023/data/VA'

csv_data = load_data(directory)

#csv_clean_age = load_file_data(csv_data, "NIBRS_AGE.csv")

csv_clean_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")

remove_arrestee_column = remove_value_column(csv_clean_arrestee, 'age_range_high_num')

remove_arrestee_column = remove_value_column(csv_clean_arrestee, 'clearance_ind')

object_change_arrestee = change_obj(remove_arrestee_column, 'arrest_date', 'datetime')