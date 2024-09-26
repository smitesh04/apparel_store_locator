import pandas as pd
import os
from db_config import DbConfig
obj = DbConfig()

path = r"C:/Users/Actowiz/Desktop/Smitesh_Docs/Project/apparel_store_locator/csv"
df_list = list()
files = os.listdir(path)
for file in files:
    df = pd.read_csv(f'{path}/{file}')
    df_list.append(df)
all_df = pd.concat(df_list)
unique_provider = list(all_df['12'].unique())
unique_list = []
for i in unique_provider:
    if type(i) == str:
        i = i.strip()
    if i not in unique_list:
        unique_list.append(i)
for provider in unique_list:
    if type(provider) == str:
        if provider != 'Provider':
            qr = f'insert into unique_provider(provider) values("{provider.strip()}")'
            obj.cur.execute(qr)
            obj.con.commit()

