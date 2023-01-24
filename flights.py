#%%
import pandas as pd
from data_clean import DataClean
pd.set_option('display.max_columns', None)

#%%
# Read all the CSV files into dataframes
if __name__ == '__main__':
    path_96 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1996.csv'
    path_95 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1995.csv'
    path_94 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1994.csv'
    path_93 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1993.csv'
    path_92 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1992.csv'
    path_91 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1991.csv'
    path_90 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1990.csv'
    path_89 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1989.csv'
    path_87 = 'E:/Data Science/AiCore/Data-analytics-Tableau/1987.csv'
    df96 = pd.read_csv(path_96)
    df95 = pd.read_csv(path_95)
    df94 = pd.read_csv(path_94)
    df93 = pd.read_csv(path_93)
    df92 = pd.read_csv(path_92)
    df91 = pd.read_csv(path_91)
    df90 = pd.read_csv(path_90)
    df89 = pd.read_csv(path_89)
    df87 = pd.read_csv(path_87)

#%%
#Remove all columns and rows that have their entire values as NULL
DataClean.clean_flight_data(df96)
DataClean.clean_flight_data(df95)
DataClean.clean_flight_data(df94)
DataClean.clean_flight_data(df93)
DataClean.clean_flight_data(df92)
DataClean.clean_flight_data(df91)
DataClean.clean_flight_data(df90)
DataClean.clean_flight_data(df89)
DataClean.clean_flight_data(df87)  

#%%
#Combine all the dataframes into single dataframe
df_dict = {'df96': df96 , 'df95': df95, 'df94': df94 , 'df93': df93, 'df92': df92 , 'df91': df91, 'df90': df90 , 'df89': df89, 'df87': df87}

#%%
new_combi = pd.concat((df for _, df in df_dict.items()), ignore_index=True)
#%%
#Verify the combined dataframe
new_combi.head()
#%%
new_combi.info()

#%%
# convert "DepTime" from float to int and replace NaN values
new_combi['DepTime'] = new_combi['DepTime'].fillna(0).astype(int)

#%%
# convert "ArrTime" from float to int and replace NaN values
new_combi['ArrTime'] = new_combi['ArrTime'].fillna(0).astype(int)

#%%
# convert "FlightNum" from float to string and replace NaN values
new_combi['FlightNum'] = new_combi['FlightNum'].fillna(0).astype(str)

#%%
#Verify number of lines/records in the combined dataframe
new_combi

#There are 42722968 rows × 23 columns in the dataframe
#%%
#Convert dataframe to CSV
new_combi.to_csv('E:/Data Science/AiCore/Data-analytics-Tableau/combined_data.csv',na_rep='0')

"""
Extract dataframe from s3 bucket
path = 's3://data-analytics-migration-2-tableau/combined_data.csv'
df3 = DataExtractor.extract_from_s3(path)
"""
#%%