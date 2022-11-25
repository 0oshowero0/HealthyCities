from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/house_price')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)


msoa_lut = pd.read_csv('./city_defination_and_LUTs/msoa_look_up_table.csv')
msoa_lut = msoa_lut[['CityName','CityCode','MSOAName','MSOACode']]

mean_price = pd.read_csv('./house_price/msoa_mean_all_sales_all_house_types.csv')
median_price = pd.read_csv('./house_price/msoa_median_all_sales_all_house_types.csv')

mean_price = msoa_lut.merge(mean_price,left_on='MSOACode', right_on='MSOACode',how='left')
median_price = msoa_lut.merge(median_price,left_on='MSOACode', right_on='MSOACode',how='left')


city_name_list = []
city_code_list = []
msoa_name_list = []
msoa_code_list = []
time_list = []
type_list = []
price_list = []
for _, row in mean_price.iterrows():
    for i in range(len(row.index) - 4):
        city_name_list.append(row['CityName'])
        city_code_list.append(row['CityCode'])
        msoa_name_list.append(row['MSOAName'])
        msoa_code_list.append(row['MSOACode'])
        type_list.append('Mean')

        time_list.append(row.index[i+4])
        price_list.append(row[row.index[i+4]])

for _, row in median_price.iterrows():
    for i in range(len(row.index) - 4):
        city_name_list.append(row['CityName'])
        city_code_list.append(row['CityCode'])
        msoa_name_list.append(row['MSOAName'])
        msoa_code_list.append(row['MSOACode'])
        type_list.append('Median')

        time_list.append(row.index[i+4])
        price_list.append(row[row.index[i+4]])

house_price = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list, 'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list, 'Time':time_list, 'Aggregation':type_list, 'Price':price_list})
house_price = house_price.sort_values(['CityCode','MSOACode'], ascending=True)
house_price.to_csv(OUTPUT_PATH.joinpath('house_price_msoa.csv'),index=False)
