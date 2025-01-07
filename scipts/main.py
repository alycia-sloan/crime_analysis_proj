from data_load_clean import *
from data_join import *

directory = 'VA-2023/data/VA'

csv_data = load_data(directory)

#csv_clean_age = load_file_data(csv_data, "NIBRS_AGE.csv")

csv_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")

remove_arrestee_column = remove_value_column(csv_arrestee, 'age_range_high_num')

#do I need to change this so that instead of csv_arrestee, it's remove_arrestee_column?
remove_arrestee_column2 = remove_value_column(csv_arrestee, 'clearance_ind')

object_change_arrestee = change_type(remove_arrestee_column2, 'arrest_date', 'datetime')

csv_weapon_type = load_file_data(csv_data, "NIBRS_WEAPON_TYPE.csv")

csv_weapon = load_file_data(csv_data, "NIBRS_WEAPON.csv")

csv_offense_type = load_file_data(csv_data, "NIBRS_OFFENSE_TYPE.csv")

csv_incident = load_file_data(csv_data, 'NIBRS_incident.csv')

csv_offense = load_file_data(csv_data, 'NIBRS_OFFENSE.csv')


offense_arrestee_join = data_join(csv_offense, csv_arrestee, "incident_id")

offense_weapon_join = data_join(offense_arrestee_join, csv_weapon, "offense_id")

weapon_type_join = data_join(offense_weapon_join, csv_weapon_type, "weapon_id")

