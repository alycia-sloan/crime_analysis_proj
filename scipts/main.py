from data_load_clean import *
from data_join import *
import seaborn as sns
import matplotlib.pyplot as plt

directory = 'VA-2023/data/VA'

csv_data = load_data(directory)

#csv_clean_age = load_file_data(csv_data, "NIBRS_AGE.csv")

#returns final_arrestee_df
def process_arrestee_offense_incident_weapon_df(csv_data):
    csv_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")
    remove_arrestee_column = remove_value_column(csv_arrestee, 'age_range_high_num')
    #do I need to change this so that instead of csv_arrestee, it's remove_arrestee_column?
    remove_arrestee_column2 = remove_value_column(csv_arrestee, 'clearance_ind')
    object_change_arrestee = change_type(remove_arrestee_column2, 'arrest_date', 'datetime')
    final_arrestee_df = object_change_arrestee

    csv_weapon = load_file_data(csv_data, "NIBRS_WEAPON.csv")
    csv_weapon_type = load_file_data(csv_data, "NIBRS_WEAPON_TYPE.csv")

    csv_offense_type = load_file_data(csv_data, "NIBRS_OFFENSE_TYPE.csv")
    csv_incident = load_file_data(csv_data, 'NIBRS_incident.csv')
    csv_offense = load_file_data(csv_data, 'NIBRS_OFFENSE.csv')

    offense_names = pd.merge(csv_offense, csv_offense_type, on = 'offense_code',how = 'left')
    offenses_weapons = pd.merge(offense_names, csv_weapon, on = 'offense_id', how = 'left')
    offenses_weapon_names = pd.merge(offenses_weapons, csv_weapon_type,on = 'weapon_id', how = 'left' )
    return offenses_weapon_names

def arrestee_age(csv_data):
    csv_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")
    csv_age = load_file_data(csv_data, 'NIBRS_AGE.csv')
    #print(csv_age['age_id'])
    age_arrestee_merge = pd.merge(csv_arrestee, csv_age, on = "age_id")
    age_df = age_arrestee_merge[['age_id']]
    #age_counts = age_arrestee_merge['age_code'].value_counts()
    #sort_age_counts = age_counts.sort_values(by = 'age_code', ascending = False)
    #print(sort_age_counts)   

'''
def weapons_to_offenses(df):
    weapon_offense_df = df[['weapon_name','offense_name']]
    counts = weapon_offense_df['weapon_name'].value_counts()
    pivot_df = pd.crosstab(df['offense_name'], df['weapon_name'])
    print(pivot_df.head())
    print(pivot_df.corr())
    #pivot_df.plot(kind = 'barh', stacked = True)
    #plt.show()
'''
general_weap_arr_inc_off_df = process_arrestee_offense_incident_weapon_df(csv_data)
arrestee_age(csv_data)
#weapons_to_offenses(general_weap_arr_inc_off_df)

