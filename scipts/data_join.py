import pandas as pd
import os

def data_join(df1,df2, id):
    
    merge_df1_df2 = pd.merge(df1, df2, on = id)
    print(merge_df1_df2.head())
    return merge_df1_df2
    #print('test')