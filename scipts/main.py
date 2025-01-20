from data_load_clean import *
from data_join import *
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, median, mode
import pandas as pd

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

def arrestee_age_graph(csv_data):
    csv_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")
    bins = [0, 18, 25, 35, 45, 55, 65, 120]
    labels =  ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    csv_arrestee['age_group'] = pd.cut(csv_arrestee['age_num'], bins = bins, labels = labels, right = False )
    age_groups = csv_arrestee.groupby('age_group')
    age_group_counts = age_groups.size().reset_index(name = 'counts')
    age_labels = age_group_counts['age_group']
    sizes = age_group_counts['counts']
    plt.figure(figsize=(8,8))
    colors = sns.color_palette('rocket')
    plt.pie(sizes, labels = age_labels, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, colors = colors)
    plt.title("Age Distribution of Arrestees")
    plt.show()

def arrestee_age_exp(csv_data):
    csv_arrestee = load_file_data(csv_data, "NIBRS_ARRESTEE.csv")
    csv_arr_age = csv_arrestee[['age_num']].copy()
    csv_age_mean = csv_arr_age['age_num'].mean()
    csv_age_mode = csv_arr_age['age_num'].mode()
    csv_age_median = csv_arr_age['age_num'].median()
    print(f"Mean age of arrestees: {round(csv_age_mean,3)}")
    print(f"Mode age of arrestees: {round(csv_age_mode,3).iloc[0]}")
    print(f"Median age of arrestees: {round(csv_age_median,3)}")

general_weap_arr_inc_off_df = process_arrestee_offense_incident_weapon_df(csv_data)
#arrestee_age_graph(csv_data)
#weapons_to_offenses(general_weap_arr_inc_off_df)
arrestee_age_exp(csv_data)

